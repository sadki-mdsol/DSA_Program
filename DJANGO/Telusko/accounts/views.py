from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email_id = request.POST['email_id']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists() or User.objects.filter(email=email_id).exists():
                messages.info(request,"")
                print("User already existis with username or email........")
            else:
                user = User.objects.create_user(username=user_name,first_name= first_name,last_name=last_name,email = email_id,password=password1)
                user.save()
                print('USer Created')
        else:
            print('passwprd incorrect')
        return redirect('/')
    else:
        return render(request,'register.html')