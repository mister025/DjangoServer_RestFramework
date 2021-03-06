from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (TasklistCreateView,
                    TasklistDetailsView,
                    TaskCreateView,
                    TaskDetailsView,
                    TagCreateView,
                    TagDetailsView,
                    UserCreateView,
                    #UserLoginView,
                    UserDetail,
                    UserList)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    url(r'^todolists/$', TasklistCreateView.as_view(), name="lists"),
    url(r'^todolists/(?P<pk>[0-9]+)/$', TasklistDetailsView.as_view(), name="list-detail"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/$', TaskCreateView.as_view(), name="tasks"),
    url(r'^todolists/(?P<list_id>[0-9]+)/tasks/(?P<pk>[0-9]+)/$', TaskDetailsView.as_view(), name="task-detail"),
    url(r'^tags/$', TagCreateView.as_view(), name="tags"),
    url(r'^tags/(?P<pk>[0-9]+)/$', TagDetailsView.as_view(), name="tag-details"),
    url(r'^register/$', UserCreateView.as_view(), name="register"),
    #url(r'^logiin/$', UserLoginView.as_view(), name="login"),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^newauth/$', obtain_auth_token),
]


urlpatterns = format_suffix_patterns(urlpatterns)
