from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# from . import products
products = [
    {'id':1,'name':'Iphone','price':45000},
    {'id':2,'name':'Redmi','price':35000},
    {'id':3,'name':'Realme','price':25000},
    {'id':4,'name':'Vivo','price':15000},
]

# Create your views here.
def entry_page(req):
    return render(req,'login.html')

def login(req):
    # print(req.method)
    print(req.POST.get('username'))
    print(req.POST.get('password'))
    db_user = 'Nayab'
    db_pass = 'nayab@123'
    if db_user == req.POST.get('username') and db_pass == req.POST.get('password'):
        return HttpResponse('Login Success!')
    else:
        return HttpResponse('Invalid Credentials')

# def get_product(req,id):
#     for product in products.product_list:
#         if product.get('id') == int(id):
#             return render(req,'home.html',{'product':product})
#     return HttpResponse('Invalid ID!')

def all_product(req):
    if req.method == 'POST':
        p_name = req.POST.get('prod_name')
        p_price = req.POST.get('price')
        p_id = len(products)+1
        new_product = {
            'id':p_id,
            'name':p_name,
            'price':p_price
        }
        products.append(new_product)
    return render(req,'home.html',{'products':products})

def delete_product(req,id):
    for product in products:
        if product.get('id') == id:
            products.remove(product)
    return render(req,'home.html',{'products':products})

def update_product(req,id):
    if req.method == 'POST':
        p_name = req.POST.get("name")
        p_price = req.POST.get('price')

        for product in products:
            if product.get('id') == id:
                product['name'] = p_name
                product['price'] = p_price
                return render(req,'home.html',{'products':products})

    required_product = None
    for product in products:
        if(product).get('id') == id:
            required_product = product
    return render(req,'update.html',{'product':required_product})