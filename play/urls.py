from django.conf.urls import url


from .views import graph, play_count_by_month

urlpatterns = [
    url(r'^$', graph),
    url(r'^api/play_count_by_month', play_count_by_month, name='play_count_by_month'),
]
