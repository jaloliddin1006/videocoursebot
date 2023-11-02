from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active=models.BooleanField(default=True)
    class Meta:
        abstract = True
        

class BotUsers(BaseModel):
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user_id} | {self.first_name} | {self.last_name}'
    
    class Meta:
        verbose_name_plural = "Bot Users"
        ordering = ["-created_at"]
        
