from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import RedirectView
from agreements.views import AgreementDetailView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/'), name='AgreementIndexView'),
    #url(r'^create/$',  login_required(AgreementCreateView.as_view()), name='AgreementCreateView'),
    #url(r'^(?P<slug>[-_\w]+)/edit/$',  AgreementEditView.as_view(), name='AgreementEditView'),
    url(r'^(?P<slug>[-_\w]+)/$',  AgreementDetailView.as_view(), name='AgreementDetailView'),
)
