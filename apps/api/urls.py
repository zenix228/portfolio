from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.portfolio import views

from rest_framework.routers import DefaultRouter
from.views import AboutViewSet, PortfolioViewSet

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('portfolio/', view=views.product_list),
]

router = DefaultRouter()
router.register('about', AboutViewSet, basename='about')
router.register('portfolio', PortfolioViewSet, basename='portfolio')

urlpatterns += router.urls