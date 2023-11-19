from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('col', views.index, name="index_col"),
    path('col/index/', views.index, name="index_collaborator"),
    path('col/student/<str:student_code>/student_detail', views.student_detail, name='student_detail_collaborator'),
    path('col/students/', views.students_view, name="students_col"),
    path('col/send_info/', views.send_info, name="send_info_col"),
    path('col/student/<int:student_id>/create_alert/', views.create_alert, name='create_alert'),
    path('col/collaborator/create/', views.create_collaborator, name='create_collaborator'),
    path('col/collaborator/', views.collaborator_view, name='collaborator'),
    path('col/collaborator/<str:collaborator_code>/detail',
         views.collaborator_detail, name='collaborator_detail'),
    path('col/collaborator/<str:collaborator_code>/edit/',
         views.collaborator_edit, name='collaborator_edit'),
    path('col/collaborator/<str:collaborator_code>/delete/', views.collaborator_delete, name='delete_collaborator'),
    path('col/registrate/', views.registrate_user, name='registrate_collaborator'),
    path('col/info_dissemination/', views.info_dissemination, name='info_dissemination_col'),
    path('col/create_alert/<str:student_code>/', views.create_alert, name='create_alert_collaborator'),
    path('col/update_info/<str:student_code>/', views.update_info, name='update_info_student'), # url para actualizar info
    # maneja los dos métodos del form GET y POST | GET para devolver la pagina donde sube el archivo y POST para manejar
    # el archivo que ya subió y guardarlo
    path('col/info_dissemination/send', views.send_info, name='send_info_col'),
    path('col/info_dissemination/show', views.show_info, name='show_info_col')
]
