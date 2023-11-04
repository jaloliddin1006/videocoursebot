from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from . import models
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class OrderResources(resources.ModelResource):
    
    class Meta:
        model = models.Order
        # fields = "__all__"
        fields = ("check_id", "full_name",  "phone_number", "email", "promo_code", "discount", "total_price", "total_price_with_discount", "is_paid", "created_at")
        export_order = ("check_id", "full_name",  "phone_number", "email", "promo_code", "discount", "total_price", "total_price_with_discount", "is_paid", "created_at")
        
        

@admin.register(models.BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ("id", "telegram_id", "telegram_username", "telegram_full_name", "telegram_phone_number", "promo_code", "created_at")
    search_fields = ("telegram_id", "telegram_phone_number", "promo_code")
    list_filter = ("created_at", "promo_code")

@admin.register(models.PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "promo_code", "discount", "created_at", "is_active")
    search_fields = ("promo_code", "user")
    list_filter = ("created_at",)
    
@admin.register(models.Order)
class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("check_id", "telegram_id", "full_name", "phone_number", "email", "promo_code", "total_price_with_discount", "is_paid", "created_at")
    search_fields = ("full_name", "phone_number")
    list_filter = ( "created_at", "promo_code")
    resource_classes = [OrderResources]
    # actions = None
    # readonly_fields = ( "total_price", "total_price_with_discount", "promo_code", "is_paid", "phone_number", "created_at")
    

    
    