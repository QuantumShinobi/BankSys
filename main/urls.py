from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', main, name="home"),
    path('index', IndexView.as_view(), name="index"),
    path('login', LoginView.as_view(), name="login"),
    path('signed_up', SignedUpView.as_view(), name="signed_up"),
    path('logged_in', LoggedInView.as_view(), name="logged_in"),
    path('signup', signup, name="signup"),
    path('logout', logout, name="logout"),
    path('a', add, name="add"),
    path('w', withdraw, name="withdraw"),
    path('del', del_account, name="delete_account"),
    path('yourAccount', account, name="account"),
    path("cp", change_pwd, name="change_pwd"),
    path("t_list", transaction_list, name="transaction_list"),
    path("d_list", delete_transaction_history, name="delete_transactions"),
    path("transaction/<str:transaction_id>", transaction, name="transaction"),
    path("changeCurrency",
         ChangeCurrencyView.as_view(),
         name="change_currency"),
    path("analysis", spending_analysis, name="analysis"),
    path("friends", FriendsView.as_view(), name="friends"),
    path("addFriends", AddFriends.as_view(), name="add_friends"),
    path("transfer", TransferView.as_view(), name="transfer_money")
]
