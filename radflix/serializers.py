from rest_framework import serializers
from radflix.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id',
                  'show_id',
                  'type',
                  'title',
                  'director',
                  'cast',
                  'country',
                  'date_added',
                  'release_year',
                  'rating',
                  'duration',
                  'listed_in',
                  'description')
