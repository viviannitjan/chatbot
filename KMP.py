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

def metode_kmp(query):
    percentage = {}
    for i in range (len(pertanyaan_modif)):
        percentage[i] = kmp(query,pertanyaan_modif[i])
                                                                         
    #sorting value of percentage
    percentage = sorted(percentage.items(), key=lambda item: item[1], reverse=True)
    jsonpass =  []
    if (percentage[0][1]>=0.9):
        jsonpass.append(jawaban[percentage[0][0]])
        # print(jawaban[percentage[0][0]])
    else:
        # print("Apakah yang anda maksud: ")
        # print(pertanyaan_asli[percentage[0][0]])
        # print(pertanyaan_asli[percentage[1][0]])
        # print(pertanyaan_asli[percentage[2][0]])
        jsonpass.append("Apakah yang Anda maksud : ")
        jsonpass.append(pertanyaan_asli[percentage[0][0]])
        jsonpass.append(pertanyaan_asli[percentage[1][0]])
        jsonpass.append(pertanyaan_asli[percentage[2][0]])
    return json.dumps(jsonpass)

def kmp(query,text) :
    #seaching with kmp algo
    #processing query
    query = query.lower()
    query_words = remove_stopwords(query)
    inp = " ".join(query_words)
    inp_len = len(inp)
    txt_len = len(text)
    percent = 0

    #search for longest prefix that is also suffix
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


    #kmp algo
    i=0
    j=0
    while (i<txt_len):
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
        # print(percent)
    return percent

metode_kmp(first)