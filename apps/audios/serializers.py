from rest_framework import serializers

from apps.audios.models import Audio, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class AudioSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Audio
        fields = ('id', 'name', 'category', 'audio_file', 'picture')


class AudioDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = ('id', 'name', 'category', 'audio_file', 'picture',)