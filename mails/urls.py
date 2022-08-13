from . import views
from django.urls import path

urlpatterns = [
    path('received/', views.received, name='received'),
    path('outgoing/', views.outgoing, name='outgoing'),
    path('draft/', views.draft, name='draft'),
    path('new/', views.new, name='new'),
    path('reply/<int:id>/', views.reply, name='reply'),
    path('mail/<int:id>/', views.mail, name='mail'),
    path('send_draft/<int:id>/', views.send_draft, name='send_draft'),
    path('attachment_received/', views.attachment_received, name='attachment_received'),
    path('attachment_outgoing/', views.attachment_outgoing, name='attachment_outgoing'),
]
