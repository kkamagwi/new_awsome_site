from django.shortcuts import get_object_or_404, render, redirect
from .models import News
from .forms import NewsForm


def news(request):
    news = News.objects.all()
    return render(request, 'news/news.html', {'news': news})

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
