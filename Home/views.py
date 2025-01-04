from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Home/register.html', {'form': form})

def home(request):
    return render(request, 'Home/home.html')


def menu(request):
    menu_data = {
        "Appetizers": [
            {"name": "Spring Rolls", "description": "Crispy rolls with a savory filling.", "price": 5.99, "image_url": "https://via.placeholder.com/300"},
            {"name": "Garlic Bread", "description": "Toasted bread with garlic and herbs.", "price": 4.99, "image_url": "https://via.placeholder.com/300"},
        ],
        "Main Course": [
            {"name": "Grilled Salmon", "description": "Fresh salmon grilled to perfection.", "price": 14.99, "image_url": "https://via.placeholder.com/300"},
            {"name": "Steak", "description": "Juicy steak served with sides.", "price": 19.99, "image_url": "https://via.placeholder.com/300"},
        ],
        "Desserts": [
            {"name": "Cheesecake", "description": "Rich and creamy cheesecake.", "price": 6.99, "image_url": "https://via.placeholder.com/300"},
            {"name": "Brownie", "description": "Chocolate brownie with ice cream.", "price": 5.99, "image_url": "https://via.placeholder.com/300"},
        ],
        "Beverages": [
            {"name": "Coffee", "description": "Freshly brewed coffee.", "price": 2.99, "image_url": "https://via.placeholder.com/300"},
            {"name": "Lemonade", "description": "Refreshing lemonade.", "price": 3.99, "image_url": "https://via.placeholder.com/300"},
        ],
    }
    return render(request, 'Home/menu.html', {'menu': menu_data})

def about(request):
    return render(request, 'Home/about.html')

@login_required
def contact(request):
    return render(request, 'Home/contact.html')
