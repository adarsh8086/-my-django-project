

from django.urls import path
from .views import CustomLoginView, Shop, add_to_cart, cart,home,register,men_category_view, women_category_view,ProductDetailView,about_us_view,buy_now
from . import views
from myapp import views


from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import confirm_order
from .views import clear_orders, cancel_last_order
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('',home, name='home'),
    path('shop/', Shop, name='shop'),
    path('shop/men/', men_category_view, name='men_category'),
    path('shop/women/', women_category_view, name='women_category'),
    path('about-us/', about_us_view, name='about_us'),
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),
    path('buy/<int:product_id>/', views.buy_now, name='buy_now'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('register/', register, name='register'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path('buy/<int:product_id>/', buy_now, name='buy_now'),
    path('confirm-order/', confirm_order, name='confirm_order'),
    path('view_ordered_items/', views.view_ordered_items, name='view_ordered_items'),
    path('clear_orders/', clear_orders, name='clear_orders'),
    # path('cancel-last-order/<int:item_id>/', cancel_last_order, name='cancel_last_order'),
    path('cancel-last-order/<int:order_id>/', views.cancel_last_order, name='cancel_last_order'),
       
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





