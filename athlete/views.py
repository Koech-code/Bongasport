from django.shortcuts import render
from .serializers import Athelete_Post_Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['POST'])
# @parser_classes([MultiPartParser])
def athlete_post_view(request, *args, **kwags):
    '''
    Upload a video for other users to see and comment on.
    '''
    serializeposts = Athelete_Post_Serializer(data=request.data)

    if serializeposts.is_valid():
        serializeposts.save()
        return Response(serializeposts.data,
                        status=status.HTTP_201_CREATED)
    else:
        return Response(serializeposts.errors,
                        status=status.HTTP_400_BAD_REQUEST)
