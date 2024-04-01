from django.urls import path
from catalog.views import CategoryListView, CategoryProductsView, SellerListView, SellerProductsView, DiscountProductsView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:category_id>/', CategoryProductsView.as_view(), name='category-products'),
    path('sellers/', SellerListView.as_view(), name='sellers'),
    path('sellers/<int:seller_id>/', SellerProductsView.as_view(), name='seller-products'),
    path('discount/<int:discount_id>/', DiscountProductsView.as_view(), name='discount-products'),
]
