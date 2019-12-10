"""location_vehicule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from vehicule import views
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('vehicule/users', views.users, name='users'),
    path('del-user <username>', views.desactivate_user, name='del_path'),
    #path('active-user <username>', views.activate_user, name='active_path'),
    path('edit-user <username>', views.edit_user, name='edit_path'),
    path('vehicule/creatclt', views.creatclt, name='creatclt'),
    path('vehicule/enrvehicule', views.enrvehicule, name='enrvehicule'),
    path('vehicule/listveh', views.listveh, name='listveh'),
    path('vehicule/navgerant', views.navgerant, name='navgerant'),
    path('change-status/<status>/<id>', views.cahnge_status_vh, name='cahnge_status'),
    path('vehicule/', include('vehicule.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
