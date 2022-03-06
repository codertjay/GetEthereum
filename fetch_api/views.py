from rest_framework.generics import ListCreateAPIView
from rest_framework.serializers import ModelSerializer
from .models import EthereumAccounts


class GetEthereumSerializer(ModelSerializer):
    class Meta:
        model = EthereumAccounts
        fields = '__all__'


class CreateRetrieveAPIView(ListCreateAPIView):
    serializer_class = GetEthereumSerializer
    queryset = EthereumAccounts.objects.all()
