from django.urls import path
from.views import PostDeleteView, post_comment_create_list, like_unlike_post, PostUpdateview

urlpatterns = [
    path('', post_comment_create_list, name = 'home'),
    path('liked/', like_unlike_post, name = "like_unlike_post"),
    path('<pk>/delete/', PostDeleteView.as_view(), name = "post_delete"),
    path('<pk>/update/', PostUpdateview.as_view(), name = "post_update")
]