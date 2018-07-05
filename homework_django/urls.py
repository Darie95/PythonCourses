"""homework_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from HomeworkDjango import views
from homework_django import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.main, name='index'),
    url(r'^select_data/$', views.select_data),
    url(r'^update_data/$', views.update_data),
    url(r'^delete_data/$', views.delete_data),
    url(r'^my_view/$', views.MyView.as_view()),
    url(r'^shops/', include(
        [url('^$', views.shops), url(r'^add/$', views.AddShop.as_view()),
         url(r'^(\d+)/', include(
             [url('^$', views.about_shop, name='about_shop'),
              url(r'add/$', views.NewDep.as_view(), name="add_dep")]))])),
    url(r'^items/(?P<pk>\d+)/',
        include([url(r'^update/$',views.ItemUpdate.as_view(), name='update'),
                 url(r'^delete/$', views.ItemDelete.as_view(), name='delete')])),
    url(r'^templates/$', views.template),
    url(r'^item_create/$', views.ItemCreateView.as_view()),
    url(r'^search/$', views.Search.as_view()),
    url(r'^result/$', views.Search.as_view())]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
