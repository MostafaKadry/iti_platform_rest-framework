from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainees/', include('trainee.urls')),
    path('track/', include('track.urls')),
    path('course/', include('course.urls')),

      # session-based auth for DRF browsable API login/logout
    path('api-auth/', include('rest_framework.urls')),

      # token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
] +static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
