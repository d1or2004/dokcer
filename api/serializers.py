from rest_framework import serializers
from rest_framework.authtoken.models import Token

from restaran.models import MasterChef, ProductType, FoodMenu, TableOnline, Costumer, Testimonial, Contact, Service


class MasterChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterChef
        # fields = '__all__'
        fields = ('id', 'last_name', 'first_name', 'experience')


class ProductTypeSerializer(serializers.ModelSerializer):
    # product_type = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = ProductType
        fields = ('id', 'name')


class FoodMenuSerializer(serializers.ModelSerializer):
    # food_menu = ProductTypeSerializer(many=True)

    class Meta:
        model = FoodMenu
        fields = '__all__'
        # fields = ('id', 'title', 'description', 'price', 'product_type')


class TableOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOnline
        fields = ('id', 'ism', 'email')


class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = ('id', 'last_name', 'first_name')


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ('id', 'description', 'costumer')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'subject', 'message')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'title', 'description')
