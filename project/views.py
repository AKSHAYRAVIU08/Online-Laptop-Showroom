from django.shortcuts import render, redirect
from .models import Sign, Submit
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
# Create your views here.

def one(request):
    if request.method == "POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        print("username",username)
        print("email",email)
        print("password",password)
        if Sign.objects.filter(username=username).exists():
            messages.error(request,'Username already exist')
        else:
            Sign.objects.create_user(username=username,email=email,password=password)
            messages.error(request,'SignUp Successfull')
            return redirect('second')
    return render(request, 'one.html')


def two(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Login Success')
            return redirect('third')
        else:
            messages.error(request,'Invalid Username or Password')
    return render(request, 'two.html')


def three(request):
    return render(request, 'three.html')


def four(request):
    return render(request, 'four.html')


def five(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Login Success')
            return redirect('product_list')
        else:
            messages.error(request,'Invalid Username or Password')
    return render(request, 'five.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html',
                  {'products': products})


def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(request, 'product_form.html',
                  {'form': form})


def edit_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST,
                           request.FILES,
                           instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm(instance=product)

    return render(request, 'product_form.html',
                  {'form': form})


def delete_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'product_delete.html',
                  {'product': product})


def six(request):
    return render(request,'six.html')


def seven(request):
    return render(request,'seven.html')


def eight(request):
    return render(request,'eight.html')


def nine(request):
    return render(request,'nine.html')


def ten(request):
    return render(request,'ten.html')


def eleven(request):
    return render(request,'eleven.html')


def twovelve(request):
    return render(request,'twovelve.html')


def payment(request):

    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID,
              settings.RAZORPAY_KEY_SECRET)
    )

    payment_data = {
        "amount": 50000,   # Amount in paise = 500 INR
        "currency": "INR",
        "receipt": "order_rcptid_11"
    }

    order = client.order.create(data=payment_data)

    context = {
        'order_id': order['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'amount': payment_data['amount'],
        'currency': payment_data['currency'],
    }

    return render(request, 'payment.html', context)


@csrf_exempt
def payment_success(request):

    if request.method == "POST":

        client = razorpay.Client(
            auth=(settings.RAZORPAY_KEY_ID,
                  settings.RAZORPAY_KEY_SECRET)
        )

        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }

        try:
            client.utility.verify_payment_signature(params_dict)
            return render(request, 'payment_success.html')

        except:
            return HttpResponseBadRequest()
        

def verify_payment(request):

    payment_verified = True

    if payment_verified:
        return redirect('payment_success')
    else:
        return redirect('payment_failed')


def thirteen(request):
    return render(request,'thirteen.html')


def fourteen(request):
    return render(request,'fourteen.html')


def fifteen(request):
    return render(request,'fifteen.html')


def sixteen(request):
    return render(request,'sixteen.html')


def seventeen(request):
    return render(request,'seventeen.html')


def eighteen(request):
    return render(request,'eighteen.html')


def nineteen(request):
    return render(request,'nineteen.html')


def twentieth(request):
    return render(request,'twentieth.html')


def twentifirst(request):
    return render(request,'twentifirst.html')


def twentisecond(request):
    return render(request,'twentisecond.html')


def twentithird(request):
    return render(request,'twentithird.html')


def twentifourth(request):
    return render(request,'twentifourth.html')