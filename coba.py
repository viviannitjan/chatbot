import re
from sys import argv
script, first = argv

stopwords = ["is","an","the","on","of","was","in","for","does","do","'ve","a","or","to","and","any","are","been"]

#Imort file jawaban
file = open('jawaban.txt','r',encoding="utf8")
jawaban = file.read()
file.close()
jawaban = jawaban.split('~')

#import file pertanyaan
file = open('pertanyaan.txt','r',encoding="utf8")
pertanyaan = file.read()
file.close()
pertanyaan = pertanyaan.split('\n')

#Daftar pertanyaan dirubah semua ke huruf kecil
for i in range(len(pertanyaan)-1):
    pertanyaan[i] = pertanyaan[i].lower()

#ini function buat pakai regex
def metode_regex(query):
    query = query.split(' ')
    #Kalau kata pertama nya stopwords bakal hilang jadi char pertama ga boleh ^
    if (query[0] in stopwords):
        hasil = ""
    else :
        hasil = "^"

    #hapus stopwords
    i = 0
    while (i < len(query)):
        if(query[i] in stopwords):
            del query[i]
            i = 0
        else :
            i += 1

    #rubah inputan ke regex
    for i in range(len(query)-1):
        hasil += query[i] + ".*"
    #terakhir ? harus diganti \?$
    query[len(query)-1] = query[len(query)-1][:-1]
    hasil += query[len(query)-1] + "\?$"
    
    #Cek huruf besar
    t = list(hasil)
    i = 0
    for c in t:
        if c.isupper():
            pengganti = "(" + c + "|" + c.lower() + ")"
            t[i] = pengganti
        i+=1
    hasil = ''.join(t)
    print(hasil)

    #Cari di list pertanyaan ada ga
    for i in range(23):
        x = re.search(hasil, pertanyaan[i])
        if (x):
            print(jawaban[i])
            break

metode_regex(first)