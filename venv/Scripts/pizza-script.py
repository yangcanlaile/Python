#!"E:\Program Files (x86)\Python\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'Pizza==0.1.2','console_scripts','pizza'
__requires__ = 'Pizza==0.1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Pizza==0.1.2', 'console_scripts', 'pizza')()
    )
