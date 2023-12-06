# from django.urls import path
# from.views import forgotcreate
# urlpatterns=[
#      path('',forgotcreate.as_view() ),
#  ]
from django.urls import path
from.views import ForgotList
urlpatterns=[
    path('',ForgotList.as_view() ),
]