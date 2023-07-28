from django.urls import path
from .views import *


urlpatterns = [
    path('', hoem_page, name='home_page'),
    path('post-details/<int:id>', post_details, name='post_details'),
]
