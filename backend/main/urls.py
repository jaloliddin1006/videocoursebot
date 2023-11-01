from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'botuser', views.BotUserViewset)
router.register(r'feedback', views.FeedbackViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', views.BotGetCategoryListView.as_view()),
    path('category/<str:category>/', views.BotGetCategoryListView.as_view()),
    path('source/', views.BotGetSourceListView.as_view()),
    path('source/<str:category>/', views.BotGetSourceListView.as_view()), 
]