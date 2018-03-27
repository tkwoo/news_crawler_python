import numpy as np
from konlpy.tag import Kkma, Twitter
import gensim
from gensim.models import Word2Vec
from functools import reduce
import time

kkma = Kkma()

fin = open('./job_test_cleaned.txt', 'r')
sents = fin.read().split('\n')

print (sents[:2])

model = Word2Vec.load('./ko.bin')

unknown_vec = np.zeros((200,), dtype=np.float32)

start = time.time()
list_wvs = []
list_words = []
for sent in sents:
    words = [word for word, _ in kkma.pos(sent)]
    wv = [model[word] if word in model.wv.vocab else unknown_vec for word in words]
    list_wvs.append(wv)
    list_words.append(words)
end = time.time()

processing_time = end - start
print ('%.3f s'%processing_time)

print (len(list_wvs))

flat_list = reduce(lambda x,y: x+y, list_words)
print (flat_list)
print (len(flat_list))
print (len(list_words))
