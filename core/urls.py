from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from home import views

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('logout/', views.logout, name='logged_out_user'),
    path('reset_request/', views.reset_request, name='password_reset'),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
