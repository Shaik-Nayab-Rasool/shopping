from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.entry_page),
    path('login/',views.login),
    # path('product/<int:id>',views.get_product),
    path('all_products/',views.all_product),
    path('delete/<int:id>',views.delete_product,name='delete'),
    path('update/<int:id>',views.update_product,name='edit')
]