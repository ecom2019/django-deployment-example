from django.urls import path
from .views import ProductList , ProductDetail, ProductView, ProductLanguageView, ProductCategoryView, ProductSearchView 

app_name='product'

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    #path('product', ProductView.as_view(), name='home'),
    #path('product_list', ProductList.as_view(), name='product_list'),
    #path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('product_detail/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('language/<str:lang>', ProductLanguageView.as_view(), name='product_language'),
    path('category/<str:category>', ProductCategoryView.as_view(), name='product_category'),
    path('search/>', ProductSearchView.as_view(), name='product_search'),
    #path('category/<int:pk>', ProductCategoryView.as_view(), name='product_category'),

]