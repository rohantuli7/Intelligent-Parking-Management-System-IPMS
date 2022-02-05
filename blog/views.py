from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import userdata, finedata
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from .alpr import main
from .forms import number_images


def home(request):
    return render(request, 'blog/home.html', )


def index(request):
    u = request.user.username
    x = main()
    return render(request, 'blog/index.html', context={'username': x})


def register(request):
    if request.method == 'POST':
        email1 = request.POST.get('email', False)
        number_plate = request.POST.get('number_plate', False)
        username1 = request.POST.get('username', False)
        fname1 = request.POST.get('fname', False)
        password1 = request.POST.get('pass', False)
        repassword1 = request.POST.get('re', False)
        lname1 = request.POST.get('lname', False)
        designation1 = request.POST.get('desg', False)
        cp1 = request.POST.get('cp', False)
        address1 = request.POST.get('addr', False)
        pincode1 = request.POST.get('pin', False)
        contactno1 = request.POST.get('cont', False)
        u = userdata(email=email1, number_plate=number_plate, username=username1, fname=fname1, password=password1,
                     repassword=repassword1, lname=lname1, designation=designation1, cp=cp1, address=address1,
                     pincode=pincode1,
                     contactno=contactno1)
        u.save()
        user = User.objects.create_user(username=username1, email=email1, password=password1)
        user.save()

        send_mail('Registration Successful',
                  'Dear User,\n\t Welcome! You have successfully been registered. ',
                  'settings.EMAIL_HOST_USER',
                  [email1],
                  fail_silently=False,
                  )
        return redirect("blog-login")
    return render(request, 'blog/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('user', False)
        password = request.POST.get('pass1', False)

        v = auth.authenticate(username=username, password=password)

        if v is not None:
            auth.login(request, v)
            if username == 'Aakansh':
                return redirect('/adminhome')
            else:
                return redirect('/userhome')

        else:
            return redirect('blog-register')
    return render(request, 'blog/login.html')


def page1(request):
    x = main()
    return render(request, 'blog/page1.html', context={'username': x})


def contact(request):
    return render(request, 'blog/contact.html')


def alpr(request):
    if request.method == 'POST':
        name = request.POST.get('fname', False)
        fine = request.POST.get('fine', False)
        x = main()
        a = finedata(name=name, fine=fine, numberplate=x)
        a.save()

        return redirect('/adminhome')
    return render(request, 'blog/alpr.html')


def fine_history(request):
    return render(request, 'blog/fine_history.html')


def current_fine(request):
    u = request.user.username
    if finedata.objects.filter(name=u).exists():
        f = finedata.objects.get(name=u).fine
    else:
        return redirect('/current_fine1')

    if request.method == 'POST':
        return redirect('/payment')

    return render(request, 'blog/current_fine.html', context={'username': u, 'fine': f})


def adminhome(request):
    u = request.user.username
    return render(request, 'blog/adminhome.html', context={'username': u})


def userhome(request):
    u = request.user.username
    return render(request, 'blog/userhome.html', context={'username': u})


def current_fine1(request):
    return render(request, 'blog/current_fine1.html')


def payment(request):
    return render(request, 'blog/payment.html')


def fine_upload1(request, obj):
    p = get_object_or_404(finedata, name=obj)
    x = main(p.image.path)
    p.numberplate = x
    p.save()
    print(".............................................")
    return redirect('/login')

def fine_upload(request):
    y = ''
    if request.method == 'POST':
        form = number_images(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.numberplate = ''
            instance.save()
            return redirect('/upload1/' + instance.name)
        else:
            return render(request, 'blog/alpr.html', {'form': form})
    else:
        form = number_images()
    return render(request, 'blog/alpr.html', {'form': form})
