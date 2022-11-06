from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_list_or_404
from django.views import View
from . import forms, models
from .models import ContactUs
from .models import Products
from django.contrib.auth import logout



# Create your views here.
def home(request):
    return render(request,'base.html')

# def homepage(request):
#     return redirect ('base.html')


class Login(View):
    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        unm = request.POST['unm']
        pwd = request.POST['pass']
        userdata = models.Registration.objects.filter(username__exact=unm).filter(pswrd__exact=pwd)
        if userdata:
            for i in userdata:
                request.session['username'] = i.username
                request.session['fullname'] = i.firstname + " " + i.lastname
            return redirect('/')
        else:
            return HttpResponse("Error in Login....")

def products(request):
    produc = models.Products.objects.all()
    context = {'products':produc}
    return render(request,'products.html',context)

def showContactUs(request):
    return render(request,'contact.html')


def ContactUs(request):
    if request.method == 'GET':
        return HttpResponse('get method of contact us')
    
    elif request.mothod == "POST":
        c_name = request.POST['c_name']
        c_email = request.POST['c_email']
        c_mobile = request.POST['c_mobile']
        c_message = request.POST['c_message'] 
        c_save = ContactUs(c_name=c_name,c_email=c_email,c_mobile=c_mobile,c_message=c_message)
        c_save.save()
        return HttpResponse('Done.....')
    else:
        return HttpResponse('Error....!!!!')

# class Contact(View):
#     def get(self,request):
#         myform = forms.ContactUsForm
#         return render(request,'contact.html',{"myform":myform})

#     def post(self,request):
#         # c_name = request.POST['c_name']
#         # c_email = request.POST['c_email']
#         # c_mobile = request.POST['c_mobile']
#         # c_message = request.POST['c_message']
#         # c_s = 

#         myform = forms.ContactUsForm(request.POST)
#         if myform.is_valid():
#             fname = myform.cleaned_data['firstname']
#             lname = myform.cleaned_data['lastname']
#             email = myform.cleaned_data['email']
#             mobile = myform.cleaned_data['mobile']
#             quaries = myform.cleaned_data['quaries']
#             s = models.ContactUs(fname,lname,email,mobile,quaries)
#             s.save()
#             return redirect('/')

#         else:
#             return HttpResponse("Could not save the data....")
def about(request):
    return render(request,'about.html')


def cart(request):
    return render(request,'mycart.html')

class Register(View):
    def get(self, request):
        myform = forms.RegistrationForm
        return render(request,'register.html', {"myform": myform})
    def post(self,request):
        myform = forms.RegistrationForm(request.POST)
        if myform.is_valid():
            uname = myform.cleaned_data['username']
            fname = myform.cleaned_data['firstname']
            lname = myform.cleaned_data['lastname']
            email = myform.cleaned_data['email']
            mobile = myform.cleaned_data['mobile']
            ct = myform.cleaned_data['city']
            cntry = myform.cleaned_data['country']
            pwd = myform.cleaned_data['pswrd']
            utype = myform.cleaned_data['usertype']
            f = models.Registration(uname,fname,lname,email,mobile,ct,cntry,pwd,utype)
            f.save()
            return redirect('/')

        else:
            return HttpResponse("Error...")

def myLogout(request):
    logout(request)
    return redirect('/')

class ProductCategory(View):
    def get(self,request):
        myform1 = forms.ProductCategoryForm
        return render(request,'addproduct.html',{"myform1":myform1})
    def post(self,request):
        myform1 = forms.ProductCategoryForm(request.POST)
        if myform1.is_valid():
            pcid = myform1.cleaned_data['product_cid']
            pctg = myform1.cleaned_data['product_category']
            f = models.Registration(pcid,pctg)
            f.save()
            return redirect('/')
class Product(View):
    def get(self,request):
        # myform1 = forms.ProductCategoryForm
        myform2 = forms.ProductForm
        return render(request,'addproduct.html',{"myform2":myform2,})
    def post(self,request):
        myform2 = forms.ProductForm(request.POST)
        if myform2.is_valid():
            pid = myform2.cleaned_data['product_id']
            pnm = myform2.cleaned_data['product_name']
            pdsc = myform2.cleaned_data['product_description']
            pprc = myform2.cleaned_data['product_price']
            pimg = myform2.cleaned_data['image']
            # pcid = str(myform2.cleaned_data['pc_id'])
            # pmfg = myform2.cleaned_data['product_mfg']
            f = models.Registration(pid,pnm,pdsc,pprc,pimg,)
            f.save()
            return redirect('/')
        else:
            return HttpResponse("Error in submit")
