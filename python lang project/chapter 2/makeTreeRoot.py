import os, glob, shutil as sh
from os import path

os.chdir(r'C:\Users\male-\OneDrive\Documents\python lang project\chapter 2\TreeRoot')

newFiles = ['FA.txt', 'FB.txt']
cwd = os.getcwd()
for file in newFiles:
    filePath = os.path.join(cwd, file)
    print(filePath)
    with open(filePath, 'w') as f:
        f.write('Content for ' + file)
