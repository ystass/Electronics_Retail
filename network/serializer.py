from rest_framework.serializers import ModelSerializer


from network.models import Product, Link


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class LinkSerializer(ModelSerializer):

    class Meta:
        model = Link
        fields = "__all__"
