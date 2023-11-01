from django.shortcuts import render
from rest_framework import generics, filters
from .models import Category, CourseSource, BotUsers, Feedback
from .serializers import BotGetCategoryListSerializer, BotGetSourceListSerializer, BotUserSerializer, BotFeedbackSerializer
from rest_framework.viewsets import ModelViewSet
from django.core.paginator import Paginator
# Create your views here.
from rest_framework.pagination import PageNumberPagination

class PageResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10

class BotGetCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = BotGetCategoryListSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = PageResultsSetPagination
    search_fields = ['name']
    def get_queryset(self):
        if self.kwargs:
            queryset = self.queryset.filter(parent__name=self.kwargs['category'])
        else:
            queryset = self.queryset.filter(parent=None)
            
        return queryset
    
class BotGetSourceListView(generics.ListAPIView):
    pagination_class = None
    queryset = CourseSource.objects.all()
    serializer_class = BotGetSourceListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    def get_queryset(self):
        if self.kwargs:
            queryset = self.queryset.filter(category__name=self.kwargs['category'])
        else:
            queryset = self.queryset.all()
        return queryset


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
    
           
class FeedbackViewset(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Feedback.objects.all()
    serializer_class = BotFeedbackSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']