from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from restaran.models import Contact, FoodMenu, TableOnline, Costumer, Testimonial, Service
from .serializers import MasterChef, ProductType, FoodMenuSerializer, TestimonialSerializer, CostumerSerializer, \
    TableOnlineSerializer, ContactSerializer, ServiceSerializer, MasterChefSerializer, ProductTypeSerializer
from rest_framework import generics, status
from rest_framework import filters


class LandingAPIView(APIView):
    def get(self, request):
        return Response(data={"Landing Page, get request ": "Landing Page"})

    def post(self, request):
        return Response(data={"Landing Page, post request ": "Landing Page"})


# --------------------------------------------------------------------
class MasterChefCreateAPIView(generics.CreateAPIView):
    queryset = MasterChef.objects.all()
    serializer_class = MasterChefSerializer


class MasterChefUpdateAPIView(generics.UpdateAPIView):
    queryset = MasterChef.objects.all()
    serializer_class = MasterChefSerializer


class MasterChefDeleteAPIView(generics.DestroyAPIView):
    queryset = MasterChef.objects.all()
    serializer_class = MasterChefSerializer


# ________________________________________________________________________

# class ContactDetailAPIView(APIView):
#     def get(self, request, id):
#         contact = Contact.objects.get(id=id)
#         try:
#             serializer = ContactSerializer(contact)
#             return Response(data={"Contact": serializer.data})
#         except:
#             return Response(data={"Error": "Contact not found"})
#
#     def put(self, request, id):
#         contact = Contact.objects.all(id=id)
#         serializer = ContactSerializer(instance=contact, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data={"Contact": serializer.data})
#         return Response(data={"Error": serializer.data})
#
#     def delete(self, request, id):
#         contact = Contact.objects.all(id=id)
#         contact.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def patch(self, request, id):
#         contact = Contact.objects.all(id=id)
#         serializer = ContactSerializer(instance=contact, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data={"Contact": serializer.data})
#         return Response(data={"Error": serializer.data})


class ProductTypeSetAPIView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    # permission_classes = (IsAuthenticated)
    # permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('name',)
    # search_fields = ('^name')
    # search_fields = ('=name',)
    search_fields = ('name',)


class FoodMenuSetAPIView(ModelViewSet):
    queryset = FoodMenu.objects.all()
    serializer_class = FoodMenuSerializer
    # permission_classes = (IsAuthenticated)
    # permission_classes = (IsAuthenticated)
    # permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('title',)
    # search_fields = ('^title')
    # search_fields = ('=title',)
    search_fields = ('title', 'description')

    @action(detail=True, methods=['GET'])
    def product_type(self, request, *args, **kwargs):
        food_meny = self.get_object()
        project_type = food_meny.product_type
        serializer = ProductTypeSerializer(project_type)
        return Response(data=serializer.data)

    @action(detail=True, methods=['GET'])
    def title(self, request, *args, **kwargs):
        food_meny = self.get_object()
        serializer = FoodMenuSerializer(food_meny)
        return Response(data=serializer.data)


class TableOnlineSetAPIView(ModelViewSet):
    queryset = TableOnline.objects.all()
    serializer_class = TableOnlineSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')

    @action(detail=True, methods=['GET'])
    def ism(self, request, *args, **kwargs):
        ism = self.get_object()
        serializer = TableOnlineSerializer(ism)
        return Response(data=serializer.data)


class CostumerSetAPIView(ModelViewSet):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('last_name', 'first_name')

    @action(detail=True, methods=['GET'])
    def full_name(self, request, *args, **kwargs):
        full_name = self.get_object()
        serializer = CostumerSerializer(full_name)
        return Response(data=serializer.data)


class TestimonialSetAPIView(ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('costumer', 'description')

    @action(detail=True, methods=['GET'])
    def costumer(self, request, *args, **kwargs):
        testimonial = self.get_object()
        costumer = testimonial.costumer
        serializer = CostumerSerializer(costumer)
        return Response(data=serializer.data)


class ContactSetAPIView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email')


class ServiceSetAPIView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description')
