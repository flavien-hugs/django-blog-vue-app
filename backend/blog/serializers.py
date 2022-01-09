# blog.serializers.py

from rest_framework import serializers

from blog.models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name', 'image',
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'category', 'name', 'subtitle',
            'body', 'image', 'status', 'published'
        )
