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
        

class Feedback(BaseModel):
    user = models.ForeignKey(BotUsers, on_delete=models.CASCADE, null=True, blank=True)
    feedback = models.TextField()
    def __str__(self):
        return f'{self.id} | {self.feedback}'
    
    class Meta:
        verbose_name_plural = "Feedbacks"
        ordering = ["-created_at"]
    
        
class Category(MPTTModel, BaseModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
   
    def __str__(self):
        return f'{self.id}. {self.parent} |  {self.name}' if self.parent else f'{self.id}. {self.name}'
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["-created_at"]
        
    class MPTTMeta:
        order_insertion_by = ["name"]
        
        
class CourseSource(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="category", verbose_name="Kategoriya", limit_choices_to={'parent__isnull': False})
    name = models.CharField(max_length=255)
    source = models.CharField(max_length=355)
    def __str__(self):
        return f'{self.id} | {self.name}'
    
    class Meta:
        verbose_name_plural = "Course Sources"
        ordering = ["-created_at"]
    
    def save(self, *args, **kwargs):
        if not self.name: 
            self.name = self.source.split('/')[-1]
        super().save(*args, **kwargs)
        