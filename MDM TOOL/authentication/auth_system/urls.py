from django.urls import path,include
from .views import HomePage, Register, Login, test, logoutuser
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home/', HomePage, name="home-Page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
    path('logout/', logoutuser, name='logout'),
    path('test/', test, name='test'),
    path('NIBIN456/', views.nibin456_view, name='nibin456'),
    path('catalogue/', views.catalogue_view, name='catalogue'),
    path('source/', views.source_view, name='source'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)