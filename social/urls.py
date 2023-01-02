from django.urls import include, path
from rest_framework.routers import DefaultRouter

from social.views import LikeDetail, PostViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),
    path("likes/<int:pk>/", LikeDetail.as_view()),
]
