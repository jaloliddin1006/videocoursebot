from rest_framework import generics, filters
from .models import BotUsers, PromoCode, Order
from .serializers import BotUserSerializer, PromoCodeSerializer, OrderCreateSerializer
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

# Create your views here.


class BotUserViewset(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = BotUsers.objects.all()
    serializer_class = BotUserSerializer
    filter_backends = [filters.SearchFilter]
    lookup_field = 'telegram_id'
    search_fields = ['name']
    
    # def get_queryset(self):
    #     if self.kwargs:
    #         queryset = self.queryset.filter(user_id=self.kwargs['user_id'])
    #     return queryset
    
        

class GetPromoCodesView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = PromoCode.objects.filter(is_active=True)
    serializer_class = PromoCodeSerializer
    lookup_field = 'promo_code'

    def get_object(self):
        promo_code = self.kwargs.get(self.lookup_field)
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, promo_code=promo_code)
        return obj

    def get_queryset(self):
        promo_code = self.kwargs.get(self.lookup_field)
        if promo_code:
            return self.queryset.filter(promo_code=promo_code)
        else:
            raise NotFound("Promo code is required")



class OrderCreateView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        return Response({
            "order": OrderCreateSerializer(order, context=self.get_serializer_context()).data,
        })

# class OrderValuesUpdate(generics.RetrieveUpdateAPIView):
#     authentication_classes = []
#     permission_classes = []
#     queryset = Order.objects.all()
#     serializer_class = OrderUpdateSerializer

    
#     def patch(self, request, *args, **kwargs):
#         telegram_id = self.kwargs.get("telegram_id")
#         pk = self.kwargs.get('pk')
#         obj = get_object_or_404(BotUsers, telegram_id=telegram_id)
#         orders = obj.user_orders.all()
#         order = get_object_or_404(orders, pk=pk)
#         serializer = OrderUpdateSerializer(order, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"status": True, "message": "Order updated successfully"}, status=200)
        
