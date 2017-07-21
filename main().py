import csv

file=open("tag.csv", 'w')
str = ""
with open('tag.txt') as openfileobject:
    for line in openfileobject:
        for letter in line:
            if letter!='=':
                str+=letter
            else:
                str+=';'
        file.write(str)
        str=""

file.close()