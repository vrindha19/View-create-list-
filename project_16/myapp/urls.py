#  create view


# from django.urls import path
# from.views import logincreate
# urlpatterns=[
#     path('',logincreate.as_view() ),
# ]


# list view 



from django.urls import path
from.views import LoginList
urlpatterns=[
    path('',LoginList.as_view() ),
]