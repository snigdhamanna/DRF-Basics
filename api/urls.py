from django.urls import path , include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')



urlpatterns = [
    path('student/',views.studentview, name='studentview'),
    path('student/<int:pk>/',views.studentviewdetail, name='studentviewdetail'),
    
    # #cbv employee
    # 
    # path('employees/', views.EmployeeList.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    # 
    path('', include(router.urls)),
    
    
    
    # nested serializer 
    path('blog/',views.Blogview.as_view(), name='blogview'),
    path('comments/',views.Commentview.as_view(), name='commentview'),
    
    
            
]