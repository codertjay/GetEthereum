from rest_framework.serializers import ModelSerializer
from .models import PlaceHolder


class PlaceHolderSerializer(ModelSerializer):
    class Meta:
        fields = ['albumId',
                  'id',
                  'title',
                  'url',
                  'thumbnail_url',
                  'timestamp', ]
        model = PlaceHolder
