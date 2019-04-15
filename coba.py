import re
import string
from sys import argv
script, first = argv
import json

stopwords = ["is","an","the","on","of","was","in","for","does","do","'ve",
"a","or","to","and","any","are","been","untuk","di","ini","sudah","saja","yang",
"adalah","oleh","dalam"]

#fungsi untuk remove stopwords
def remove_stopwords(query):
    query_word = query.split(' ')

    #hapus stopwords
    i = 0
    while (i < len(query_word)):
        if(query_word[i] in stopwords):
            query_word.remove(query_word[i])
            i = 0
        else :
            i += 1
    return query_word

#Import file jawaban
file = open('jawaban.txt','r',encoding="utf8")
jawaban = file.read()
file.close()
jawaban = jawaban.split('~')

#import file pertanyaan
file = open('pertanyaan.txt','r',encoding="utf8")
pertanyaan_asli = file.read()
pertanyaan_modif = pertanyaan_asli
file.close()
pertanyaan_asli = pertanyaan_asli.split('\n')
pertanyaan_modif = pertanyaan_modif.split('\n')


#Daftar pertanyaan dirubah semua ke huruf kecil
for i in range(len(pertanyaan_asli)-1):
    pertanyaan_modif[i] = pertanyaan_asli[i].lower()
    query_word = remove_stopwords(pertanyaan_modif[i])
    pertanyaan_modif[i] = " ".join(query_word)

#ini function buat pakai regex
def metode_regex(query):
    query_sudah_displit = query.split(' ')
    #Kalau kata pertama nya stopwords bakal hilang jadi char pertama ga boleh ^
    if (query_sudah_displit[0] in stopwords):
        hasil = ""
    else :
        hasil = "^"

    #hapus stopwords
    query_word = remove_stopwords(query)

    #rubah inputan ke regex
    for i in range(len(query_word)-1):
        hasil += query_word[i] + ".*"
    #terakhir ? harus diganti \?$
    query_word[len(query_word)-1] = query_word[len(query_word)-1][:-1]
    hasil += query_word[len(query_word)-1] + "\?$"
    
    #Cek huruf besar
    t = list(hasil)
    i = 0
    for c in t:
        if c.isupper():
            pengganti = "(" + c + "|" + c.lower() + ")"
            t[i] = pengganti
        i+=1
    hasil = ''.join(t)
    
    #Cari di list pertanyaan ada ga
    for i in range(len(pertanyaan_asli)):
        x = re.search(hasil, pertanyaan_asli[i])
        if (x):
            jsonpass = jawaban[i]
            # print(jawaban[i])
            break
    return json.dumps(jsonpass)

def metode_kmp(query):
    percentage = {}
    for i in range (23):
        print(pertanyaan_modif[i])
        percentage[i] = kmp(query,pertanyaan_modif[i])
    # print(percentage)

def kmp(query,text) :
    query_words = remove_stopwords(query)
    inp = " ".join(query_words)
    print(inp)
    inp_len = len(inp)
    txt_len = len(text)
    percent = 0

    longest = [0]
    i=0
    j=1
    while (j<txt_len):
        if(text[i]==text[j]):
            longest.append(i+1)
            i+=1
            j+=1
        else:
            if(i>0):
                i=longest[i-1]
            else:
                longest.append(0)
                j+=1
    # print(longest)

    i=0
    j=0
    while (i<txt_len):
        print(inp[j],text[i])
        if(inp[j]==text[i]):
            if(j==inp_len-1):
                return j/(txt_len-1)
            i+=1
            j+=1
        elif (j>0): 
            percent = max(percent,j/(txt_len-1))
            j=longest[j-1]
        else:
            percent = max(percent,j/(txt_len-1))
            i+=1
        print(percent)
    return percent

# metode_kmp("what is python?")
# print(kmp("what is python?",pertanyaan_modif[0]))
#metode_regex(first)
