from .views import TodoViewSet
from django.urls import path

todo_list = TodoViewSet.as_view({
    'get': 'list',
})
todo_create = TodoViewSet.as_view({
        # 'get': 'list',
        'post': 'create'
})
todo_detail = TodoViewSet.as_view({
    'get': 'retrieve',
})
todo_update = TodoViewSet.as_view({
    'post': 'update',
})
todo_delete = TodoViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = [
    path('',todo_list,name="todolist"),
    path('todo-create/',todo_create,name="todocreate"),
    path('todo-detail/<int:pk>/',todo_detail,name="tododetail"),
    path('todo-update/<int:pk>/',todo_update,name="todoupdate"),
    path('todo-delete/<int:pk>/',todo_delete,name="tododelete"),
]
