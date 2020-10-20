from django.contrib import admin
from django.urls import path
import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.index, name ="index"),
    path('sobang', mainapp.views.sobang, name ="sobang"),
    path('dongpo', mainapp.views.dongpo, name ="dongpo"),
    path('susanbangsong', mainapp.views.susanbangsong, name ="susanbangsong"),
    path('founder', mainapp.views.founder, name ="founder"),
    path('iyousystemz', mainapp.views.iyousystemz, name ="iyousystemz"),
    path('student', mainapp.views.student, name ="student"),
]
