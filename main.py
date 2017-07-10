import re, os
import svn.local
import subprocess


homeDir = "/home/wulf/workspace/share/"
#homeDir = "/home/wulf/fonts"
excludeDir = set([".m2","bin",".svn",".metadata",".idea"])
excludefile = set(["*.gz"])


import fnmatch
import os
import os.path
import re

includes = ['*.java', '*.xml'] # for files only
excludes = ['*.m2','*/bin/*','*.svn','*.metadata',"*.idea"] # for dirs and files

# transform glob patterns to regular expressions
includes = r'|'.join([fnmatch.translate(x) for x in includes])
excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'

for root, dirs, files in os.walk(homeDir):

    # exclude dirs
    dirs[:] = [os.path.join(root, d) for d in dirs]
    dirs[:] = [d for d in dirs if not re.match(excludes, d)]

    # exclude/include files
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if not re.match(excludes, f)]
    files = [f for f in files if re.match(includes, f)]

    for fname in files:
        p = subprocess.Popen("svn info "+fname, stdout = subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        print (output)
	

'''
def return_dir(j):
    return os.listdir(j)
'''


