from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active=models.BooleanField(default=True)
    class Meta:
        abstract = True
        

class PromoCode(BaseModel):
    user = models.CharField(max_length=255, null=True, blank=True)
    promo_code = models.CharField(max_length=255, unique=True)
    discount = models.IntegerField()
    
    def __str__(self):
        return f'{self.promo_code} | {self.discount}'
    
    class Meta:
        verbose_name_plural = "Promo Codes"
        ordering = ["-created_at"]
      
class BotUsers(BaseModel):
    telegram_id = models.IntegerField(unique=True)
    telegram_full_name = models.CharField(max_length=255, null=True, blank=True)
    telegram_username = models.CharField(max_length=255, null=True, blank=True)
    telegram_phone_number = models.CharField(max_length=20, null=True, blank=True)
    promo_code = models.ForeignKey(PromoCode, on_delete=models.CASCADE, null=True, blank=True, to_field="promo_code")
    
    def __str__(self):
        return f'{self.telegram_id} | {self.telegram_full_name}'
    
    class Meta:
        verbose_name_plural = "Bot Users"
        ordering = ["-created_at"]
        
          
class Order(BaseModel):
    check_id = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(BotUsers, on_delete=models.CASCADE, to_field="telegram_id", related_name="user_orders")
    promo_code = models.CharField(max_length=35, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    total_price = models.IntegerField()
    total_price_with_discount = models.IntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user} | {self.total_price_with_discount}'
    
    class Meta:
        verbose_name_plural = "Orders"
        ordering = ["-created_at"]
        
    def save(self, *args, **kwargs):
        if self.promo_code:
            discount = PromoCode.objects.get(promo_code=self.promo_code).discount
            self.discount = discount
            self.total_price_with_discount = self.total_price - discount
            
        else:
            self.total_price_with_discount = self.total_price
        super(Order, self).save(*args, **kwargs)
    
    def telegram_id(self):
        return self.user.telegram_id