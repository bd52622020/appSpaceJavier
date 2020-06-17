
import re
import os
from shutil import copyfile

html_files = [f for f in os.listdir('.') if re.search('(.html)$', f)]
print(html_files)

for html_file in html_files:
    src = './' + html_file
    dst = './copy_' + html_file
    copyfile(src, dst)
    
