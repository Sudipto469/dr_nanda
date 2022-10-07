from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product,Review
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        # print("model", object)
        fields = ['id','username','email', 'name', 'isAdmin']

    def get_name(self,object):
        name = object.first_name
        if name == '':
            name = object.email
        return name

    def get_isAdmin(self,obj):
        return obj.is_staff

class UserSerializersWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        # print("model" , model)
        fields = ['id','username','email', 'name' , 'isAdmin', 'token']

    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        # ['name','school']

    def get_reviews(self,obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews,many=True)
        return serializer.data

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    # def get_reviews(self,obj):
    #     reviews = obj.review_set.all()
    #     serializer = ReviewSerializer(reviews,many=True)
    #     return serializer.data
