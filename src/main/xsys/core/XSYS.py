#!/usr/bin/env python
from src.main.xsys.core.Configurator import Configurator
from main.xsys.utils.DelegateCore import DelegateCore


class XSYS(Configurator, DelegateCore):
    """
        [Description]
        __init__
        - Construct a XSYS Object
    """
    def __init__(self):
        super(XSYS, self).__init__()
