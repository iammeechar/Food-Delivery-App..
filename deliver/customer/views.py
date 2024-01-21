from django.shortcuts import render

# Create your views here.
from django.views import View
#create an index view to handle any get requests.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')#render html template
    
class About(View):
     def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')#render in the about page

class Order(View):
    def get(self, request, *args, **kwargs):
        
        #get each item from each category
        appetizers = MenuItems.objects.filter(category__name__contains='Appetizer')
        entres = MenuItems.objects.filter(category__name__contains='Entre')
        desserts = MenuItems.objects.filter(category__name__contains='Dessert')
        drinks = MenuItems.objects.filter(category__name__contains='Drink')
        #pass into context
        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,

        }

        #render the template
        return render(request, 'Customer/order.html ')
    
    def post(self, request, *args, **kwargs):
        order_items ={
            'items':[]
        }

        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItems.objects.get(pk__containts= int(item))
            item_data = {
                'id':menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }