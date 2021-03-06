"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from blog.views import (
    IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
)
from blog.apis import PostViewSet, CategoryViewSet
from config.views import LinkListView
from comment.views import CommentView
from .custom_site import custom_site

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')
router.register(r'category', CategoryViewSet, basename='api-category')


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    re_path(r'^category/(?P<category_id>\d+)/$',
            CategoryView.as_view(), name='category-list'),
    re_path(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    re_path(r'^post/(?P<post_id>\d+).html$',
            PostDetailView.as_view(), name='post-detail'),
    re_path(r'^author/(?P<owner_id>\d+)/$',
            AuthorView.as_view(), name='author'),
    path('links/', LinkListView.as_view(), name='links'),
    path('search/', SearchView.as_view(), name='search'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('super_admin/', admin.site.urls, name='super-admin'),
    path('admin/', custom_site.urls, name='admin'),
    path('api/', include(router.urls)),
    path('api/docs', include_docs_urls(title='tyoeidea apis')),
]
#  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
