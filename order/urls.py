from django.urls import path
from .views import cart_view, ChechoutProcess, PaymentView
app_name = 'order'

urlpatterns = [
		
			path('cart/',cart_view, name= 'cart_view' ),
			path('checkout/', ChechoutProcess.as_view(), name= 'checkout'),
			path('payment/',PaymentView.as_view(), name='stripe' )

		]