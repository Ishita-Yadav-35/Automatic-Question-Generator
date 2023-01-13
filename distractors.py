#wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
#tar -xvf  s2v_reddit_2015_md.tar.gz
#dir s2v_old

from sense2vec import Sense2Vec
import random

s2v = Sense2Vec().from_disk(r"C:\Users\Ishita Yadav\s2v_old")

from collections import OrderedDict
def sense2vec_get_words(word,s2v):
    output = []
    word = word.lower()
    word = word.replace(" ", "_")

    sense = s2v.get_best_sense(word)
    most_similar = s2v.most_similar(sense, n=20)

    # print ("most_similar ",most_similar)

    for each_word in most_similar:
        append_word = each_word[0].split("|")[0].replace("_", " ").lower()
        if append_word.lower() != word:
            output.append(append_word.title())

    out = list(OrderedDict.fromkeys(output))
    return out


word = "4"
distractors = sense2vec_get_words(word,s2v)
distractors.insert(0,word)
options = distractors[:4]
random.shuffle(options)

print (options)