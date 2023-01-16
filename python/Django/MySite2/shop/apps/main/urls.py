from django.urls import path

import apps.main.views as views

urlpatterns = [
    path('',views.indes),
    path('step1',views.step1),
    path('step2',views.step2),
]
