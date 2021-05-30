from django.urls import path
from . import views
from django_cloud_deployer import runInPaaS, runInFaaS


app_name = 'comments'
urlpatterns = [
    path('<int:pk>/delete/', views.CommentDelete.as_view(), name='comment-delete'),
    runInPaaS(path('<comment_id>/<event_id>/detail/', views.comment_detail, name='comment-detail')),
]
