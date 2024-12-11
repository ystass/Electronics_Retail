from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from network.models import Product, Link
from network.serializer import ProductSerializer, LinkSerializer
from users.permissions import IsActiveEmployees


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveEmployees]


class LinkCreateAPIView(CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActiveEmployees]


class LinkListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActiveEmployees]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('country',)


class LinkRetrieveAPIView(RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActiveEmployees]


class LinkUpdateAPIView(UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActiveEmployees]

    def perform_update(self, serializer):
        if "debt" in serializer.validated_data:
            serializer.validated_data.pop("debt")
            raise Exception("Запрещено обновлять поле задолженности")
        super().perform_update(serializer)


class LinkDestroyAPIView(DestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated, IsActiveEmployees]
