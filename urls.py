from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculate_area,name='calculate_area'),
]

Calculate Churn Rate
churn=initialCust/PresentCust