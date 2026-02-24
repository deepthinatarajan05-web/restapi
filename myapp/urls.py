from django.urls import path
from .views import studentlist

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('ad/<int:id>/',studentlist),
]