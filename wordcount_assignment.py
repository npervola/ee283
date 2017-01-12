# coding: utf-8

with open('gpl-3.0.txt','r') as f:
    file = f.readlines()
    
file=''.join(file)

from collections import Counter

file2=file.translate(None,string.punctuation).replace('\n',' ').lower()
c = Counter()
for line in file2.splitlines():
    c.update(line.split())
print(c)
len(c)
