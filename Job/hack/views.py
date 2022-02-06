from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BaseModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
 

# Create your views here.

#def index(request):
    #return HttpResponse('Hello World')
#    return render(request, 'hack/index.html')

def post_list(request):
    object_list = BaseModel.objects.all()
    paginator = Paginator(object_list, 5) # 5 items in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'hack/list.html',
                  {'page':page, 'posts': posts})


def post_detail(request, id):
     post = get_object_or_404(BaseModel, id=id)
     return render(request,
                   'hack/detail.html',
                   {'post': post})


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = BaseModel.objects.annotate(
            search=SearchVector('title', 'text', 'by'),).filter(search=query)
    return render(request, 'searchp.html', {'form': form, 'query': query, 'results': results})


#def search_result(request):
    # View code here... #set your data here
#    c = {key_data: 'bar'}
#    return render(request, 'search.html', context = c)


