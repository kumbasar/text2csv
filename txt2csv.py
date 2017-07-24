import csv

file=open("taf.csv", 'w')
str = ""
with open('taf.txt') as openfileobject:
    for line in openfileobject:
        for letter in line:
            if letter!='=':
                str+=letter
            else:
                str+=';'
        file.write(str)
        str=""
file.close()