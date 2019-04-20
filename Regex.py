import re
import json
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from sys import argv
script, first = argv

# stopwords = [" ","is","an","the","on","of","was","in","for","does","do","'ve",
# "a","or","to","and","any","are","been","untuk","di","ini","sudah","saja","yang",
# "adalah","oleh","dalam"]
stopwords = set(stopwords.words('english'))

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

def cari_synonim(query):
    sinonim_query = []
    query_displit = query.split(' ')
    for i in range(len(query_displit)):
        sinonim_kata_ke_i = []
        for syn in wordnet.synsets(query_displit[i]):
            for l in syn.lemmas():
                sinonim_kata_ke_i.append(l.name())
        sinonim_kata_ke_i = list(set(sinonim_kata_ke_i))

        for j in range(len(sinonim_kata_ke_i)):
            copy_query = query
            copy_query = copy_query.replace(query_displit[i],sinonim_kata_ke_i[j])
            # print(query_displit[i], sinonim_kata_ke_i[j])
            # print(copy_query)
            sinonim_query.append(copy_query)
    return sinonim_query


global jsonpass
jsonpass = []
#ini function buat pakai regex
def metode_regex(query):
    global jsonpass
    jsonpass = []
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
            jsonpass.append(jawaban[i])
            print(jawaban[i])
            break
    # return json.dumps(jsonpass)
    
daftar_pertanyaan = cari_synonim(first)
daftar_pertanyaan.append(first)
# print(daftar_pertanyaan)
while (i < len(daftar_pertanyaan) and len(jsonpass) == 0):
    metode_regex(daftar_pertanyaan[i])
    i += 1
