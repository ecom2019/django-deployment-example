from django.shortcuts import render
from django.db.models import F, Count
from django.db.models.functions import Length, Upper

from django.views.generic import ListView , DetailView, TemplateView



#from .models import Product
from product.models import Product
# Create your views here.



class ProductView(ListView):
    model = Product
    template_name= 'product/home.html'
    #paginate_by=1

class ProductList(ListView):
    model = Product
    template_name= 'product/product_list.html'
    #  paginate_by=1

class ProductDetail(DetailView):
    model = Product
    template_name= 'product/product_detail.html'

class ProductCategoryView(ListView):

    model = Product

    def get_queryset(self):
        self.category = self.kwargs['category']
        return Product.objects.filter(category = self.category)

    def get_context_data(self , **kwargs):
        context = super(ProductCategoryView , self).get_context_data(**kwargs)
        context['product_category'] = self.category
        return context 


class ProductLanguageView(ListView):
    model = Product

    def get_queryset(self):
        self.lanuage= self.kwargs['lang']
        return Product.objects.filter(language=self.lanuage)

    def get_context_data(self , **kwargs):
        context = super(ProductLanguageView , self).get_context_data(**kwargs)
        context['product_language'] = self.lanuage
        return context 

class ProductSearchView(ListView):
    model = Product
    template_name= 'test.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Product.objects.filter(title__icontains=query)
            print(query)
            print('xyz q' )
            print(object_list)
            print('xyz obj')
        else:
            object_list = Product.objects.none()
            print('no-query')
            print(query)
            print(object_list)
            print('no-obj query')
        return object_list
