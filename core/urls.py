from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings
from django.conf.urls.static import static

from api import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('api/', include('api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile_view, name='profile'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])