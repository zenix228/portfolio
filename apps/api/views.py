from apps.about.models import About
from apps.portfolio.models import Portfolio

from .serializers import AboutSerializer, PortfolioSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

class PortfolioViewSet(ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]