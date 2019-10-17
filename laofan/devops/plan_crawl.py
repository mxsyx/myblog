import os
import sys
import time
import shutil
import MySQLdb
import datetime
import subprocess

import config
import emails


class Crawl(object):
    def __init__(self):
        self._email = emails.Email()
        self._start_time = time.time()

    def _reset_log(self):
        error_messages = []
        with open(config.ERRORLOG, 'r+') as f:
            error_messages.extend(f.readlines())
            f.seek(0)
            f.truncate()
        with open(config.ERRORLOG_BACKUP, 'a') as f:
            f.writelines(error_messages)

        info_messages = []
        with open(config.INFOLOG, 'r+') as f:
            info_messages.extend(f.readlines())
            f.seek(0)
            f.truncate()
        with open(config.INFOLOG_BACKUP, 'a') as f:
            f.writelines(info_messages)

    def _analysis(self):
        info_messages = []
        with open(config.INFOLOG, 'r') as f:
            info_messages.extend(f.readlines())
        error_messages = []
        with open(config.ERRORLOG, 'r') as f:
            error_messages.extend(f.readlines())

        self._end_time = time.time()
        consume = self._end_time - self._start_time
        content = "更新 -> %s\n错误 -> %s\n耗时 -> %smin\n\n%s\n\n\n%s" % (
            len(info_messages), round(len(error_messages)/3),
            int(consume/60), info_messages, error_messages
        )
        return content

    def _connectdb(self):
        command = ['mysqld_multi']
        command.extend(['start', '3307'])
        subprocess.call(command, stdout=sys.stdout)
        time.sleep(5)
        return self._check_connect()

    def _check_connect(self):
        try:
            MySQLdb.connect(
                unix_socket=config.UNIX_SOCKET, db=config.MYSQL_DBNAME,
                user=config.MYSQL_USER, passwd=config.MYSQL_PASSWORD,
                charset='utf8', use_unicode=True
            )
            return True
        except MySQLdb.OperationalError as e:
            self._email.send('3307数据库连接失败', str(e))
            return False

    def _closedb(self):
        command = ['mysqld_multi']
        command.extend(['stop', '3307'])
        subprocess.call(command, stdout=sys.stdout)

    def _backupdb(self):
        today = datetime.date.today().strftime("%Y-%m-%d")
        ago = (datetime.datetime.now()-datetime.timedelta(days=31))
        data_path = '/opt/backup/data/DATAbackup%s.sql'

        command = ['mysqldump']
        command.extend(['-S', '/opt/mysqldtd/mysqld.sock'])
        command.extend(['-uroot', '-p201920', 'redtea'])

        with open(data_path % today, 'w') as f:
            try:
                subprocess.check_call(command, stdout=f)
                #os.remove(data_path % ago.strftime("%Y-%m-%d"))
            except subprocess.CalledProcessError as e:
                self._email.send('3308数据库备份错误', str(e))

    def _backupurl(self):
        src = '/opt/laofan/laofan/tmp/%s'
        dst = '/opt/backup/url/%s'
        for file in config.FILES:
            shutil.copyfile(src % file, dst % file)

    def _crawl(self):
        for item in config.ITEMS:
            command = ['scrapy']
            command.extend(['crawl', 'Homepage'])
            command.extend(['-a', 'start_url=%s' % item[0]])
            command.extend(['-a', 'increment_low=%s' % item[1]])
            command.extend(['-a', 'increment_high=%s' % item[2]])
            command.extend(['-a', 'video_type=%s' % item[3]])
            try:
                subprocess.check_call(command, stdout=sys.stdout)
                if not self._crawl_info(item[4:7]):
                    return False
            except subprocess.CalledProcessError:
                self._closedb()
                self._email.send('爬行主页任务出错', str(item))
                return False
        return True

    def _crawl_info(self, item):
        command = ['scrapy']
        command.extend(['crawl', '%s' % item[0]])
        command.extend(['-a', 'increment_low=%s' % item[1]])
        command.extend(['-a', 'increment_high=%s' % item[2]])
        try:
            subprocess.check_call(command, stdout=sys.stdout)
            return True
        except subprocess.CalledProcessError:
            self._closedb()
            self._email.send('爬行信息任务出错', str(command))
            return False

    def _task_completed(self):
        command = ['closeChromeDriver']
        subprocess.call(command)
        content = self._analysis()
        self._email.send("任务完成", content)

    def start(self):
        self._reset_log()
        if self._connectdb():
            self._crawl()
            self._closedb()
        self._backupurl()
        self._backupdb()
        self._task_completed()


if __name__ == '__main__':
    os.chdir(config.ROOT_DIR)
    crawl = Crawl()
    crawl.start()
