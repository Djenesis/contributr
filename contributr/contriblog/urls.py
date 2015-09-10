from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^post/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="detail"),
    ]
