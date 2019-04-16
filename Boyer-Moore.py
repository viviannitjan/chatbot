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


def metode_bm(query):
    #menghasilkan jawaban
    percentage = {}
    for i in range (len(pertanyaan_modif)):
        percentage[i] = bm(query,pertanyaan_modif[i])
    
    #sorting value of percentage
    percentage = sorted(percentage.items(), key=lambda item: item[1], reverse=True)
    jsonpass = []

    if (percentage[0][1]>=0.9):
        # print(jawaban[percentage[0][0]])
        jsonpass.append(jawaban[percentage[0][0]])
    else:
    #     print("Apakah yang anda maksud: ")
    #     print(pertanyaan_asli[percentage[0][0]])
    #     print(pertanyaan_asli[percentage[1][0]])
    #     print(pertanyaan_asli[percentage[2][0]])

        jsonpass.append("Apakah yang anda maksud: ")
        jsonpass.append(pertanyaan_asli[percentage[0][0]])
        jsonpass.append(pertanyaan_asli[percentage[1][0]])
        jsonpass.append(pertanyaan_asli[percentage[2][0]])
    return json.dumps(jsonpass)

def bm(query,text):
    #searching query in text, return the percent
    #process input : remove stopwords
    query = query.lower()
    query_words = remove_stopwords(query)
    inp = " ".join(query_words)
    percent = 0
    inp_len = len(inp)
    txt_len = len(text)

    #to save last occurence
    last_occ = dict((k,-1) for k in string.ascii_lowercase)
    
    for i in range(0, inp_len):
        last_occ[inp[i]]=i
    
    #search with booye moore algorithm
    i = inp_len-1
    j = inp_len-1
    while (j<=txt_len-1):
        if(inp[i]==text[j]):
            #if same
            if (i==0):
                return (inp_len-1-i)/(txt_len-1)
            else:
                i-=1
                j-=1
        else:
            #not same
            percent = max(percent,(inp_len-1-i)/(txt_len-1))
            if (text[j] not in last_occ.keys()):
                last=-1
            else:
                last = last_occ[text[j]]
            j=j+inp_len-min(i,1+last)
            i=inp_len-1
    
    return percent

metode_bm(first)