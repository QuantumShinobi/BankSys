import bcrypt
from django.core.exceptions import ValidationError
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .gen import *
from django.views import View


categories = ["Groceries", "Transportation", "Dining", "Entertainment", "Clothing", "Debt Payments", "Healthcare", "Insurance", "Savings and Investments",
                           "Taxes", "Education", "Charitable Donations", "Travel", "Business Expenses", "Rent", "Utilities: Electricity bills, etc.", "Loan Payments", "Money Earned"]
currency_symbols = {"USD": "$", "EUR": "€", "JPY": "¥", "GBP": "£", "AUD": "$", "CAD": "$", "CHF": "Fr.", "CNY": "¥", "INR": "₹",
                    "BRL": "R$", "RUB": "₽", "KRW": "₩", "MXN": "$", "ZAR": "R", "SGD": "$", "NZD": "$", "HKD": "$", "SEK": "kr", "NOK": "kr", "TRY": "₺"}
currency_names = {"USD": "United States Dollar", "EUR": "Euro", "JPY": "Japanese Yen", "GBP": "British Pound Sterling", "AUD": "Australian Dollar", "CAD": "Canadian Dollar", "CHF": "Swiss Franc", "CNY": "Chinese Yuan", "INR": "Indian Rupee", "BRL": "Brazilian Real",
                  "RUB": "Russian Ruble", "KRW": "South Korean Won", "MXN": "Mexican Peso", "ZAR": "South African Rand", "SGD": "Singapore Dollar", "NZD": "New Zealand Dollar", "HKD": "Hong Kong Dollar", "SEK": "Swedish Krona", "NOK": "Norwegian Krone", "TRY": "Turkish Lira"}


class IndexView(View):
    @staticmethod
    def get(request):
        if isinstance(User.get_user(request=request), User):
            user = User.get_user(request=request)
            try:
                transaction_list = user.get_transactions()
                if len(transaction_list) == 0:
                    return render(request, 'main/index.html', context={"user": user, "host": request.META['HTTP_HOST'], "categories": categories, "currency_symbol": currency_symbols[user.currency]})
            except TypeError:
                return render(request, 'main/index.html', context={"user": user, "host": request.META['HTTP_HOST'], "categories": categories, "currency_symbol": currency_symbols[user.currency]})
            last = transaction_list[-5::]
            return render(request, 'main/index.html', context={"user": user, "transactions": last[::-1], "host": request.META['HTTP_HOST'], "categories": categories, "currency_symbol": currency_symbols[user.currency]})

        return User.get_user(request=request)


class LoginView(View):
    @staticmethod
    def get(request):
        try:
            request.COOKIES['user-identity']
        except KeyError:
            return render(request, 'main/login.html')
        else:
            return redirect("main:index")


class SignedUpView(View):
    @staticmethod
    def post(request):
        try:
            request.COOKIES['user-identity']
        except KeyError:
            username = request.POST['username']
            password = request.POST['password']
            name = request.POST['name']
            if User.objects.filter(username=username).exists() is True:
                return render(request, "main/signup.html", context={'error': "Username has already been taken"})
            else:
                if len(password) < 8:
                    return render(request, "main/signup.html", context={'error': "Password should be atleast 8 characters long"})
                hash_pwd = bcrypt.hashpw(
                    bytes(password, 'utf-8'), bcrypt.gensalt())
                name = name.capitalize()
                new_user = User.objects.create(
                    username=username, password=hash_pwd, name=name)
                response = render(request, 'main/logout.html',
                                  context={"title": "Sign up", "text": "Creating your account"})
                response.set_cookie("user-identity", str(new_user.unique_id))

                return response

        else:
            return redirect("main:index")

    @staticmethod
    def get(request):
        raise Http404


def signup(request):
    try:
        request.COOKIES['user-identity']
    except KeyError:
        return render(request, 'main/signup.html')
    else:
        return redirect("main:index")


class LoggedInView(View):
    @staticmethod
    def post(request):
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists() == True:
            user = User.objects.get(username=username)
            return user.authenticate(password, request)
        return render(request, "main/login.html", context={'error': "There is no account associated with this username"})

    @staticmethod
    def get(request):
        raise Http404()


class AnalysisView(View):
    def get(self, request):
        return render(request, "main/analysis.html")

    def post(self, request):
        pass


def logout(request):
    return User.logout(request=request)


def add(request):
    if request.method == "POST":
        money_to_add = request.POST['add_amount']
        reason = request.POST['reason']
        id = request.COOKIES['user-identity']

        user = User.objects.get(unique_id=id)
        try:
            user.bank_balance += int(money_to_add)
            user.save()
            new_transaction_created = Transaction(
                user=user, amount=money_to_add, type="Add", reason=reason)
            user.transaction(new_transaction_created)
        except ValueError:
            return render(request, "error.html", context={"error": "Please enter an integer!"})
        return redirect("main:index")
    return render(request, "error.html", context={"error": "Access Denied"})


def withdraw(request):
    if request.method == "POST":
        money_to_withdraw = request.POST['withdraw_amount']
        category = request.POST['category']
        reason = request.POST['reason']
        id = request.COOKIES['user-identity']
        user = User.objects.get(unique_id=id)
        try:
            money_to_withdraw = int(money_to_withdraw)
        except ValueError:
            return render(request, "error.html", context={"error": "Please enter an integer!"})

        if int(money_to_withdraw) > user.bank_balance:
            return render(request, "error.html", context={"error": "You dont have that much money. YOu BrOkE Bruh 🙁 💸"})
        user.bank_balance -= int(money_to_withdraw)
        user.save()
        new_transaction_created = Transaction(
            user=user, amount=money_to_withdraw, type="Withdraw", reason=reason, category=category)
        user.transaction(new_transaction_created)
        return redirect("main:index")
    return render(request, "error.html", context={"error": "Access Denied"})


def del_account(request):
    if request.method == "POST":
        if isinstance(User.get_user(request=request), User):
            user = User.get_user(request=request)
            user.delete()
            res = render(request, "main/logout.html",
                         context={"text": "Deleting your account"})
            res.delete_cookie("user-identity")
            return res
        return User.get_user(request=request)
    else:
        return HttpResponse("ACCESS DENIED")


def account(request):
    if isinstance(User.get_user(request=request), User):
        user = User.get_user(request=request)
        return render(request, "main/account.html", context={"user": user, "currency_symbol": currency_symbols[user.currency], "currency": currency_names[user.currency], "currencies": [f"{currency_names[a]} ({currency_symbols[a]})" for a in currency_symbols]})

    else:
        return User.get_user(request)


def change_pwd(request):
    if isinstance(User.get_user(request=request), User):
        user = User.get_user(request=request)
        if request.method == "GET":
            return HttpResponse("Access Denied")
        if request.method == "POST":
            pwd = request.POST['password']
            hash_pwd = bcrypt.hashpw(
                bytes(pwd, 'utf-8'), bcrypt.gensalt())
            user.password = hash_pwd
            user.save()

            host = request.META['HTTP_HOST']
            return redirect(f"http://{host}/yourAccount?pwd_change=true")
    else:
        return User.get_user(request=request)


# Transaction list for user
def transaction_list(request):
    if isinstance(User.get_user(request=request), User):
        user = User.get_user(request=request)
        try:
            transaction_list = user.get_transactions()
        except TypeError:
            return render(request, "main/transactions.html", context={"no_t": "You have no transactions"})
        return render(request, "main/transactions.html", context={"transactions": transaction_list, "host": request.META['HTTP_HOST'], "currency_symbol": currency_symbols[user.currency]})
    return User.get_user(request=request)


def delete_transaction_history(request):
    if isinstance(User.get_user(request=request), User):
        if request.method == "POST":
            user = User.get_user(request=request)
            user.transaction_list = []
            user.save()
            host = request.META['HTTP_HOST']
            return redirect(f"http://{host}/yourAccount?t_list_erase=true")
        return HttpResponse("Access Denied")


def transaction(request, transaction_id):
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
        user = transaction.user
        return render(request, "main/transaction.html", context={"transaction": transaction, "user": user, "currency_symbol": currency_symbols[user.currency]})
    except (Transaction.DoesNotExist, KeyError, ValidationError):
        return HttpResponse("Invalid ID")


class ChangeCurrencyView(View):
    def get(self, request):
        return HttpResponse("Access Denied")

    def post(self, request):
        user = User.get_user(request=request)
        currency = request.POST['currency'][:-4]

        for a, b in currency_names.items():
            if b == currency:
                c = a
        user.currency = c
        host = request.META['HTTP_HOST']
        user.save()

        return redirect(f"http://{host}/yourAccount?currency_change=true")
