from django.urls import path
from blog import views

urlpatterns=[
    path('',views.Home.as_view(),name="home"),

    path('article/<int:pk>',views.ArticleView.as_view(),name='article'),
    path('addpost/',views.AddPostView.as_view(),name='add_post'),
    path('article/update/<int:pk>',views.UpdatePostView.as_view(),name='update_post'),
    path('article/delete/<int:pk>',views.DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>/',views.CategoryView,name='category'),

    path('category-details/',views.CategoryDetail,name='category_detail'),
    path('like/<int:pk>',views.LikeView,name='like_post'),
    path('article/<int:pk>/comment',views.AddCommentView.as_view(),name='add_comment')
]