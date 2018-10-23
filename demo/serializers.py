from django.contrib.auth.models import User, Group
from rest_framework import serializers

from demo.models import Home, HomeSections, Articles


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Home
        fields = ('home_name', 'location')

    def update(self, instance, validated_data):
        instance.home_name = validated_data.get('home_name', instance.home_name)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance


class HomeSectionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeSections
        fields = ('home', 'section_name')


class SectionsArticlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = ('section', 'article_name', 'color', 'quantity', 'description')
