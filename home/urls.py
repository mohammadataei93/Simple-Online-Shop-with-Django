from django.urls import path, include
from . import views

app_name = 'home'

bucket_urls = [
    path('', views.BucketHomeView.as_view(), name='bucket'),
    path('delete-object/<str:key>/', views.DeleteBucketObjectView.as_view(), name='delete-object-bucket'),
    path('download-object/<str:key>/', views.DownloadBucketObjectView.as_view(), name='download-object-bucket'),
]

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('category/<slug:category_slug>/', views.HomeView.as_view(), name='category-filter'),
    path('bucket/', include(bucket_urls)),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail')
]
