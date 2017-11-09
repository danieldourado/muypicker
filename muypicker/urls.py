"""muypicker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include



from estatisticas_facebook.views import PageListView, PageView, PageDetailView, eraseAllPageinsights, eraseAllPages, PageInsightsDetailView, PageInsightsListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^page/insights/erase-all/', eraseAllPageinsights),
    url(r'^page/erase-all/', eraseAllPages),
    url(r'^page/insights/$', PageInsightsListView.as_view()),
    url(r'^page/insights/(?P<slug>[\w-]+)/$', PageInsightsDetailView.as_view()),
    
    url(r'^page/(?P<pk>\w+)/$', PageDetailView.as_view()),
    url(r'^page/$', PageListView.as_view()),
    #url(r'^page/index/(?P<slug>\w+)/$', PageListView.as_view()),
    
]
