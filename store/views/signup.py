from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self ,request):
        return render(request,'signup.html')
    
    def post(self, request):
        postData=request.POST
        firstname=postData.get('firstname')
        lastname=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')
            
        # validation
            
        value= {
            'firstname' : firstname,
            'lastname' : lastname,
            'phone' : phone,
            'email': email,
        }
        errormessage=None
        
        customer=Customer(first_name=firstname,last_name=lastname,phone=phone,email=email,password=password)
        errormessage=self.validateCustomer(customer)
    
        if not errormessage:
            print(firstname,lastname,phone,email,password)
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('homepage')
        
        else:
            data={"error" :errormessage,
                'values' : value,
                }
            return render(request, "signup.html", data)
    def validateCustomer(self,customer):
        errormessage=None
        if (not customer.first_name):
            errormessage="First Name Required !"
        elif len(customer.first_name) < 3:
            errormessage="First Name must be 3 character long or more"
        elif (not customer.last_name):
            errormessage="Last Name Required !"
        elif len(customer.last_name) < 3:
            errormessage="First Name must be 3 character long or more"
        elif not customer.phone:
            errormessage="Phone number requied"
        elif len(customer.phone) < 10:
            errormessage="Phone number must be 10 number long or more"
        elif len(customer.password) < 5:
            errormessage="Password must be 6 character long or more"
        elif len(customer.email) < 5:
            errormessage="Email must be 5 character long or more"
        # elif customer.isExists():
        #     errormessage="Email Address Already Registerd"

        return errormessage

        
