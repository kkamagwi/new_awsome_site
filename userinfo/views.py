from django.shortcuts import render, redirect
from .forms import UserContactsForm

def new_user(request):
    if request.method == "POST":
        form = UserContactsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('news')
    else:
        form = UserContactsForm()
    return render(request, 'userinfo/index.html', {'form': form})
