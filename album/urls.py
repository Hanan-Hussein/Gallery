from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    path('',views.landing, name='Welcome'),
    path('category/<category>/',views.filter_category, name='filterCategory'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)