from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import News
from .serializers import CarsSerializer

class NewsApiView(APIView):
    def get(self,request:Request):
        news = News.objects.values()
        return Response(news)
   












# class NewsApiView(ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewSerializers


# class NewsApiDetailView(RetrieveAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewSerializers