from __future__ import print_function
import argparse
import os
import re

def build_corpus(text):
    sents = text.split('\n')
    print (sents[0:10])


def main():
    fIn = open('./job_cleaned.txt', 'r')
    text = fIn.read()
    build_corpus(text)

if __name__=='__main__':
    main()