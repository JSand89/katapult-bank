from django.urls import path
from . import views

urlpatterns = [
    path('',views.BankListView.as_view(),name='banks'),
]

#urls banks
urlpatterns += [
    path('<int:pk>',views.BankDetailView.as_view(),name='bank-detail'),
    path('create/',views.BankCreateView.as_view(),name='bank-create'),
    path('<int:pk>/update/',views.BankUpdateView.as_view(), name='bank-update'),
    path('<int:pk>/delete/',views.BankDeleteView.as_view(), name='bank-delete'),
]

urlpatterns += [
    path('supplier/',views.SupplierListView.as_view(),name='suppliers'),
    path('supplier/<int:pk>',views.supplier_detail,name='supplier-detail'),
    path('supplier/create',views.SupplierCreateView.as_view(),name='supplier-create'),
    path('supplier/<int:pk>/update',views.SupplierUpdateView.as_view(), name='supplier-update'),
    path('supplier/<int:pk>/delete',views.SupplierDeleteView.as_view(), name='supplier-delete'),
]