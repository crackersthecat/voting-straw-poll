from django.conf.urls import patterns, url

from vote import views

urlpatterns = patterns(
    '',
    # eg: /vote/
    url(r'^$', views.index, name='index'),
    # eg: /vote/process/
    url(r'^process/$', views.process_response, name='process_response'),
    # eg: /vote/results/
    url(r'^results/$', views.results_all, name='results_all'),
    # eg: /votes/results/constituency
    url(r'^results/constituency/$', views.select_constituency, name='select_constituency'),
    # eg: /votes/results/constituency/process
    url(r'^results/constituency/process/$', views.constituency_chosen, name='constituency_chosen'),
    # eg: /vote/resutls/constituency/6
    url(r'^results/constituency/(?P<constituency_id>\d+)/$', views.results_by_constituency, name='results_by_constituency'),
)
