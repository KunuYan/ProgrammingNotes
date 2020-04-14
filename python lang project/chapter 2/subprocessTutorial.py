import os
import subprocess as sub

os.chdir(r'C:\Users\male-\OneDrive\Documents\python lang project\chapter 2\root')

print(sub.call(['cmd', '/c', 'dir', '/b']))
#print(sub.call(['cmd', '/c', 'dir', '/b'], stdout=open('ls.txt', 'w')))
print(sub.call(['cmd', '/c', 'type', 'ls.txt']))
