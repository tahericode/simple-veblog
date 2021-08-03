from django.urls import path
from .views import contact_us, detail_list, post_list

urlpatterns = [
    path('',post_list, name= "index"),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/',detail_list, name="post_detail"),
    path('contact-us',contact_us, name="contact_us"),
]
