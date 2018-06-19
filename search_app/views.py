from django.shortcuts import render, redirect
import requests
from .models import *
from .forms import *


def home(request):
    s = Search.objects.all()
    search = []
    if 'q' in request.GET:
        q = request.GET['q']
        result = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBANrKh1ceZe5e0-HeqHoFGWJ4wUGXivw4&cx=004553453871434279896:0jr_zktiwb8&client_id=1068010455315-61tqerc4jaalos7ov396c792k3umgihv.apps.googleusercontent.com&q=%s' %q
        print(result)
        response = requests.get(result)
        # print(response)
        search = response.json()
        print(search)

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            s = search
            form.save()
            s.save()

        return redirect('home')

    return render(request, 'search_app/search.html', {'search':search})



    # cx = '004553453871434279896:0jr_zktiwb8';



# from django.shortcuts import render_to_response
# from django.http import Http404, HttpResponse, HttpResponseRedirect

# def home(request):
#     from django.shortcuts import render_to_response
#     from django.http import Http404, HttpResponse, HttpResponseRedirect
#     # from project.application.web_search....
#     from google.searchengine.web_search import google
#
#     def search(request):
#
#         if request.POST:
#             return render_to_response('search.html', {'result': google(request.POST['term'], 10)})
#         # return HttpResponseRedirect("/")
#         else:
#             return render_to_response('search_app/search.html')

