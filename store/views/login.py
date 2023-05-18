from django.shortcuts import render, redirect,HttpResponsePermanentRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View

class Login(View):
    return_url=None
    def  get(self, request):
        Login.return_url=request.GET.get('return_url')
        return render(request,'login.html')

    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        errormessage=None
        # print(customer)
        if customer:
            flat=check_password(password , customer.password)
            if flat:
                request.session['customer']=customer.id
                
                if Login.return_url:
                    return HttpResponsePermanentRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('homepage')
            else:
                errormessage="Email or Password invalid !! "
        else:
            errormessage="Email or Password invalid !! "
        print(email,password)
        return render(request,'login.html',{'error': errormessage})
    
def logout(request):
    request.session.clear()
    return redirect('login')

        