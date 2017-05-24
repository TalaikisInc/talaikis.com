from random import choice, shuffle
from functools import lru_cache

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from redir.models import Quotes, QuoteAuthor, QuoteCat

#TODO quick fix, server doesn't support Python 3!!!!!

class QuotesSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False)
    cat = serializers.StringRelatedField(many=False)

    class Meta:
        model = Quotes
        fields = ('quote', 'author', 'cat')


@lru_cache(maxsize=32)
def randomquote_ids():
    random_ids = Quotes.objects.all().values_list('id', flat=True).order_by('id')
    return random_ids


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
@lru_cache(maxsize=128)
def quote_list(request):
    if request.method == 'GET':
        try:
            quotes = Quotes.objects.all()
            pool= list(quotes)
            shuffle(pool)
            serializer = QuotesSerializer(pool[:100], many=True)
            return JSONResponse(serializer.data)
        except:
            return HttpResponse(status=404)


@csrf_exempt
def random_quote(request):
    try:
        how_much_quotes = 1
        random_ids = randomquote_ids()
        random_id = choice(random_ids)
        quote = Quotes.objects.get(pk=random_id)

        if request.method == 'GET':
            serializer = QuotesSerializer(quote)
            return JSONResponse(serializer.data)
    except Quotes.DoesNotExist:
        return HttpResponse(status=404)


@csrf_exempt
def quote(request, pk):
    try:
        quote = Quotes.objects.get(pk=pk)

        if request.method == 'GET':
            serializer = QuotesSerializer(quote)
            return JSONResponse(serializer.data)
    except Quotes.DoesNotExist:
        return HttpResponse(status=404)
