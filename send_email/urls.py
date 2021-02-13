from django.urls import path
from send_email.views import MessageEdit, MessageList, MessageDetail, message_create_many
from send_email import views

app_name = "send_email"

urlpatterns = [
    path('', MessageEdit.as_view(), name="message-edit"),
    path('message_create/', views.message_create),
    path('message_list/', MessageList.as_view(), name="message-list"),
    path('message_list/<int:pk>/', MessageDetail.as_view(), name="message-detail"),
    path('send_email_many/', message_create_many, name='message-create-many'),
]