from rest_framework import serializers
from .models import Athlete_Post

class Athelete_Post_Serializer(serializers.ModelSerializer):
    # image = Base64ImageField(
    #     max_length=None, use_url=True,
    # )

    class Meta:
        model = Athlete_Post
        fields = [
            'image',
            'video',
            'content',
            ]