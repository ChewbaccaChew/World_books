from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('edit1/<int:pk>', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
