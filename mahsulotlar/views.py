import json

from django.shortcuts import redirect
from django.http import JsonResponse
from .services import *
from config.settings import MEDIA_ROOT
from .forms import *

from django.shortcuts import render
from .models import ElektronXizmat

def xizmatlar_royxati(request):
    xizmatlar = ElektronXizmat.objects.all()
    return render(request, 'mahsulotlar/index.html', {'xizmatlar': xizmatlar})


def home_page(request):
    if request.GET:
        product = get_product_by_id(request.GET.get("product_id", 0))
        return JsonResponse(product, safe=False)


def order_page(request):
    if request.GET:
        user = get_user_by_phone(request.GET.get("phone_number",0))
        return JsonResponse(user)

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    orders = []
    orders_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price",0)
    print(orders_list)
    print(total_price)
    if orders_list:
        for key, val in json.loads(orders_list).items():
            orders.append(
                {
                "product": Product.objects.get(pk=int(key)),
                "count": val
                }
            )
    ctx = {
        'categories': categories,
        'products': products,
        'orders':orders,
        'total_price':total_price,
        'MEDIA_ROOT': MEDIA_ROOT
    }

    response = render(request, 'mahsulotlar/index.html', ctx)
    response.set_cookie("greeting", 'hello')
    return response

def main_order(request):
    model=Customer()
    if request.POST:
        try:
            model = Customer.objects.get(phone_number=request.POST.get("phone_number", ""))
        except:
            model = Customer()
        form = CustomerForm(request.POST or None, instance=model)
        if form.is_valid():
            customer = form.save()
            formOrder = OrderForm(request.POST or None, instance=Order())
            if formOrder.is_valid():
                order = formOrder.save(customer=customer)
                print("order:",order)
                orders_list = request.COOKIES.get("orders")


                for key,value in json.loads(orders_list).items():
                    product = get_product_by_id(int(key))

                    counts = value
                    order_product = OrderProduct(
                        count=counts,
                        price = product['price'],
                        product_id = product['id'],
                        order_id = order.id
                    )
                    order_product.save()

                return redirect("index")
            else:
                print(formOrder.errors)
        else:
            print(form.errors)

    categories = Category.objects.all()
    products = Product.objects.all()
    orders = []
    orders_list = request.COOKIES.get("orders")
    total_price = request.COOKIES.get("total_price")
    if orders_list:
        for key, val in json.loads(orders_list).items():
            orders.append(
                {
                "product": Product.objects.get(pk=int(key)),
                "count": val
                }
            )
    ctx = {
        'categories': categories,
        'products': products,
        'orders':orders,
        'total_price':total_price,
        'MEDIA_ROOT': MEDIA_ROOT,
    }

    response = render(request, 'mahsulotlar/order.html', ctx)
    # response.set_cookie("greeting", 'hello')
    return response

def send_order(request):
    return redirect(index)
    return render(request, 'mahsulotlar/order.html')