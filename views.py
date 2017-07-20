from pyramid.response import Response
from pyramid.view import view_config
from prova import Prova
import random


@view_config(route_name='quotes:id', renderer='json')
def get_quotes(request):
    quote_id = request.matchdict.get('id', '')
    html = "<li>%s</li>" % Prova.do_request(quote_id)['quote']
    return Response(html)


@view_config(route_name='quotes')
def get_quote(request):
    html = "<ul>"
    for q in Prova.do_request()['quotes']:
        html += "<li>%s</li>" % q
    html += "</ul>"
    return Response(html)


@view_config(route_name='random_quotes', renderer='json')
def get_random_quote():
    all_quotes = Prova.do_request()['quotes']
    return all_quotes[random.randint(0, len(all_quotes) - 1)]


@view_config(route_name='hello')
def hello(request):
    return Response("<h1>Desafio Web 1.0</h1>")
