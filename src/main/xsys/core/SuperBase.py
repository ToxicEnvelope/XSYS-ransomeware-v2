#!/usr/bin/env python
from src.main.xsys.crawlers.Crawler import Crawler
from src.main.xsys.smtp.MailSender import Sender


class SuperBase(Crawler, Sender):
    """
        [Description]
        __init__
        - Construct a SuperBase Object
    """
    def __init__(self):
        super(SuperBase, self).__init__()
