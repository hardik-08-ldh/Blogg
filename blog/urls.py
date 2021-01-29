from django.urls import path
from blog import views
# from django.views.generic import TemplateView
urlpatterns=[
    path('',views.Home.as_view(),name="home"),
    # path('not_authenticated',views.NotAllowed.as_view(),name="not_allowed"),
    path('article/<int:pk>',views.ArticleView.as_view(),name='article'),
    path('addpost/',views.AddPostView.as_view(),name='add_post'),
    path('article/update/<int:pk>',views.UpdatePostView.as_view(),name='update_post'),
    path('article/delete/<int:pk>',views.DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>/',views.CategoryView,name='category'),
    # just cats is the name/|\ given
    path('category-details/',views.CategoryDetail,name='category_detail'),
    path('like/<int:pk>',views.LikeView,name='like_post'),
    path('article/<int:pk>/comment',views.AddCommentView.as_view(),name='add_comment')
]