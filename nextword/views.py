from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.conf import settings

import nltk
import json

common_words = [
    'the', 'be', 'to', 'of', 'me'
    'and', 'a', 'in', 'that',
    'have', 'i', 'it', 'for',
    'not', 'on', 'with', 'he',
    'she', 'as', 'you', 'do',
    'with', 'this', 'but', 'his',
    'by', 'from', 'they', 'we',
    'say', 'she', 'or', 'an',
    'will', 'my', 'one', 'all',
    'there', 'their', 'what', 'so',
    'up', 'out', 'if', 'about',
    'who', 'get', 'which', 'go'
]

def landing(request):
    return render(request, 'index.html')

# words = nltk.corpus.gutenberg.words()

# ngrams = [nltk.ngrams(words, num_tokens) for num_tokens in range(3)]
# ngrams_list = [nltk.ngrams(words, num_tokens) for num_tokens in range(1, 4)]


def rank(data):
    result = []
    for entry in set(data):
        result.append((entry, data.count(entry)))
    result.sort(key = lambda x: -x[1])
    return filter(lambda x: x[1] > 1, result)


def matches(ngram, pattern_tokens, should_ignore):
    for i in range(len(pattern_tokens)):
        token = pattern_tokens[i]
        if (token == '*' and (not should_ignore or ngram[i] not in common_words)) or token == ngram[i]:
        # if token == '*' or token == ngram[i]:
            continue
        return False
    return True

def find(request):
    pattern = request.GET.get('pattern')
    should_ignore = request.GET.get('ignore')

    tokens = nltk.word_tokenize(pattern)
    num_tokens = len(tokens)
    ngrams = settings.NGRAMS_LIST[num_tokens - 2]
    return_val = rank([ngram for ngram in ngrams if matches(ngram, tokens, should_ignore)])
    return HttpResponse(json.dumps(return_val), content_type='application/json')
    return HttpResponse(json.dumps(tokens), content_type='application/json')
