from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import News,Events,Pujas
from rest_framework import permissions
from .serializers import EventsSerializer, NewsSerializer, PujasSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def getNews(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getEvents(request):
    events = Events.objects.all()
    serializer = EventsSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPujas(request):
    pujas = Pujas.objects.all()
    serializer = PujasSerializer(pujas, many=True)
    return Response(serializer.data)