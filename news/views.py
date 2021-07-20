from django.shortcuts import get_object_or_404, render, redirect
from .models import News, Tag
from .forms import NewsForm


def news(request):
    news = News.objects.all()
    tags = Tag.objects.all()
    return render(request, 'news/news.html', {'news': news, 'tag': tags})

def news_detail(request, pk):
    news_detail = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', 
                {'news_detail': news_detail})

def news_new(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news/news_edit.html', {'form': form})


def tag_detail_view(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    news_by_tag = tag.news_set.all()
    return render(request, 'news/news_by_tag.html', 
    {'news_by_tag': news_by_tag})
