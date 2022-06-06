from ntpath import join
import string
import pdfplumber
import os
import re


def getPagesLen(path):
    with pdfplumber.open(path) as pdf:
        a = len(pdf.pages)
        pdf.close
        return a



def getAll(path):
    print("\nLoading text. This may take a while.\n")
    letters = []
    with pdfplumber.open(path) as pdf:
        n = getPagesLen(join(dirname, "files/KC.pdf"))
        j = 0
        while (j<n):
            page = pdf.pages[j]
            top = page.chars[0]["top"]
            for i, char in enumerate(page.chars):
                if char["top"] != top:
                    top = char["top"]
                letters.append(char["text"])
            text = ''.join(letters)
            j += 1
            all = ''.join(text)
        pdf.close
        
    return (all)


def getAllArts():
    Arts = []
    a = getAll(join(dirname, "files/KC.pdf"))
    Arts = re.findall(r"(?<=Art\. )(.+?)(?=Art\. )", a)
    for i in Arts:
        i = "Art." + i
    return Arts


#reSearch returns text that fulfills user's regular expression
def reSearch():
    Arts = getAllArts()
    print("Enter a regular expression:\n")
    crit = input()
    escape = True
    is_valid = isRegex(crit)
    if is_valid:
        re.compile(crit)
        a = re.findall(crit, Arts)
        return a
    else:
        return 0
        

#searchArts returns all articles that contain user's regular expression. typing "\d+" will return all articles.
def searchArts():
    Arts = getAllArts()
    print("Enter a regular expression:\n")
    crit = input()
    b = []
    escape = True
    is_valid = isRegex(crit)
    if is_valid:
        re.compile(crit)
        for i in Arts:
            a = re.findall(crit, i)
            if a:
                b.append(i)
                a = []
        return b
    else:
        return 0


def isRegex(crit):
    try:
        re.compile(crit)
        return 1
    except re.error:
        return 0




dirname = os.path.dirname(__file__)

a = searchArts()
#a = reSearch()

for i in a:
    print(i, "\n")

if(not a):
    print("No matches found for this regular expression")
