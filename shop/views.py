from django.shortcuts import render
from shop.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'index.html', {'products':products})

def search_results(request):
    if 'product' in request.GET and request.GET['product']:
        search_term = request.GET.get('product')
        searched_products = Product.search_by_product(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 
                                                'products':searched_products})
    else:
        message = 'You have not searched for any product'
        return render(request, 'search.html', {'message':message})