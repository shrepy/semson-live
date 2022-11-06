from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.home, name='homepage'),
    path('login',views.Login.as_view(),name='login'),
    # path('homepage',views.homepage, name='homepage')
    path('products',views.products, name='products'),
    path('contact',views.showContactUs, name='contact'),
    path('about',views.about, name='about'),
    path('cart',views.cart,name='cart'),
    path('logout',views.myLogout,name='logout'),
    path('register',views.Register.as_view(), name='register'),
    path('addproduct',views.Product.as_view(), name='addproduct'),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)