from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from subscriber import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('ad/', include('ad.urls')),
    path('subscribe/', views.subscribe),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)