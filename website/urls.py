from django.urls import path
from . import views

urlpatterns = [
    # path("samsung",views.samsung),
    #path("iphone",views.iphone),
    #path("realme",views.realme),
    path("<int:Offer>",views.cart_int),
    path('<str:Offer>',views.cart,name="amazon_cart"),
    path("",views.index)
]
