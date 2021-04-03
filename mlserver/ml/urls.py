# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^ml/swagger', TemplateView.as_view(template_name="index.html"), name='swagger_ui'),
    url(r'^ml/v1/service?$', views.service, name='service'),
]
