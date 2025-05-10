from collections import Counter, defaultdict


def tokenize(text):
    """
    将字符串token化，返回每个字符
    :param text:
    :return:
    """
    return [char for char in text]


def count_ngrams(corpus, n):
    """
    检查预料中，每个句子中，以N元组为分割，各个字符的出现次数
    其中key为(字,)，value为Counter{'A':次数，'B'：次数}
    :param corpus:
    :param n:
    :return:
    """
    ngrams_count = defaultdict(Counter)
    for text in corpus:
        tokens = tokenize(text)
        for i in range(len(tokens) - n + 1):
            ngram = tuple(tokens[i:i + n])
            print(ngram)
            prefix = ngram[:-1]
            token = ngram[-1]
            ngrams_count[prefix][token] += 1
    return ngrams_count


def ngram_probabilities(ngrams_count):
    """
    计算每个ngram中词的出现概率
    :param ngrams_count:
    :return:
    """
    ngram_probs = defaultdict(Counter)
    for prefix, counts in ngrams_count.items():
        total_count = sum(counts.values())
        for token, count in counts.items():
            ngram_probs[prefix][token] = count / total_count
    return ngram_probs


def generate_next_token(prefix, ngram_probs):
    """
    按照概率，使用max函数，返回可能性最大的key
    :param prefix:
    :param ngram_probs:
    :return:
    """
    if not prefix in ngram_probs:
        return None
    next_token_probs = ngram_probs[prefix]
    next_token = max(next_token_probs, key=next_token_probs.get)
    return next_token


def generate_text(prefix, ngrams_prob, n, length=6):
    """
    按照 ngrams_prob来循环生成词
    :param prefix: 第一个词
    :param ngrams_prob: 训练过的概率表
    :param n:
    :param length: 生成的长度
    :return:
    """
    tokens = list(prefix)
    print("token list is {}".format(tokens))
    print("length is {}".format({length - len(prefix)}))
    for _ in range(length - len(prefix)):
        next_token = generate_next_token(tuple(tokens[-(n - 1):]), ngrams_prob)
        print(tuple(tokens[-(n - 1):]))
        if not next_token:
            break
        tokens.append(next_token)
    return ''.join(tokens)


corpus = ["我喜欢吃苹果",
          "我喜欢吃香蕉",
          "她喜欢吃葡萄",
          "他不喜欢吃香蕉",
          "他喜欢吃苹果",
          "她喜欢吃草莓"]

ngrams_count = count_ngrams(corpus, 2)

for prefix, count in ngrams_count.items():
    print(f"prefix of {''.join(prefix)}: counter is {dict(count)}")

ngram_probs = ngram_probabilities(ngrams_count)
print("bigram 出现的概率如下：")
for prefix, count in ngram_probs.items():
    print("{} {} {}".format("".join(prefix), dict(count), generate_next_token(prefix, ngram_probs)))

generated_text = generate_text("我", ngram_probs, 2)

print(generated_text)
