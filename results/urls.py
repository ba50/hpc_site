from django.conf.urls import url
from . import views

app_name = 'results'

urlpatterns = [
    # /results/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /results/<setup_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
