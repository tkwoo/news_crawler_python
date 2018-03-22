from __future__ import print_function
import argparse
import os
import re
from konlpy.tag import Kkma

kkma = Kkma()

max_corpus_size = 1000000000

def segment_word(sent):
    words = [word for word, _ in kkma.pos(sent)]
    # words = sent.split(' ')
    return words

def build_corpus(text):
    sents = text.split('\n')
    # print (sents[0:10])
    
    for sent in sents[:10]:
        if sent is not None:
            if len(sent) == 0:
                continue
            words = segment_word(sent)
            print (len(words))



def main():
    fIn = open('./job_cleaned.txt', 'r')
    text = fIn.read()
    build_corpus(text)

if __name__=='__main__':
    main()