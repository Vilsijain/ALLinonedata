import os
import random
import nltk
import gensim

def load_model():
    model = gensim.models.KeyedVectors.load_word2vec_format(os.getenv('DOWNLOAD_FILE_NAME'), binary=False)
    return model 
                 
def generate_tlds(word):
    result=[]
    str2 = ['.com', '.in', '.co', '.net', '.org', '.co', '.info', '.me', '.website', '.tech','.host', '.cricket']
    for i in random.sample(str2,12):
        strres=word+i
        result.append(strres)
    return list(result)

 
def generate_prepended_strings(word):
    model = load_model()
    result = model.most_similar(positive=word, topn = 20)
    result = [item[0] for item in result]
    response  = []
    for i in random.sample(result,20):
        response.append(word+i)
    return response

 
def generate_appended_strings(word):
    model = load_model()
    result = model.most_similar(positive=word, topn = 20)
    result = [item[0] for item in result]
    response  = []
    for i in random.sample(result,20):
        response.append(i+word)
    return response



def merge_words(word1,word2):
    model = load_model()
    result1 = model.most_similar(positive=word1, topn = 3)
    result2 = model.most_similar(positive=word2, topn = 3)
    result1 = [item[0] for item in result1]
    result2 = [item[0] for item in result2]
    response = []
    for i in random.sample(result1,3):
        for j in random.sample(result2,3):
            response.append(i+j)
    return response

def generate_top_10(word):
    model = load_model()
    result = model.most_similar(positive=[word], topn = 10)
    return result
