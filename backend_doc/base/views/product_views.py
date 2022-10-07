from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# from ..products import products
from django.contrib.auth.models import User
from ..models import Product, Review
from ..serializer import ProductSerializer, UserSerializer , UserSerializersWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.db.models import Q

@api_view(['GET'])
def getProducts(request):
    query = request.query_params.get('keyword')
    # print("query",query)
    # # q= query.ToString()
    # print('q',len(query))
    if query == 'null':
        query = ''

    products = Product.objects.filter(
        Q(name__icontains=query) | Q(specialization__icontains= query)).order_by('-createdAt')
    # products = Product.objects.all()
    serializer = ProductSerializer(products,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getSort(request):
    products = Product.objects.order_by('-numReviews')
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProductReview(request, pk):
    user = request.user
    product = Product.objects.get(id=pk)
    data = request.data

    # 1 - Review already exists
    alreadyExists = product.review_set.filter(user=user).exists()
    if alreadyExists:
        content = {'detail': 'Product already reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 2 - No Rating or 0
    elif data['rating'] == 0:
        content = {'detail': 'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 3 - Create review
    else:
        review = Review.objects.create(
            user=user,
            product=product,
            name=user.first_name,
            rating=data['rating'],
            comment=data['comment'],
        )

        reviews = product.review_set.all()
        product.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        product.rating = total / len(reviews)
        product.save()

        return Response('Review Added')
