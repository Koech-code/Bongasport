from django.urls import path

from .views import (
    athlete_post_view
)

urlpatterns = [
    path('athelete_post/', athlete_post_view),
]