import sys
import psutil
import subprocess
import emails


def get_program_names():
    pids = psutil.pids()
    names = []
    for pid in pids:
        program = psutil.Process(pid)
        names.append(program.name())
    return names


def check_close(email):
    names = get_program_names()
    count_mysqld = names.count('mysqld')
    count_chromium = names.count('chromium')
    count_chromedriver = names.count('chromedriver')
    if count_mysqld > 1:
        tips = '3307数据库未关闭'
        command = ['3307stop']
        if not subprocess.check_call(command):
            content = '关闭成功'
        else:
            content = '关闭失败'
        email.send(tips, content) 
    if count_chromium > 0 or count_chromedriver > 0:
        tips = 'chrome未关闭'
        command = ['closeChromeDriver']
        subprocess.call(command)
        email.send(tips, tips) 


def check_alive(email):
    names = get_program_names()

    if 'uwsgi' not in names:
        tips = 'UWSGI挂掉'
        command = ['ustart']
        if not subprocess.check_call(command):
            content = '重启成功'
        else:
            content = '重启失败'
        email.send(tips, content)

    if 'nginx' not in names:
        tips = 'NGINX挂掉'
        command = ['nstart']
        if not subprocess.check_call(command):
            content = '重启成功'
        else:
            content = '重启失败'
        email.send(tips, content)

    if 'mysqld' not in names:
        tips = 'MYSQLD挂掉'
        command = ['3308start']
        if not subprocess.check_call(command):
            content = '重启成功'
        else:
            content = '重启失败'
        email.send(tips, content)



if __name__ == "__main__":
    email = emails.Email()
    entrances = sys.argv[1]
    if entrances == 'checkalive':
        check_alive(email)
        sys.exit(0)
    if entrances == 'checkclose':
        check_close(email)
        sys.exit(0)
