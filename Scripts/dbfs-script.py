#!c:\users\java\documents\github\economic-impacts-on-music\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'databricks-cli==0.16.6','console_scripts','dbfs'
__requires__ = 'databricks-cli==0.16.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('databricks-cli==0.16.6', 'console_scripts', 'dbfs')()
    )
