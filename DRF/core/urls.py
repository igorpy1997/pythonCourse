from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blogDRF.views import (
    PostViewSet,
    CommentViewSet,
    CustomObtainToken,
)

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("api-token-auth/", CustomObtainToken.as_view({"post": "create"}), name="api_token_auth"),
    path("", include(router.urls)),
]
