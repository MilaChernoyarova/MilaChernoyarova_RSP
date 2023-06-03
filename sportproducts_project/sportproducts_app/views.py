from django.shortcuts import render
from .models import Product, MyProduct
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def index(request):
    all_products = Product.objects.all()
    my_products_sum = 0
    my_products_count = 0

    if request.POST.get('buy_btn') == 'КУПИТЬ':
        product_id = request.POST.get('product_id')

        try:
            my_product = Product.objects.get(id=product_id)
            if MyProduct.objects.filter(model=my_product.model).exists():
                print("Товар уже в корзине")
            else:
                MyProduct.objects.create(
                    title=my_product.title,
                    price=my_product.price,
                    discription=my_product.discription,
                    image_url=my_product.image_url,
                    model=my_product.model
                )

        except ObjectDoesNotExist:
            print("Объект не сушествует")

        except MultipleObjectsReturned:
            print("Найдено более одного объекта")
    
    for product in MyProduct.objects.all():
        my_products_sum += product.price
    my_products_count = len(MyProduct.objects.all())

    context = {
        'all_products' : all_products,
        "my_products_sum" : my_products_sum,
        "my_products_count" : my_products_count,
    }
    return render(request, 'index.html', context)



def detail(request, product_id):
    my_products_sum = 0
    my_products_count = 0

    if request.POST.get('buy_btn') == 'КУПИТЬ':
        try:
            my_product = Product.objects.get(id=product_id)
            if MyProduct.objects.filter(model=my_product.model).exists():
                print("Товар уже в корзине")
            else:
                MyProduct.objects.create(
                    title=my_product.title,
                    price=my_product.price,
                    discription=my_product.discription,
                    image_url=my_product.image_url,
                    model=my_product.model
                )
        except ObjectDoesNotExist:
            print("Объект не сушествует")

        except MultipleObjectsReturned:
            print("Найдено более одного объекта")

    for product in MyProduct.objects.all():
        my_products_sum += product.price
    my_products_count = len(MyProduct.objects.all())

    context = {
        'product' : Product.objects.get(id=product_id),
        "my_products_sum" : my_products_sum,
        "my_products_count" : my_products_count,
    }
    return render(request, 'detail.html', context)



def shopping_cart(request):
    my_products = MyProduct.objects.all()
    my_products_sum = 0
    my_products_count = 0

    if request.POST.get('clear_cart') == 'ОЧИСТИТЬ КОРЗИНУ':
        for product in my_products:
            product.delete()
    
    for product in my_products:
        my_products_sum += product.price
    my_products_count = len(MyProduct.objects.all())

    context = {
        'my_products' : my_products,
        "my_products_sum" : my_products_sum,
        "my_products_count" : my_products_count,
    }

    return render(request, 'shopping_cart.html', context)

