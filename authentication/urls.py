from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # URL para gerar token
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # URL para dar refresh no token
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # URL para verificar token
]

