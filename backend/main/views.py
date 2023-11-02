from django.shortcuts import render
from rest_framework import generics, filters
from .models import BotUsers
from .serializers import BotUserSerializer
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator
# Create your views here.
from rest_framework.pagination import PageNumberPagination

class PageResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10



class BotUserViewset(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    # def get_queryset(self):
    #     if self.kwargs:
    #         queryset = self.queryset.filter(user_id=self.kwargs['user_id'])
    #     return queryset
    
           
