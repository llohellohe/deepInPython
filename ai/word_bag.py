corpus = ["我特别特别喜欢看电影",
          "这部电影真的是很好看的电影",
          "今天天气真好是难得的好天气",
          "我今天去看了一部电影",
          "电影院的电影都很好看"]
import jieba

# 使用jieba分词进行分词
corpus_tokenized = [list(jieba.cut(sentence)) for sentence in corpus]
print(corpus_tokenized)

word_dict = {}

# 创建词汇表
for sentence in corpus_tokenized:
    for word in sentence:
        if word not in word_dict:
            word_dict[word] = len(word_dict)
print("词汇表", word_dict)

"""
转化为词袋表示,
即按照上面的词汇表,
构建每个词出现的次数。

特别注意：
词袋模型和ngram模型的不同之处就在于：
词袋模型忽略了词出现的顺序，只关注出现的次数

"""
bow_vectors = []

for sentence in corpus_tokenized:
    sentence_vector = [0] * len(word_dict)
    print("vector", sentence_vector)
    for word in sentence:
        sentence_vector[word_dict[word]] += 1
    bow_vectors.append(sentence_vector)
print("词袋表示：", bow_vectors)

"""
通过两个向量的余弦相似度来查看相似性。
越接近1表示越相似，越接近-1表示越不相似，当接近0时，说明没有明显的相似性。
"""

import numpy as np


def cosine_similarity(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    norm_a = np.linalg.norm(vector1)
    norm_b = np.linalg.norm(vector2)
    return dot_product / (norm_a * norm_b)


similarity_matrix = np.zeros((len(corpus), len(corpus)))

for i in range(len(corpus)):
    for j in range(len(corpus)):
        similarity_matrix[i][j] = cosine_similarity(bow_vectors[i], bow_vectors[j])
