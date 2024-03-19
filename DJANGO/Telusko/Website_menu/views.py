from django.shortcuts import render

from .models import Destination

# Create your views here.
def index(request):
    # dest1 = Destination()
    # dest1.id = 123
    # dest1.name = "Bali"
    # dest1.discription = "It's good place"
    # dest1.price = 1100000
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.id = 124
    # dest2.name = "Mumbai"
    # dest2.discription = "People don't sleep"
    # dest2.price = 10000
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.id = 125
    # dest3.name = "Indonesia"
    # dest3.discription = "It's gods of island"
    # dest3.price = 1500000
    # dest3.offer = False

    # dest = [dest1,dest2,dest3]


    dest = Destination.objects.all()
    return render(request,'index.html',{'dests':dest})
