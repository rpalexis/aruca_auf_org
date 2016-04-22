import re
from annuaire.models import *
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.db.models import Q
from itertools import chain
from django.http import HttpResponse, HttpResponseRedirect

from annuaire.decorators import chercheur_required #Resolving stay connected for a-propos

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['nom', 'prenom', 'discipline', 'theme_recherche', 'mots_cles', 'etablissement'])
        chercheur = Chercheur.objects.filter(entry_query).order_by('-date_pub')
        entry_query2 = get_query(query_string, ['intitule', 'axe', 'etablissement', 'nom', 'presentation', 'problematique', 'mots_cles',])
        equipe = Equipe.objects.filter(entry_query2).order_by('-date_pub')
        found_entries = chain(chercheur, equipe)
        return render_to_response('hintPages/search.html',
                                  { 'query_string': query_string, 'found_entries': found_entries },
                                  context_instance=RequestContext(request))
    return HttpResponse("<p>Merde</p>")
@chercheur_required
def propos(request):
    return render_to_response('hintPages/propos.html')

@chercheur_required
def help(request):
    return render_to_response('hintPages/aide.html')


@chercheur_required
def useful(request):
    return render_to_response('hintPages/liens.html')

@chercheur_required
def acc(request):
    return HttpResponseRedirect('annuaire/')
