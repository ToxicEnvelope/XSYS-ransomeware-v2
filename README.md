# XSYS-ransomeware-v2

Any potentially malicious content in this repository is for testing/educational purposes and should be approached with caution.

Updated version on XSYS-ransomeware Project!


XSYS-ransomeware-v2 : Ransomeware Trojan


This is a Ransomeware Trojan program.
this program divided by modules:

---
###GUI Module:
######(src.main.xsys.ui)

    * Menu.py             -   Responsible for main loop logic and GUI as a Console / teminal application.
---
###Core Modules:
######(src.main.xsys.core)

    * Configurator.py     -   The main configuration module, handle both MenuConfig and CrawlerConfig.
    
    * XSYS.py             -   The main logic mudule, handle the core functionalities of Crawler and MailSender.
---
###Config Modules:
######(src.main.xsys.config)

    * MenuConfig.py       -   The menu configuration module, used to divid properties and some flags.
    
    * CrawlerConfig.py    -   The crawler configutation module, responsileb to store critical properties as the main loop running.
---   
###SMTP Module:
######(src.main.xsys.smtp)

    * MailSender.py       -   This module responsile to send notifications by emails via TorNet.
--- 
###Crawler Module:
######(src.main.xsys.crawlers)

    * Crawler.py          -   This module responsible to manage the crawling and scannig events in the system,  
                              Also, will use to add statistics about the system and display GUI tree pattens in the system.
---                            
###Cryptography Module:
######(src.main.xsys.cryptography)

    * CryptoManager.py    -   This module responsible of all cryptography oporations such as AES, SHA256 and CDC block
                               manipulations on files system.                             
---
Compile and Execute:    
    In order to complie and execute this project,
    you want to install `pyinstaller` module.
    Follow the instruction below in the link about the HOW-TO compile to .exe
    
    Link: https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263
    
    NOTE:
        * Our main module that responsible to run the program is `Menu.py`
          therefore, it should be used as source of compilation! 
        
          We could use this command:
            `pyinstaller --onefile <Relative_Path_Of_Module>`
          example:
            `pyinstaller --onefile ./src.main.xsys.ui.Menu.py`
            
        * Once compiled new directories will appear at our PROJ_ROOT_DIR, 
            -> build : contain all relevant stack inside a sub-directory named after the module compiled
            -> dist  : contain the executable binary file  
