from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Tag
from .forms import ProductForm, TagForm

def products(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def products_detail(request, pk):
    products_detail = get_object_or_404(Product, pk=pk)
    return render(request, 'products/products_detail.html', 
                {'products_detail': products_detail})


def new_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.save()
            return redirect('products_detail', pk=news.pk)
    else:
        form = ProductForm()
    return render(request, 'products/products_edit.html', {'form': form})


def new_tag(request):
    if request.method == "POST":
        tag_form  = TagForm(request.POST)
        if tag_form.is_valid():
            tags = tag_form.save(commit=False)
            tags.save()
            return redirect('new_product')
    else:
        tag_form = TagForm()
    return render(request, 'products/tag_edit.html', {'tag_form': tag_form})
