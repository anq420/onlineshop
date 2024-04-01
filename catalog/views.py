from catalog.models import Category, Product, Seller
from rest_framework.generics import ListAPIView
from catalog.serializers import CategorySerializer, ProductSerializer, SellerSerializer, DiscountSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryProductsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, category_id):
        queryset = Product.objects.filter(category__id=category_id)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class SellerListView(ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [AllowAny]


class SellerProductsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, seller_id):
        queryset = Product.objects.filter(seller__id=seller_id)
        serializer = SellerSerializer(queryset, many=True)
        return Response(serializer.data)


class DiscountProductsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, discount_id):
        queryset = Product.objects.filter(discount__id=discount_id)
        serializer = DiscountSerializer(queryset, many=True)
        return Response(serializer.data)
