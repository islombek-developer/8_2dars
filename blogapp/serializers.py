from rest_framework import serializers
from .models import News
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'name', 'year', 'content']



class Cars:
    def __init__(self, name, year, content):
        self.name = name
        self.year = year
        self.content = content


new_car1 = Cars(name='Nexia2', year=2015, content='O‘zbekistonning “xalq mashinasi”ga aylangan Daewoo Nexia modelining uzoq davom etgan tarixi 2016 yilda yakunlandi.')

class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    year = serializers.IntegerField()
    content = serializers.CharField()


def serialization():
    print(new_car1)
    serializer = CarSerializer(new_car1)
    print(serializer.data)
    json = JSONRenderer().render(serializer.data)
    print(json)


def deserialization():
    json = b'{"name":"Nexia2","year":2015,"content":"O\xe2\x80\x98zbekistonning \xe2\x80\x9cxalq mashinasi\xe2\x80\x9dga aylangan Daewoo Nexia modelining uzoq davom etgan"}'
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)