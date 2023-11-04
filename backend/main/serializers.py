from rest_framework import serializers
from .models import BotUsers, PromoCode, Order

class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = '__all__'
        
        
        
class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = ("user", "promo_code", "discount")
        
        
        
class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("user", "full_name", "phone_number", "email", "total_price", "is_paid")
        
# class OrderUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ("id", "phone_number", "promo_code", "is_paid")
        

# class OrderUserSerializer(serializers.ModelSerializer):
#     user_orders = OrderUpdateSerializer(many=True)
#     class Meta:
#         model = BotUsers
#         fields = ("telegram_id", "full_name", "user_orders")
        
    
    # def update(self, instance, validated_data):
    #     orders_data = validated_data.pop('user_orders')
    #     orders = (instance.user_orders).all()
    #     orders = list(orders)
    #     instance.telegram_id = validated_data.get('telegram_id', instance.telegram_id)
    #     instance.full_name = validated_data.get('full_name', instance.full_name)
    #     instance.save()
        
    #     for order_data in orders_data:
    #         order = orders.pop(0)
    #         order.phone_number = order_data.get('phone_number', order.phone_number)
    #         order.promo_code = order_data.get('promo_code', order.promo_code)
    #         order.is_paid = order_data.get('is_paid', order.is_paid)
    #         order.save()
    #     return instance