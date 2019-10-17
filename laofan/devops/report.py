import subprocess

import emails

if __name__ == "__main__":
    command = 'goaccess -f /opt/log/access.log > report.html'
    subprocess.check_call(command,shell=True)
    emails.Email().send('Nginx-log','Hello, Boy!','./report.html')
