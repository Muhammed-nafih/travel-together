from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.db import connection


def Home(request):
	return render(request,"Home.html",{})

def Registration(request):
	if request.method == "POST":
		Name= request.POST['name']
		Age= request.POST['age']
		Address= request.POST['address']
		Phone= request.POST['phone']
		Email= request.POST['email']
		image = request.FILES['image']
		Username= request.POST['username']
		Password= request.POST['password']
		if userDetails.objects.filter(Username=Username).exists():
			messages.info(request,"Username already Taken")
			return redirect('/Registration')
		else:
			obj = userDetails(
			Name=Name
			,Age=Age
			,Phone=Phone
			,Email=Email
			,Address=Address
			,Image = image
			,Username=Username
			,Password=Password)
			obj.save()
			messages.info(request,"User Registered")
			return redirect('/User_Login')
	else:
		return render(request,"Registration.html",{})

def User_Login(request):
	if request.method == "POST":
		C_name = request.POST['aname']
		C_password = request.POST['apass']
		if userDetails.objects.filter(Username=C_name,Password=C_password).exists():
			users = userDetails.objects.all().filter(Username=C_name,Password=C_password)
			messages.info(request,C_name +' logged in')
			request.session['UserId'] = users[0].id
			request.session['type_id'] = 'User'
			request.session['UserType'] = C_name
			request.session['login'] = "Yes"
			return redirect('/')
		else:
			messages.info(request, 'Wrong Username or password')
			return redirect("/User_Login")
	else:
		return render(request,'User_Login.html',{})

def Profile(request):
	user_id = request.session['UserId']
	details = userDetails.objects.filter(id=user_id)
	return render(request,"Profile.html",{'details':details})

def UpdateProfile(request):
	return redirect('/Profile/')



def ChangePassword(request):
	Userid = request.session['UserId']
	if request.method == "POST":
		newpass = request.POST['new_pass']
		confirm = request.POST['confirm_pass']
		if newpass == confirm:
			userDetails.objects.filter(id=Userid).update(Password=newpass)
			messages.info(request,'Password changed')
			details = userDetails.objects.filter(id=Userid)
			return render(request,'ChangePassword.html',{'details':details})
		else:
			messages.info(request,'Passwords dont match')
			return redirect('/ChangePassword')
	else:
		Userid = request.session['UserId']
		details = userDetails.objects.filter(id=Userid)
		return render(request,'ChangePassword.html',{'details':details})

	return render(request,"ChangePassword.html",{})

def Manage_Groups(request):
	user_id = request.session['UserId']
	details = Groups.objects.filter(user_id=user_id)
	return render(request,"Manage_Groups.html",{'details':details})

def Add_Group(request):
	if request.method == "POST":
		user_id = request.session['UserId']
		Name = request.POST['name']
		Image = request.FILES['image']
		Description = request.POST['Description']
		Status = request.POST['Status']
		if Groups.objects.filter(Name = Name,user_id= user_id).exists():
			messages.info(request,"Group already exists")
			return redirect('/Manage_Groups/')
		else:
			obj = Groups(user_id=user_id,Name=Name,Image=Image,Description=Description,Status=Status)
			obj.save()
			messages.info(request,"Group Added")
			return redirect('/Manage_Groups/')
	else:
		return render(request,"Manage_Groups.html",{})


# def View_Groups(request):
# 	user_id = request.session['UserId']
# 	details = Groups.objects.exclude(user_id=user_id)
# 	user_requests = JoinRequest.objects.filter(user_id=user_id)
# 	return render(request,"View_Groups.html",{'details':details,'user_requests': user_requests})

def View_Groups(request):
    user_id = request.session['UserId']
    details = Groups.objects.exclude(user_id=user_id)
    user_requests = JoinRequest.objects.filter(user_id=user_id)
    group_ids_with_requests = user_requests.values_list('group_id', flat=True)

    group_data = []
    for group in details:
        join_request = None
        if group.id in group_ids_with_requests:
            join_request = user_requests.get(group_id=group.id)
        group_data.append({'group': group, 'join_request': join_request})

    return render(request, "View_Groups.html", {'group_data': group_data})

def Join(request,id):
	user_id = request.session['UserId']
	user = userDetails.objects.get(id=user_id)
	group = Groups.objects.get(id=id)
	data = JoinRequest.objects.filter(user=user_id,group=id)
	for i in data:
		ST = data[0].status
	if JoinRequest.objects.filter(user=user_id,group=id).exists():
		messages.info(request,"Your request is in process")
		return redirect('/View_Groups')
	else:
		obj = JoinRequest(user=user,group=group)
		obj.save()
		return redirect('/View_Groups')
	return render(request,"View_Groups.html",{'ST':ST})

def View_Members(request,id):
	print("YES")
	details = Member.objects.filter(group=id)
	return render(request,"View_Members.html",{'details':details})

def View_Request(request,id):
	details = JoinRequest.objects.filter(group=id)
	print(details)
	return render(request,"View_Request.html",{'details':details})


def Update_Status(request):
	if request.method == "POST":
		req_id = request.POST['req_id']
		group_id = request.POST['group_id']
		status = request.POST['status']
		user_id = request.POST['user_id']
		print("req_id "+str(req_id))
		print("group_id "+str(group_id))
		print("status "+str(status))
		print("user_id "+str(user_id))
		JoinRequest.objects.filter(id=req_id).update(status=status)
		user = userDetails.objects.get(id=user_id)
		group = Groups.objects.get(id=group_id)
		if status == "Approved":
			obj = Member(user=user,group=group)
			obj.save()
	return redirect('/View_Request/'+str(group_id))


def Delete_Group(request,id):
	Groups.objects.filter(id=id).delete()
	return redirect('Manage_Groups')


def View_Chat(request,id):
	details = Groups.objects.filter(id=id)
	data = Chat.objects.filter(group=id)
	return render(request,"View_Chat.html",{'details':details,'id':id,'data':data})

def Add_Comment(request):
	if request.method == "POST":
		group_id = request.POST['group_id']
		comment = request.POST['comment']
		user_id = request.session['UserId']
		user = userDetails.objects.get(id=user_id)
		group = Groups.objects.get(id=group_id)
		obj = Chat(user=user,group=group,comment=comment)
		obj.save()
	return redirect('/View_Chat/'+str(group_id))


def Update_Group(request):
    if request.method == "POST":
        group_id = request.POST['updateid']
        user_id = request.POST['updateprice']
        group_name = request.POST['updatename']
        details = Groups.objects.filter(id=group_id)
        for i in details:
            image1 = details[0].Image
        uploaded_image = request.FILES.get('image', image1)
        print(uploaded_image)
        Image = "GroupImages/" + str(uploaded_image)
        description = request.POST['updatestate']
        description = description.strip()
        status = request.POST['Status']
        Groups.objects.filter(id=group_id).update(user_id=user_id, Name=group_name, Description=description, Status=status, Image=Image)
        file_path = 'C:/Python Projects/TravelTogether/media/' + str(Image)
        with open(file_path, 'wb') as file:
            file.write(uploaded_image.read())
    return redirect('/Manage_Groups')



def Logout(request):
    Session.objects.all().delete()
    return redirect("/")
