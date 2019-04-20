import string
import nltk
from nltk.corpus import wordnet
from sys import argv
script, first = argv
import json

stopwords = ["is","an","the","on","of","was","in","for","does","do","'ve",
"a","or","to","and","any","are","been","untuk","di","ini","sudah","saja","yang",
"adalah","oleh","dalam"]

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
    percent=[(0,0), (1,0)]
    # print()
    for j in range(0, len(query)):
        percentage = {}
        for i in range (len(pertanyaan_modif)):
            percentage[i] = kmp(query[j],pertanyaan_modif[i])                                                            
        #sorting value of percentage
        percentage = sorted(percentage.items(), key=lambda item: item[1], reverse=True)
        if(percent[0][1]<percentage[0][1]):
            percent=percentage
    # print(percent)
    jsonpass =  []
    if (percent[0][1]>=0.9):
        jsonpass.append(jawaban[percent[0][0]])
        # print(jawaban[percentage[0][0]])
    elif (percent[0][1]>=0.3):
        # print("Apakah yang anda maksud: ")
        # print(pertanyaan_asli[percentage[0][0]])
        # print(pertanyaan_asli[percentage[1][0]])
        # print(pertanyaan_asli[percentage[2][0]])
        jsonpass.append("Apakah yang Anda maksud : ")
        jsonpass.append(pertanyaan_asli[percent[0][0]])
        jsonpass.append(pertanyaan_asli[percent[1][0]])
        jsonpass.append(pertanyaan_asli[percent[2][0]])
    else :
        jsonpass.append("Sepertinya anda salah bertanya, coba lagi dengan pertanyaan lain")
    return json.dumps(jsonpass)

def search_same(query,text,i):
    count = 0
    j=0
    while (i+j<len(text)) and (j<len(query)):
        if(query[j]==text[i+j]):
            count+=1
        j+=1
    return count/len(text)

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
    # print(inp_len)
    # print(txt_len)
    # print(inp)
    # print(text)
    percent_j=search_same(inp,text,0)
    # print(percent_j)
    while (i<txt_len):
        if(inp[j]==text[i]):
            if(j==inp_len-1):
                # print('a')
                # print(j)
                return (j+1)/(txt_len)
            i+=1
            j+=1
        elif (j>0): 
            percent = max(percent,percent_j)
            j=longest[j-1]
            percent_j = search_same(inp,text,j)
        else:
            percent = max(percent,percent_j)
            i+=1
            percent_j = search_same(inp,text,j)
        # print(percent)
    return percent

daftar_pertanyaan = cari_synonim(first)
daftar_pertanyaan.append(first)
# print(daftar_pertanyaan)
print(metode_kmp(daftar_pertanyaan))
# print(kmp(first,pertanyaan_modif[0]))
# print(get_synonyms("active"))
# print(search_same("what","what python?",0))
# percent={0:0, 1:0}
# print(percent[1])