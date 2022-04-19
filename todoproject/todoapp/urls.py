from django.conf.urls.static import static

from todoproject import settings
from . import views
from django.urls import path,include

from .views import add

urlpatterns = [

    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete')
 #   path('details',views.details,name='details')
]
