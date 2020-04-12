from django.urls import path

from .views import home, approve_ticket, disapprove_ticket, approved_ticket_list, disapproved_ticket_list

urlpatterns = [
    path('approve/<int:ticket_id>', approve_ticket, name='approve_ticket'),
    path('disapprove/<int:ticket_id>', disapprove_ticket, name='disapprove_ticket'),
    path('approvedlist/', approved_ticket_list, name='approved_ticket_list'),
    path('disapprovedlist/', disapproved_ticket_list, name='disapproved_ticket_list'),
    path('', home, name='staff_home'),
]
