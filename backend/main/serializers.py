from rest_framework import serializers
from .models import Category, CourseSource, BotUsers, Feedback

class BotGetCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', "name")
        

class BotGetSourceListSerializer(serializers.ModelSerializer):
    category = BotGetCategoryListSerializer()
    class Meta:
        model = CourseSource
        fields = ('id', "category", "name", "source")



class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUsers
        fields = '__all__'
        
class BotFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'