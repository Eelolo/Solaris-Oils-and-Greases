from django.contrib import admin
from django.urls import path
from solaris.views import IndexPageView, SitePageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SitePageView.as_view(), name='index_page'),
    path('<page_name>/', SitePageView.as_view(), name='site_page'),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

