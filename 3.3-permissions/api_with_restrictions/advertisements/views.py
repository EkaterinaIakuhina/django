from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwner
from django_filters.rest_framework import DjangoFilterBackend

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.request.user and self.request.user.is_staff:
            return [IsAdminUser()]

        elif self.action in ['destroy', 'update', 'partial_update']:
            return [IsOwner(), IsAuthenticated()]

        elif self.action in ['create']:
            return [IsAuthenticated()]

        return []