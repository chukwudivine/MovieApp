from django.shortcuts import render
from .models import News
from django.shortcuts import get_object_or_404


def news(request):
    searchTerm = request.GET.get('searchNews')
    if searchTerm:
        newss = News.objects.filter(headline__icontains=searchTerm)
    else:
        newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss': newss})


def ndetail(request, news_id):
    nnews = get_object_or_404(News, pk=news_id)
    return render(request, 'ndetail.html', {'news': nnews})


