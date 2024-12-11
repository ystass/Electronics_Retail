from django.urls import path
from rest_framework.routers import SimpleRouter

from network.apps import NetworkConfig
from network.views import ProductViewSet, LinkListAPIView, LinkCreateAPIView, LinkRetrieveAPIView, \
    LinkUpdateAPIView, LinkDestroyAPIView

app_name = NetworkConfig.name

router = SimpleRouter()
router.register("product", ProductViewSet, basename="product")


urlpatterns = [
    path("link/", LinkListAPIView.as_view(), name="link_list"),
    path("link/create/", LinkCreateAPIView.as_view(), name="link_create"),
    path("link/<int:pk>/", LinkRetrieveAPIView.as_view(), name="link_retrieve"),
    path("link/<int:pk>/update/", LinkUpdateAPIView.as_view(), name="link_update"),
    path("link/<int:pk>/delete/", LinkDestroyAPIView.as_view(), name="link_delete"),
]
urlpatterns += router.urls
