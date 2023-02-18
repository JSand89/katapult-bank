from django.urls import path
from . import views

urlpatterns = [
    path('',views.BankListView.as_view(),name='banks'),
    path('<int:pk>',views.BankDetailView.as_view(),name='bank-detail'),
]

urlpatterns += [
    path('create/',views.BankCreateView.as_view(),name='bank-create'),
    path('<int:pk>/update/',views.BankUpdateView.as_view(), name='bank-update'),
    path('<int:pk>/delete/',views.BankDeleteView.as_view(), name='bank-delete'),
]