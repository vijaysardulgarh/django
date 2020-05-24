from . import views
from django.urls import path,include
from rest_framework import routers
#app_name='app5'
router=routers.DefaultRouter()
router.register('app5',views.CourseView)
urlpatterns = [
path('home/',views.home,name='home'),
#path('about/', views.about, name='about'),
path('contact/',views.contact,name='contact'),
#path('faq/',views.faq,name='faq'),
path('',include(router.urls))
]