from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'botuser', views.BotUserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('promo/<str:promo_code>/', views.GetPromoCodesView.as_view()),
    path('order/create/', views.OrderCreateView.as_view()),
    # path('order/update/<int:telegram_id>/<int:pk>/', views.OrderValuesUpdate.as_view()),
]