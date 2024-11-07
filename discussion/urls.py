from django.urls import path
from . import views

urlpatterns = [
    path('discussion/<int:code>', views.discussion, name='discussion'),
    path('send/<int:code>/<int:std_id>', views.send, name='send'),
    path('message/<int:code>/<int:id>', views.send_instructor, name='send_instructor'),
]