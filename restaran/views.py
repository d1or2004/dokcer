from django.shortcuts import render, redirect
from .models import MasterChef, FoodMenu, TableOnline, Testimonial, Contact, ProductType, Costumer, Mahsulot
from django.views import View
from shop.models import Product


class LandingView(View):
    def get(self, request):
        menus = FoodMenu.objects.all()
        tables = TableOnline.objects.all()
        chefs = MasterChef.objects.all()
        costumer = Costumer.objects.all()
        testimonial = Testimonial.objects.all()

        return render(request, "main/index.html", context={
            "menus": menus,
            "tables": tables,
            "chefs": chefs,
            "costumer": costumer,
            "testimonial": testimonial
        })

    def post(self, request):
        ism = request.POST['ism']
        email = request.POST['email']
        date_time = request.POST['data_time']
        number_of_people = request.POST['number_of_people']
        requests = request.POST['requests']
        menu = TableOnline(ism=ism, email=email, date_time=date_time, number_of_people=number_of_people,
                           requests=requests)
        menu.save()
        return redirect('landing')


class AboutView(View):
    def get(self, request):
        chefs = MasterChef.objects.all()
        return render(request, "main/about.html", context={"chefs": chefs})


class ServicesView(View):
    def get(self, request):
        return render(request, "main/service.html")


class MenuView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            foodmenus = FoodMenu.objects.all()
            return render(request, "main/menu.html", context={"foodmenus": foodmenus})
        else:
            foodmenus = FoodMenu.objects.filter(title__icontains=search)
            if foodmenus:
                return render(request, "main/menu.html", context={"foodmenus": foodmenus})
            else:
                return render(request, "main/menu.html", context={"foodmenus": foodmenus})


class MunuDetailView(View):
    def get(self, request, id):
        producttype = ProductType.objects.get(id=id)
        return render(request, "main/munu.html", context={"producttype": producttype})


class TableOnlineView(View):
    def get(self, request):
        tables = TableOnline.objects.all()
        return render(request, "main/table.html", context={"tables": tables})

    # def post(self, request):
    #     tables = TableOnline.objects.all()


class BookTableOnlineView(View):
    def get(self, request):
        return render(request, "main/booking.html")

    # def post(self, request):
    #     ism = request.POST['ism']
    #     email = request.POST['email']
    #     date_time = request.POST['data_time']
    #     number_of_people = request.POST['number_of_people']
    #     requests = request.POST['requests']
    #     menu = TableOnline(ism=ism, email=email, date_time=date_time, number_of_people=number_of_people,
    #                        requests=requests)
    #     menu.save()
    #     return redirect('booktableonline')


class OurTeamView(View):
    def get(self, request):
        team = MasterChef.objects.all()
        return render(request, "main/team.html", context={"team": team})


class TestimonialView(View):
    def get(self, request):
        testimonial = Testimonial.objects.all()
        return render(request, "main/testimonial.html", context={"testimonial": testimonial})


class ContactView(View):
    def get(self, request):
        return render(request, "main/contact.html")

    def post(self, request):
        first_name = request.POST['first_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(first_name=first_name, email=email, subject=subject, message=message)
        contact.save()
        return redirect('contact')


class ProductDetailView(View):
    def get(self, request, id):
        product = FoodMenu.objects.get(id=id)
        return render(request, "main/product_detail.html", context={"product": product})


class ProductUpdateView(View):
    def get(self, request, id):
        product = FoodMenu.objects.get(id=id)
        return render(request, "main/product_update.html", context={"product": product})

    def post(self, request, id):
        product = FoodMenu.objects.get(id=id)
        new_title = request.POST['title']
        new_description = request.POST['description']
        new_price = request.POST['price']
        new_price_type = request.POST['price_type']

        product.title = new_title
        product.description = new_description
        product.price = new_price
        product.price_type = new_price_type
        product.save()
        return redirect('landing')


class DeleteProductView(View):
    def get(self, request, id):
        product = FoodMenu.objects.get(id=id)
        product.delete()
        return redirect('landing')


class InsertView(View):
    def get(self, request):
        foodmenus = FoodMenu.objects.all()
        return render(request, "main/insert.html", context={"foodmenus": foodmenus})
