from rest_framework.serializers import *
from apps.about.models import About
from apps.portfolio.models import Portfolio

class AboutSerializer(ModelSerializer):
    class Meta:

        model = About
        fields = '__all__'

class PortfolioSerializer(ModelSerializer):
    class Meta:

        model = Portfolio
        fields = '__all__'