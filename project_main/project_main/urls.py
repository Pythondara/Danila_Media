from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('login_page/', include('login_page.urls')),
    path('audio_page/', include('audio_page.urls')),
    path('video_page/', include('video_page.urls')),
    path('image_page/', include('image_page.urls')),
    path('history_page/', include('history_page.urls')),
    path('profile_page/', include('profile_page.urls')),


]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
