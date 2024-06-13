from django.shortcuts import render, get_object_or_404, redirect

from django.views import View
from django.views.generic import TemplateView, ListView

from shop.models import Category, Product, Testimonial, Savat


class LandingView(View):
    def get(self, request):
        category = Category.objects.all()
        product = Product.objects.all()
        testimonial = Testimonial.objects.all()

        context = {
            'category': category,
            'product': product,
            'testimonial': testimonial
        }
        return render(request, 'shop/index.html', context)


class ProductListView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            products = Product.objects.all()
            context = {'products': products}
            print(products)
            return render(request, 'main/index.html', context)
        else:
            products = Product.objects.filter(name__icontains=search)
            if products:
                context = {'products': products}
                print("________________________________")
                print(products)
                return render(request, 'main/index.html', context)
            else:
                context = {'products': products}
                return render(request, 'main/index.html', context)


class ShopView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'shop/shop.html', {'product': product})


class ShopDetailView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'shop/shop-detail.html', {'product': product})


class AddToCartView(View):
    def get(self, request, id):
        product = Product.objects.all()
        cart = Savat(product_id_id=id)
        cart.save()
        return redirect('shop-detail')


class ProductDetailView(View):
    def get(self, request):
        savat = Savat.objects.all()
        return render(request, 'shop/shop-detail.html', {'savat': savat})


class CartView(View):
    def get(self, request):
        cards = Product.objects.all()
        context = {'cards': cards}
        return render(request, 'shop/cart.html', context)


class ContactView(View):
    def get(self, request):
        return render(request, 'shop/contact.html')
