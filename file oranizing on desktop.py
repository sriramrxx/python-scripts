import os
import re
import shutil

def folder_name():
    #folder_name = (raw_input('Enter the folder name as per the pc :'))
    os.chdir('C:\Users\sri\Desktop')
    list = os.listdir(os.getcwd())
    return list

def seperatingfile(list):
    pdflist=[]
    for i in list:
        i=i.lower()
        pderedex=re.compile(r'.*.pdf')
        mo = pderedex.findall(i)
        if mo:
            pdflist.append(i)

    wordlist=[]
    for i in list:
        i = i.lower()
        pderedex=re.compile(r'.*.docx')
        mo = pderedex.findall(i)
        if mo:
            wordlist.append(i)
    pptlist=[]
    for i in list:
        i = i.lower()
        pderedex=re.compile(r'.*.pptx')
        mo = pderedex.findall(i)
        if mo:
            pptlist.append(i)
    return pdflist,wordlist,pptlist

def gettingsub():
    sub=[]
    sub1 = 'scam'.lower()
    sub2 = ' toc'.lower()
    sub3 = 'bigdata'.lower()
    sub4 = 'reuse'.lower()
    sub5 = 'aod'.lower()
    sub6 = 'soft'.lower()
    sub7 = 'lean'.lower()
    sub8 = 'iip'.lower()
    sub9 = '15MIS0057'.lower()
    sub= sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8
    return sub,sub9

def crosscheck(pdflist,wordlist,pptlist,sub1):
    pdfnamelist=[]
    pdf_match = []
    for i in pdflist: #deleting the pdf
        pdfname = re.compile(r'(.*).pdf')
        mo= pdfname.search(i)
        pdfnamelist.append(mo.group(1))
    for i in pdfnamelist:
        for j in sub1:
            if i.__contains__(j):
               pdf_match.append(i)

    wordnamelist = []
    word_match = []
    for i in wordlist:  # deleting the pdf
        pdfname = re.compile(r'(.*).docx')
        mo = pdfname.search(i)
        wordnamelist.append(mo.group(1))
    for i in wordnamelist:
        for j in sub1:
            if i.__contains__(j):
                word_match.append(i)

    pptnamelist = []
    ppt_match = []
    for i in pptlist:  # deleting the pdf
        pdfname = re.compile(r'(.*).pptx')
        mo = pdfname.search(i)
        pptnamelist.append(mo.group(1))
    for i in pptnamelist:
        for j in sub1:
            if i.__contains__(j):
                ppt_match.append(i)

    return pdf_match,word_match,ppt_match

def create_folder(sub,sub9):
    os.chdir('Z:\\6th sem')
    for i in sub:
        path=os.getcwd()+'\\'+i
        if os.path.exists(path):
            pass
        else: os.makedirs(path)
        path=os.getcwd()+"\\"+'sub9'
        if os.path.exists(path):
            pass
        else: os.makedirs(path)

def downloads():
    download=[]
    os.chdir('C:\Users\sri\Downloads')
    downloadfile=os.listdir(os.getcwd())
    for i in downloadfile:
        i=i.lower()
        pderedex=re.compile(r'(.*).pdf')
        mo = pderedex.search(i)
        if mo:
            download.append(i)
        pderedex=re.compile(r'(.*).docx')
        mo = pderedex.findall(i)
        if mo:
            download.append(i)
        pderedex=re.compile(r'(.*).pptx')
        mo = pderedex.findall(i)
        if mo:
            download.append(i)
    mis_match=[]
    for j in download:
        if (j.__contains__('15mis') or j.__contains__('vl2017')) :
            print j
            mis_match.append(j)
    for i in mis_match:
            if (i.__contains__('15mis') or i.__contains__('vl2017')) :
                src =os.getcwd()+"\\"+i
                dest =os.getcwd()+"\\"+sub9+"\\"+i
                shutil.move(src,dest)

def send_to_folder(pdf,word,ppt,sub):
    for i in pdf:
        for j in sub:
            if i.__contains__(j):
                src ='C:\Users\sri\Desktop'+"\\"+i+".pdf"
                dest = os.getcwd()+"\\"+j+"\\"+i+".pdf"
                shutil.move(src,dest)

    for i in word:
        for j in sub:
            if i.__contains__(j):
                src ='C:\Users\sri\Desktop'+"\\"+i+".docx"
                dest = os.getcwd()+"\\"+j+"\\"+i+".docx"
                shutil.move(src,dest)

    for i in ppt:
        for j in sub:
            if i.__contains__(j):
                src ='C:\Users\sri\Desktop'+"\\"+i+".pptx"
                dest = os.getcwd()+"\\"+j+"\\"+i+".pptx"
                shutil.move(src,dest)

if __name__ == '__main__':
    list=folder_name()
    pdflist,wordlist,pptlist=seperatingfile(list)
    sub,sub9 = gettingsub()
    pdf,word,ppt=crosscheck(pdflist,wordlist,pptlist,sub)
    create_folder(sub,sub9)
    send_to_folder(pdf,word,ppt,sub)
    downloads()
