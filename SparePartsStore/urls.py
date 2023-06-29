from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings  # Import settings module correctly

urlpatterns = [
                  path('', views.index),
                  path('home', views.home),
                  path('test/', views.test),
                  path('category/<int:category_id>/', views.category_page, name='category_page'),
                  path('cart', views.cart, name='cart'),
                  path('cart/success', views.success),
                  path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
                  path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add the following code to serve media files during development
# if settings.DEBUG:
#     from django.conf.urls.static import static
