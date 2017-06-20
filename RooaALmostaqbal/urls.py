from django.conf.urls import url
from RooaALmostaqbal import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Booking/$',views.Booking,name='Booking'),
    url(r'^About/$',views.About,name='About'),
    url(r'^contact/$',views.contact,name='contact'),
]