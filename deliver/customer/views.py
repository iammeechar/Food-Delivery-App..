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
        appetizers = MenuItems.objects.filter(category_name_contains='Appetizer')
        entres = MenuItems.objects.filter(category_name_contains='Entre')
        desserts = MenuItems.objects.filter(category_name_contains='Desserts')
        drinks = MenuItems.objects.filter(category_name_contains='Drinks')
        #pass into context
        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,

        }

        #render the template