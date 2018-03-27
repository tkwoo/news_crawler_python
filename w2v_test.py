import numpy as np
from konlpy.tag import Kkma, Twitter
import gensim
from gensim.models import Word2Vec

word1, tag1 = Kkma().pos("job")[0]
word2, tag2 = Kkma().pos("현대")[0]
word3, tag3 = Kkma().pos("마이다스아이티")[0]

print (word1)

sentences = [word1, word2, word3]
# model = gensim.models.Word2Vec(sentences=sentences, size=100, negative=5, window=5)

model = Word2Vec.load('./ko.bin')

# print (model.wv.most_similar_cosmul(positive=['일', '삶'], negative=['대기업']))

test_str = word1
print ('input word: %s'%test_str)
print ('top 10 most similar words')
print (model.most_similar(positive=[test_str], topn=10), '\n')

print ('input word: %s'%word2)
print ('top 10 most similar words')
print (model.most_similar(positive=[word2], topn=10))

print ('마이다스아이티' in model.wv.index2word)
print (model.wv.index2word[:10])

# print (model.most_similar(positive=['마이다스'], topn=10), '\n')
print (model.most_similar(positive=['다'], topn=10), '\n')

# print ('마이다스' in model.wv.vocab)

# print (model['마이다스'])