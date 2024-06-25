from django.shortcuts import render,redirect
from django.contrib import messages
from . models import register1,profile1,work1,requestsdata,contact1,endwork1,requestsdataforenduser,LFEEDBACK
# Create your views here.
def index(request):
    return render(request,'index.html')

def index4(request):
    return render(request,'index4.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    getdata = work1.objects.all()
    fetchdata = endwork1.objects.all()
    context = {
        'condetails': getdata,
        'enddetails':fetchdata
    }
    return render(request, 'blog.html',context)

def blog_details(request , id):
    getdata = work1.objects.get(id=id)
    context = {
        'pridetails': getdata
    }
    return render(request, 'blog-details.html',context)

def blog_detailsss(request , id):
    getdata = endwork1.objects.get(id=id)
    context = {
        'pridetails': getdata

    }
    return render(request, 'blog-details.html',context)

def blog_detailssforend(request , id):
    getdata = endwork1.objects.get(id=id)
    context = {
        'pridetails': getdata

    }
    return render(request, 'endusersingle.html',context)

def applyforwork(request,id):
    uid = request.session['logid']
    insertdetails = requestsdata(workid=work1(id=id),labourid=register1(id=uid),status=0)
    insertdetails.save()
    # messages.success(request,"you have applied for work. wait for confirmation.")
    return render(request,"index-2.html")

def applyforworkforenduser(request,id):
    uid = request.session['logid']
    insertdetails = requestsdataforenduser(workid=endwork1(id=id),labourid=register1(id=uid),status=0)
    insertdetails.save()
    messages.success(request,"you have applied for work. wait for confirmation.")
    return render(request,"index-3.html")



def blog_one_column(request):
    return render(request, 'blog-one-column.html')

def blog_two_column(request):
    return render(request, 'blog-two-column.html')

def contact(request):
    return render(request, 'contact.html')

def contact_fetchdata(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        insertdata = contact1(name=name, email=email,subject=subject,message=message)
        insertdata.save()
        messages.success(request, "data inserted")
        return render(request, "index.html")
    else:
        pass
    return render(request,"contact.html")

def index(request):
    try:
        uid = request.session["logid"]
        # if uid is None:
        #        print("no session")
        #        return render(request,"login.html")
        # else:
        #        return render(request,"index.html")
    except:
        return render(request, 'login-register.html')
    return render(request, 'index.html')


def index_2(request):
    return render(request, 'index-2.html')

def index_3(request):
    return render(request, 'index-3.html')

def login_register(request):
    return render(request, 'login-register.html')

def register(request):
    return render(request, 'register.html')

def workupload(request):
    return render(request, 'workupload.html')

def workupload1(request):
    if request.method == 'POST':
        cid = request.session["logid"]
        cname = request.POST.get("name")
        cphone = request.POST.get("phone")
        cLoction = request.POST.get("Loction")
        ctype_of_labour = request.POST.get("type_of_labour")
        cNo_Of_Labour = request.POST.get("No_Of_Labour")
        cexp = request.POST.get("exp")
        cWorking_Hour = request.POST.get("Working_Hour")
        cDaily_Labour_Charge = request.POST.get("Daily_Labour_Charge")
        cimage = request.FILES["work_image"]
        cmessage = request.POST.get("message")

        insertdata = work1(userid=register1(id=cid),name=cname,phone=cphone, location=cLoction, types_of_labour=ctype_of_labour,no_of_labour=cNo_Of_Labour,exp=cexp,Working_Hour=cWorking_Hour,income_per_day=cDaily_Labour_Charge,img=cimage,message=cmessage)
        insertdata.save()
        # messages.success(request, "data inserted click on back to home and view uploaded work and work request by clicking on Request : )")
        return render(request, "index.html")

    else:
        pass
    return render(request, "workupload.html")

def fetchdata(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        uemail = request.POST.get("uemail")
        uphone = request.POST.get("uphone")
        upass = request.POST.get("upass")
        uadd = request.POST.get("uadd")
        type_of_user=request.POST.get("type_of_user")

        insertdata = register1(name=uname, email=uemail, phone=uphone, password=upass, address=uadd,type_of_user=type_of_user)
        insertdata.save()
        messages.success(request, "data inserted")
        return render(request, "login-register.html")
    else:
        pass
    return render(request, "register.html")


def checkdata(request):
    if request.method == 'POST':
        uemail = request.POST.get("uemail")
        upass = request.POST.get("upass")
        try:
            userdetails = register1.objects.get(email=uemail, password=upass)
            request.session['logid'] = userdetails.id
            request.session['logname'] = userdetails.name
            request.session.save()

        except:
            userdetails = None


        if userdetails is not None:
            # messages.success(request,"correct details")
            if userdetails.type_of_user=="Contractor":
             return render(request, "index.html")
            if userdetails.type_of_user=="Labour":
             return render(request, "index-2.html")
            if userdetails.type_of_user=="End-User":
             return render(request, "index-3.html")

        else:
            messages.error(request, "data incorrect")
    else:
        pass
        return render(request, "index.html")

def enduser(request):
    return render(request, 'enduser.html')


def logout(request):
    try:
        del request.session["logid"]
        del request.session["logname"]
    except:
        pass
    return render(request,"login-register.html")

def contractor(request):
    return render(request, 'contractor.html')

def labour(request):
    return render(request, 'labour.html')


def profile(request):
    return render(request, 'profile.html')

def profetchdata(request):
    if request.method == 'POST':
        uid = request.session["logid"]
        Pname = request.POST.get("pname")
        Pphone = request.POST.get("pphone")
        Pemail = request.POST.get("pemail")
        Pexp = request.POST.get("pexp")
        Padd = request.POST.get("padd")
        Pdes = request.POST.get("pdes")
        Pimg = request.FILES["pimg"]
        insertdata = profile1(name=Pname,userid=register1(id=uid), phone=Pphone,email=Pemail,exp=Pexp,address=Padd,des=Pdes,img=Pimg)
        insertdata.save()
        messages.success(request, "data inserted click on back to home and view profie : )  ")

    else:
        pass
    return render(request,'profile.html')

def view_profile(request):
    uuid = request.session["logid"]
    getdata = profile1.objects.get(userid=uuid)
    context = {
        'prodata':getdata
    }
    return render(request, "view_profile.html",context)

def cviewprofile(request,vid):
    uuid = request.session["logid"]
    getdata = profile1.objects.get(userid=vid)
    context = {
        'prodata':getdata
    }
    return render(request, "view_profile.html",context)

def projects_one(request):
    return render(request, 'projects-one.html')

def projects_three(request):
    return render(request, 'projects-three.html')

def projects_two(request):
    return render(request, 'projects-two.html')

def service(request):
    return render(request, 'service.html')

def single_project(request):
    return render(request, 'single-project.html')

def single_service(request):
    return render(request, 'single-service.html')

def con_request(request):
    uid = request.session["logid"]
    getdata = work1.objects.filter(userid=uid)
    context = {
        'appdetails': getdata
    }
    return render(request, 'con_request.html',context)

def con_accept(request):
    return render(request, 'con_accept.html')




def end_workupload(request):
    return render(request, 'end_workupload.html')

def end_workupload1(request):
    if request.method == 'POST':
        eid=request.session["logid"]
        cname = request.POST.get("name")
        cphone = request.POST.get("phone")
        cLoction = request.POST.get("Loction")
        ctype_of_labour = request.POST.get("type_of_labour")
        #cNo_Of_Labour = request.POST.get("No_Of_Labour")
        cexp = request.POST.get("exp")
        cWorking_Hour = request.POST.get("Working_Hour")
        cDaily_Labour_Charge = request.POST.get("Daily_Labour_Charge")
        cimage = request.FILES["work_image"]
        cmessage = request.POST.get("message")

        insertdata = endwork1(userid=register1(id=eid),name=cname,phone=cphone, location=cLoction, types_of_labour=ctype_of_labour,no_of_labour=1,exp=cexp,Working_Hour=cWorking_Hour,income_per_day=cDaily_Labour_Charge,img=cimage,message=cmessage)
        insertdata.save()
        messages.success(request, "data inserted")
        return render(request, "index-3.html")
    else:
        pass
    return render(request, "end_workupload.html")

def acceptwork(request,aid):
    data=requestsdata.objects.get(id=aid)
    print(data.save)
    data.status="1"
    data.save()
    # messages.success(request,"REQUEST ACCEPTED")
    return redirect(con_request)

def rejecttwork(request,aid):
    data=requestsdata.objects.get(id=aid)
    print(data.save)
    data.status="2"
    data.save()
    # messages.success(request,"REQUEST ACCEPTED")
    return redirect(con_request)

def endacceptwork(request,aid):
    data=requestsdataforenduser.objects.get(id=aid)
    print(data.save)
    data.status="1"
    data.save()
    # messages.success(request,"REQUEST ACCEPTED")
    return redirect(end_request)

def endrejecttwork(request,aid):
    data=requestsdataforenduser.objects.get(id=aid)
    print(data.save)
    data.status="2"
    data.save()
    # messages.success(request,"REQUEST ACCEPTED")
    return redirect(end_request)

def con_accept(request,cid):
    uid = request.session["logid"]
    getdata = requestsdata.objects.filter(workid=cid)
    context = {
        'details': getdata
    }
    return render(request, 'con_accept.html',context)

def lab_request(request):
    uid = request.session["logid"]
    getdata = requestsdata.objects.filter(labourid=uid)
    getdata1 = requestsdataforenduser.objects.filter(labourid=uid)
    context = {
        'workapply': getdata,
        'workapply2': getdata1
    }
    return render(request, 'lab_request.html',context)
# def lab_request2(request):
#     uid = request.session["logid"]
#
#     print(getdata)
#     context = {
#         'workapply2': getdata
#     }
#     return render(request, 'lab_request.html',context)
def eviewprofile(request,eid):
    uuid = request.session["logid"]
    getdata = profile1.objects.get(userid=eid)
    context = {
        'pridata':getdata
    }
    return render(request, "view_profile.html",context)

def end_accept(request,endid):
    uid = request.session["logid"]
    getdata = requestsdataforenduser.objects.filter(workid=endid)
    context = {
        'enddetails': getdata
    }
    return render(request, 'end_accept.html',context)

def end_request(request):
    uid = request.session["logid"]
    getdata = endwork1.objects.filter(userid=uid)
    context = {
        'enddata': getdata
    }
    return render(request,'end_request.html',context)

def lfeedback(request,lid):

    context={
        "lid":lid
    }
    return render(request, 'feedback.html',context)

def addlfeedback(request):
    if request.method=="POST":
        lname = request.session['logname']
        flid=request.POST.get("flid")
        cmnt=request.POST.get("comment")
        rating=request.POST.get("input-1")
        insertdetails = LFEEDBACK(Labour_name=lname,C_ID_id=flid,COMMENT=cmnt,RATING=rating)
        insertdetails.save()
        messages.success(request, "THANKS FOR YOUR RESPONSE")
    else:
        messages.error(request, "CANT ADD FEEDBACK")
    return render(request,"index-2.html")

def feedback(request):
    return render(request,"feedback.html")


def viewconfeedback1(request):
    uid = request.session["logid"]
    getdata = LFEEDBACK.objects.filter(C_ID_id=uid)
    print(getdata)
    context = {
        'feeddetails': getdata
    }
    return render(request, 'viewconfeedback.html', context)