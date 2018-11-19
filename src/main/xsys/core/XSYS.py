#!/usr/bin/env python
from src.main.xsys.core.Configurator import Configurator
from src.main.xsys.core.SuperBase import SuperBase


class XSYS(Configurator, SuperBase):
    """
        [Description]
        __init__
        - Construct a XSYS Object
    """
    def __init__(self):
        super(XSYS, self).__init__()
