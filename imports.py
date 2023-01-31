from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from collections import OrderedDict

import nltk
import nltk.corpus
import re
import random
import string
import csv
import io
import numpy as np
import pandas as pd
import requests
import json
import pprint

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger') 

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

