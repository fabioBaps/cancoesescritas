from django.urls import path

from . import views

app_name = 'songs'
urlpatterns = [
    path('', views.ListView, name='list'),
    path('create/', views.CreateView, name='create'),
    path('<int:post_id>/', views.DetailView, name='detail'),
    path('update/<int:post_id>/', views.UpdateView, name='update'),
    path('delete/<int:post_id>/', views.DeleteView, name='delete'),
    # path('', views.postFormListView.as_view(), name='list'),
    # path('<int:pk>/', views.postFormDetailView.as_view(), name='detail'),
    # path('create/', views.postFormCreateView.as_view(), name='create'),
    # path('update/<int:pk>/', views.postFormUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', views.postFormDeleteView.as_view(), name='delete'),
    # path('', views.postListView.as_view(), name='list'),
    # path('<int:pk>/', views.postDetailView.as_view(), name='detail'),
    # path('create/', views.postCreateView.as_view(), name='create'),
    # path('update/<int:pk>/', views.postUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', views.postDeleteView.as_view(), name='delete'),
    path('search/', views.SearchView, name='search'),
    # path('<int:post_id>/comment/', views.commentCreateView, name='comment'),
    # path('categorys/', views.categoryListView.as_view(), name='categorys'),
    # path('categorys/<int:pk>/', views.categoryDetailView.as_view(), name='detail-category'),
    # path('categorys/create', views.categoryCreateView.as_view(), name='create-category'),
]