import time
import config
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email():
    def __init__(self):
        try:
            self._server = smtplib.SMTP_SSL(host=config.SMTP_SERVER)
        except Exception as e:
            print("\nemail init error -> %s" % str(e))

    def _connect(self):
        try:
            self._server.connect(host=config.SMTP_SERVER, port=config.SMTP_PORT)
        except Exception as e:
            print("\nemail connect error -> %s" % str(e))
        try:
            self._server.helo()
            self._server.ehlo()
            self._server.login(config.SOURCE_ADDR, config.SMTP_PASSWORD)
        except Exception as e:
            print("\nemail login error -> " + str(e))

    def _attach_file(self, msg, filename):
        try:
            with open(filename, 'rb') as f:
                mime_file = MIMEBase('text', 'plain',
                                     filename=filename.split('/')[-1])
                mime_file.add_header('Content-Disposition', 'attachment',
                                     filename=filename.split('/')[-1])
                mime_file.add_header('Content-ID', '<0>')
                mime_file.add_header('X-Attachment-Id', '0')
                mime_file.set_payload(f.read())  # read attachment information
                encoders.encode_base64(mime_file)
                msg.attach(mime_file)
        except Exception as e:
            print(str(e))

    def send(self, headline, context, filename=''):
        try:
            self._connect()
            msg = MIMEMultipart()
            
            mime_text = MIMEText(context, 'plain', 'utf-8')
            msg.attach(mime_text)
            msg['Subject'] = Header(headline, 'utf-8').encode()
            msg['From'] = config.SOURCE_ADDR
            msg['To'] = config.TARGET_ADDR
            
            if filename:
                self._attach_file(msg, filename)
            
            self._server.sendmail(config.SOURCE_ADDR,
                                  config.TARGET_ADDR, msg.as_string())
            self._server.close()
        except Exception as e:
            print("\nemail send error -> %s" % str(e))

