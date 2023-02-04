from rest_framework import filters
from ..models import Athlete_Post
from ..serializers import Athelete_Post_Serializer
from rest_framework import filters, generics


class Search_Athlete_Post(generics.ListAPIView):
    queryset = Athlete_Post.objects.all()
    serializer_class = Athelete_Post_Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content']
