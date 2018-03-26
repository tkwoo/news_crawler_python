import numpy as np
from konlpy.tag import Kkma, Twitter
import gensim
from gensim.models import Word2Vec

word1, tag1 = Kkma().pos("사랑")[0]
word2, tag2 = Kkma().pos("미국")[0]
word3, tag3 = Kkma().pos("서울")[0]

print (word1)

sentences = [word1, word2, word3]
# model = gensim.models.Word2Vec(sentences=sentences, size=100, negative=5, window=5)

model = Word2Vec.load('./data/ko1.bin')

# print (model.wv.most_similar_cosmul(positive=['삶', '추억'], negative=['이별']))
test_str = word1 #'좋아'
print ('input word: %s'%test_str)
print ('top 10 most similar words')
print (model.most_similar(positive=[test_str], topn=10), '\n')
print ('input word: 사운드')
print ('top 10 most similar words')
print (model.most_similar(positive=['사운드'], topn=10))
