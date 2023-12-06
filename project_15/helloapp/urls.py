# from django.urls import path
# from.views import registercreate
# urlpatterns=[
#      path('',registercreate.as_view() ),
#  ]

from django.urls import path
from.views import RegisterList
urlpatterns=[
    path('',RegisterList.as_view() ),
]