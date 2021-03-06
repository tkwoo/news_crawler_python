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
    fout = open('corpus.txt', 'w')
    for sent in sents:
        if sent is not None:
            if len(sent) == 0:
                continue
            words = segment_word(sent)
            if words[-1] == 'com':
                continue
            elif len(words) < 2:
                continue
            if words[0] == 'titlestart':
                words = words[1:-2]
            fout.write(" ".join(words) + "\n")
            # elif len(words) > 50:
            #     print (words)
    fout.close()

def main():
    fIn = open('./job_1500_cleaned.txt', 'r')
    text = fIn.read()
    build_corpus(text)

if __name__=='__main__':
    main()