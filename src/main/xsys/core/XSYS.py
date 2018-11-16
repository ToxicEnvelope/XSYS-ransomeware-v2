#!/usr/bin/env python
from src.main.xsys.smtp.MailSender import Sender
from src.main.xsys.cryptography.CryptoManager import Crawler


class XSYS(Crawler, Sender):

    def __init__(self):
        super(XSYS, self).__init__()
