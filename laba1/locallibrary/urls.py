"""
URL configuration for locallibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import index,renew_book_librarian,BookCreate,BookUpdate,BookDelete, BookListView, BookDetailView, AuthorListView, AuthorDetailView, LoanedBooksByUserListView, LoanedBooksAllListView, AuthorCreate,AuthorUpdate,AuthorDelete
urlpatterns = [
    path('', index , name='index'),
    path('books/' , BookListView.as_view() , name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('admin/', admin.site.urls),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',AuthorDetailView.as_view(), name='author-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'), 
    path('borrowed/', LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
    path('book/create/', BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)