from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('doctor/',views.doctor,name="doctor"),
    path('patient/',views.patient,name="patient"),
    path('patient_history/',views.phf,name="patient_history"),
    path('ward/',views.ward,name="ward"),
    path('delete_doc/<int:did>',views.delete_doc,name="delete_doc"),
    path('delete_pat/<int:did>',views.delete_pat,name="delete_pat"),
    path('delete_ward/<int:did>',views.delete_ward,name="delete_ward"),
    path('edit_doc/<int:did>',views.edit_doctor,name="edit_doc"),
    path('edit_pat/<int:did>',views.edit_patient,name="edit_pat"),
    path('edit_ward/<int:did>',views.edit_ward,name="edit_ward"),
    path('fiss/',views.fil_issue,name="fiss"),
    path('list/',views.PatientHistoryView.as_view(),name="list"),
    path('detail/<int:pk>',views.PatientHistoryDetalView.as_view(),name="detail"),  
]
