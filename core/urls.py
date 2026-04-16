from django.urls import path,include
from core import views
from django.conf.urls.static import static,settings

urlpatterns = [
    path('',views.index,name='home'),
    path('base.html/',views.base,name='base'),
    path('bachay/<int:student_id>',views.stuent_details,name='student_details'),
    path('add/', views.add_student, name='add_student'),
    path("formsave1/",views.addimginform,name="addimginform"),
    path('api/students/', views.student_list_api, name='student_api'),
    path('api/apicrud/<int:pk>/', views.student_detail_api,name="aapi"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)