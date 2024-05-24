from django.urls import path, include
from rest_framework import routers
from task import views
from rest_framework.schemas import get_schema_view

#api versioning 

router=routers.DefaultRouter()
router.register(r'task', views.taskView, 'task')


urlpatterns = [
    
    path("api/v1/", include(router.urls)),
    path("docs/", get_schema_view(
                                title="Your Project", 
                                description="API for all things …", 
                                version="1.0.0"
                                ),
                                name="openapi-schema",
        ),
   
]
