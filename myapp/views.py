from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.forms import TodoListModelForm,RegistrationForm,LoginForm
from myapp.models import TodoList
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib .auth import authenticate,login,logout
from django.contrib import messages
from myapp.decorators import signin_required
from django.utils.decorators import method_decorator
import datetime

# Create your views here.
@method_decorator(signin_required,name="dispatch")
class TodoListCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=TodoListModelForm()

        qs=TodoList.objects.filter(user_object=request.user)

    

        return render(request,"todolist_create.html",{"form":form_instance,"data":qs})
    
    def post(self,request,*args,**kwargs):

        form_instance=TodoListModelForm(request.POST)

        if form_instance.is_valid():

            form_instance.instance.user_object=request.user

            form_instance.save()

            messages.success(request,"todolist created")

            return redirect("todolist-create")
        
        else:
            
            messages.error(request,"todolist not created")

            return render(request,"todolist_create.html",{"form":form_instance})

@method_decorator(signin_required,name="dispatch")        
class TodoListUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        todolist_object=TodoList.objects.get(id=id)

        form_instance=TodoListModelForm(instance=todolist_object)


        return render(request,"todolist_update.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        todolist_object=TodoList.objects.get(id=id)

        form_instance=TodoListModelForm(instance=todolist_object,data=request.POST)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"todolist updated")

            return redirect("todolist-create")
        
        else:

            messages.error(request,"todolist not updated")

            return render(request,"todolist_update.html",{"form":form_instance})
        
@method_decorator(signin_required,name="dispatch")
class TodoListDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=TodoList.objects.get(id=id)

        return render(request,"todolist_detail.html",{"data":qs})
    
@method_decorator(signin_required,name="dispatch")
class TodoListDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        TodoList.objects.get(id=id).delete()

        messages.success(request,"todolist deleted")

        return redirect("todolist-create") 

class SignUpView(View):

    def get(self,request,*args,**kwargs):

        form_instance=RegistrationForm()

        return render(request,"register.html",{"form":form_instance}) 

    def post(self,request,*args,**kwargs):

        form_instance=RegistrationForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data) 

            return redirect("signin")

        else:

            return redirect("register")

class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=LoginForm()

        return render(request,"login.html",{"form":form_instance})    

    def post(self,request,*args,**kwargs):

        form_instance=LoginForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                return redirect("todolist-create")
        messages.error(request,"invalid credential") 
           
        return render(request,"login.html",{"form":form_instance})

@method_decorator(signin_required,name="dispatch")        
class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")

        


    






                

