from film.models import Film
from rest_framework import serializers


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = ("title","description","language","release_year","rental_duration","rental_date","category")



class FilmSerializerNoORM(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

