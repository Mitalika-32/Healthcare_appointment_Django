
from django.contrib import admin
from django.urls import path
from sitehandler.views import *
# from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('about/',aboutpage,name='aboutpage'),
    path('login/',loginpage,name='loginpage'),
    path('createaccount',createaccountpage,name='createaccountpage'),
    path('admin_login/',Login_admin,name='login_admin'),
    path('adminhome/',AdminHome,name='adminhome'),
    path('adminlogout/',Logout_admin,name='adminlogout'),
    path('adminaddDoctor/',adminaddDoctor,name='adminaddDoctor'),
    path('adminviewDoctor/',adminviewDoctor,name='adminviewDoctor'),
    path('adminDeleteDoctor<int:pid>/<str:email>',admin_delete_doctor,name='admin_delete_doctor'),
    path('adminaddReceptionist/',adminaddReceptionist,name='adminaddReceptionist'),
    path('adminviewReceptionist/',adminviewReceptionist,name='adminviewReceptionist'),
    path('adminDeleteReceptionist<int:pid>/<str:email>',admin_delete_receptionist,name='admin_delete_receptionist'),
    path('adminviewAppointment/',adminviewAppointment,name='adminviewAppointment'),
    path('home/',Home,name='home'),
    path('profile/',profile,name='profile'),
    path('makeappointments/',MakeAppointments,name='makeappointments'),
    path('viewappointments/',viewappointments,name='viewappointments'),
    path('PatientDeleteAppointment<int:pid>',patient_delete_appointment,name='patient_delete_appointment'),
    path('logout/',Logout,name='logout'),
    path('patient/dashboard/', Home, name='patient_dashboard'),
    path('doctor/dashboard/', Home, name='doctor_dashboard'),
    path('reception/dashboard/', Home, name='reception_dashboard'),
     path('approve_appointment/<int:appointment_id>/', approve_appointment, name='approve_appointment'),
    path('decline_appointment/<int:appointment_id>/', decline_appointment, name='decline_appointment'),
    # path('add-prescription/', add_prescription, name='add_prescription'),
]


