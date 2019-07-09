from django.conf.urls import patterns, include, url


# People patterns.
urlpatterns = patterns('kartoza_project.views',
    url("^category/(?P<category>.*)/$", "project_list", name="project_list_category"),
    url("^detail/(?P<slug>[-\w]+)/$", "project_detail", name="project_detail"),
    url("^$", "project_list", name="project_list"),
)