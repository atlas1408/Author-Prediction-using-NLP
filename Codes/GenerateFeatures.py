import pandas
import os
import csv
#   Target Labels:  Frank -0 , Ballantyne -1
Final = []
ignore = [".",",",":","``","''","POS"]
temp = os.listdir("D:\\ProjectBooksBigData\\CSV_Frank\\")
label =0
readfiles = 0
writefiles = 0
for x in temp:
    noun_count = 0
    adjective_count = 0
    verb_count = 0
    adverb_count = 0
    conjunction_count = 0
    word_count = 0
    total_word_len = 0
    to_count = 0
    file_read=pandas.read_csv("D:\\ProjectBooksBigData\\CSV_Frank\\" +x,usecols=[1,2],encoding='ISO-8859-1')
    readfiles+=1
    for i,r in file_read.iterrows():
        if r[1] not in ignore:
            word_count += 1
            total_word_len += len(r[0])
        if r[1] == "NN" or r[1] == "NNS" or r[1] == "NNP" or r[1] == "NNPS":
            noun_count+=1
        elif r[1]=="JJ" or r[1]=="JJS" or r[1]=="JJR":
            adjective_count+=1
        elif r[1]=="RB" or r[1]=="RBR" or r[1]=="RBS":
            adverb_count+=1
        elif r[1] == "VB" or r[1] == "VBD" or r[1] == "VBG" or r[1]=="VBN":
            verb_count+=1
        elif r[1] == "CC" or r[1] == "IN" :
            conjunction_count+=1
        elif r[1] == "TO":
            to_count+=1
    Final.append([noun_count/word_count,adjective_count/word_count,verb_count/word_count,adverb_count/word_count,conjunction_count,total_word_len/word_count,label])
    # Final.append([noun_count,adjective_count,verb_count,adverb_count,conjunction_count,to_count,label])
    print("Read files: ",readfiles)
with open("D:\\ProjectBooksBigData\\ExtractedFeatures_modified.csv","a") as f:
    writefiles+=1
    polo = csv.writer(f)
    polo.writerows(Final)
    print("Write files: ",writefiles)
#help taken from https://stackoverflow.com/questions/7588934/how-to-delete-columns-in-a-csv-file
#help taken from https://honingds.com/blog/pandas-read_csv/
#help taken from https://stackoverflow.com/questions/38716643/using-pandas-read-csv-to-read-certain-columns
#help taken from https://www.interviewqs.com/ddi_code_snippets/iterate_rows_pandas