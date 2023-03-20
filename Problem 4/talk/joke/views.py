from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.db import models
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.

vulgar_words_french = [
    "con",
    "connard",
    "conasse",
    "pute",
    "putain",
    "salope",
    "merde",
    "enculé",
    "enculée",
    "bordel",
    "couille",
    "bite",
    "chier",
    "nique",
]

vulgar_words_english = [
    "fuck",
    "shit",
    "asshole",
    "bitch",
    "cunt",
    "bastard",
    "dick",
    "cock",
    "pussy",
    "slut",
    "whore",
    "fag",
    "faggot",
    "damn",
]


list_jokes = []
black_list = ['']

def censor_vulgar_words(text):
    words = text.split()
    censored_words = []

    for word in words:
        if word.lower() in vulgar_words_french or word.lower() in vulgar_words_english:
            censored_word = '*' * len(word)
        else:
            censored_word = word
        censored_words.append(censored_word)

    censored_text = ' '.join(censored_words)
    return censored_text



class Joke(models.Model):
    i = 1
    def __init__(self, username, content):
        self.id = Joke.i
        self.username = username.capitalize()
        self.content = censor_vulgar_words(content)
        Joke.i = Joke.i + 1



def addView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        story = request.POST.get('story')
        joke = Joke(username, story)
        list_jokes.append(joke)
        return redirect('joke:index')
    return render(request, 'joke/addView.html')


def index(request):
    return render(request,"joke/index.html", {'jokes':list_jokes})

def entry_view(request, id):
    if (id > len(list_jokes)):
        raise Http404("Page not found")
    joke = list_jokes[id-1]
    data = {
        'id': id,
        'username': joke.username,
        'content': joke.content,
    }
    return JsonResponse(data)
