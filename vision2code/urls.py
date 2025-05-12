from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'Vision2Code Admin'
admin.site.site_title = 'Vision2Code Admin Portal'
admin.site.index_title = 'Welcome to Vision2Code Admin Portal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ui_recognition.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
