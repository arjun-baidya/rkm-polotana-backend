from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['title', 'date','time','image','description']

class PujasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pujas
        fields = ['title', 'image','start_date','end_date','description']