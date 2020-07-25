from django.urls import path
from .import views
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from portfolio import settings

app_name="app"

urlpatterns=[
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('pdf/',views.pdf,name="pdf_view")
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
