setwd("D:\\ProjectBooksBigData\\Books_L_Frank\\")
file <- readLines("21342-0.txt")
file <- paste(file, collapse = " ")
library(NLP)
library(openNLP)
library(RWeka)

library(RWeka)
library(magrittr)
file <- as.String(file)

word_ann <- Maxent_Word_Token_Annotator()
sent_ann <- Maxent_Sent_Token_Annotator()
POS <- Maxent_POS_Tag_Annotator()
file_annotations <- annotate(file, list(sent_ann, word_ann, POS))

#class(file_annotations)

#head(file_annotations)

file_doc <- AnnotatedPlainTextDocument(file, file_annotations)

tags <- tagged_words(file_doc)

write.csv(tags, "D:\\ProjectBooksBigData\\1.csv")

newFile <- read.csv("1.csv")

newFile <- distinct(newFile, token, .keep_all = TRUE)
write.csv(newFile, "D:\\ProjectBooksBigData\\2.csv")
