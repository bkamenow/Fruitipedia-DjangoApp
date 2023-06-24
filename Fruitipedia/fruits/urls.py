from django.urls import path, include

from Fruitipedia.fruits.views import create_fruit, fruit_details, edit_fruit, delete_fruit

urlpatterns = [
    path('create/', create_fruit, name='create-fruit'),
    path('<int:pk>/', include([
            path('details/', fruit_details, name='fruit-details'),
            path('edit/', edit_fruit, name='edit-fruit'),
            path('delete/', delete_fruit, name='delete-fruit'),
        ])),
]
