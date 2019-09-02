from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from history import views
from history_website import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('history.urls'))
]
# for development
if settings.DEBUG:
    urlpatterns += [
        url(r"^add/$", views.add)
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)