from django.urls import path

from . import views

app_name = 'banking'
urlpatterns = [
    # ex: /banking/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /banking/5/
    path('<int:pk>/history', views.HistoryView.as_view(), name='history'),
    # ex: /banking/make_t/
    path('<int:accountId>/pay', views.pay, name='pay'),
]