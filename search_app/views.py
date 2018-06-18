from django.shortcuts import render
import requests


def home(request):
    search = {}
    if 'q' in request.GET:
        q = request.GET['q']
        result = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBANrKh1ceZe5e0-HeqHoFGWJ4wUGXivw4&cx=017576662512468239146:omuauf_lfve&q=%s' %q
        print(result)
        response = requests.get(result)
        print(response)
        search = response.json()
        print(search)

    return render(request, 'search_app/search.html', {'search':search})



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

