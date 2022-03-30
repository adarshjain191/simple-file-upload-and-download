
from django.contrib import admin
from django.urls import path,include
from . import views
# newly added
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',views.index,name="index"),
    path('index1',views.index1,name="index1"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
