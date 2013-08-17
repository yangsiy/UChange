# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.context_processors import csrf
from django.contrib.auth.models import User

from uchange_app.models import Item,Person,Request,Deal,Control,Comment

def item_detail(request,item_id):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    stu=get_object_or_404(Person,student_id=student_id)
    item=get_object_or_404(Item, pk=item_id)
    p=get_object_or_404(Person,item_now=item)
    reques=1
    self=0
    accept=0
    if stu.item_now.id==item.id:
        self=1
        reques=0
    req=Request.objects.filter(item=stu.item_now)
    for each in req:
        if each.person==p:
            accept=1
            self=0
            reques=0
    if Request.objects.filter(person=stu,item=item):
        reques=0
        self=0
        accept=0
    req=Request.objects.filter(item=item)
    com=Comment.objects.filter(item=item)
    return render(request,'uchange_app/detail.html',{'user':student_id,'item':item,'request':reques,'self':self,'accept':accept,'owner':p,'count':req.count,'comments':com})

def item_history(request,item_id):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    item=get_object_or_404(Item,pk=item_id)
    deals=Deal.objects.filter(item=item).order_by('deal_time')
    if deals:
        last=Deal.objects.filter(item=item).order_by('-deal_time')[0]
    else:
        last=0
    return render(request,'uchange_app/item_history.html',{'user':student_id,'item':item,'deals':deals,'last':last})

def item_list(request):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    stu=get_object_or_404(Person,student_id=student_id)
    items=Item.objects.all()
    rtn=[]
    for each in items:
        if stu.item_now!=each and each.name!="request_add_item":
            rtn.append(each)
    return render(request,'uchange_app/item_list.html',{'user':student_id,'items':rtn})

def self(request):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    t=Person.objects.filter(student_id=student_id)
    if not t:
        return HttpResponseRedirect("/home/init/")
    if t[0].item_now.name=="request_add_item":
        return HttpResponseRedirect("/home/init_item/")
    info=get_object_or_404(Person, student_id=student_id)
    requests=Request.objects.filter(item=info.item_now)
    myrequests=Request.objects.filter(person=info)

    if info.item_now==info.item_original:
        edit_flag=1
    else:
        edit_flag=0
    
    return render(request,'uchange_app/self.html',{'user':student_id,'info':info,'number_of_requests':requests.count,'number_of_myrequests':myrequests.count,'edit_flag':edit_flag})

def profile(request,visit_id):
    student_id=request.user.username
    if student_id==visit_id:
        return self(request)
    else:
        info=get_object_or_404(Person,student_id=visit_id)
        return render(request,'uchange_app/profile.html',{'user':student_id,'info':info})

def person_history(request,visit_id):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    stu=get_object_or_404(Person,student_id=visit_id)
    deals=Deal.objects.filter(p2=stu).order_by('deal_time')
    return render(request,'uchange_app/person_history.html',{'user':student_id,'stu':stu,'deals':deals})

def request(request,item_id):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    stu=get_object_or_404(Person, student_id=student_id)
    it=get_object_or_404(Item, pk=item_id)
    if Request.objects.filter(person=stu,item=it):
        #return HttpResponse("You have requested already!")
        return item_detail(request,item_id)
    else:
        req=Request(person=stu,item=it)
        req.save()
        #return HttpResponse("Request has been sent successfully!")
        return item_detail(request,item_id)

def request_list(request):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    stu=get_object_or_404(Person, student_id=student_id)
    requests=Request.objects.filter(item=stu.item_now)
    return render(request,'uchange_app/request_list.html',{'user':student_id,'requests':requests})

def myrequest(request):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    stu=get_object_or_404(Person,student_id=student_id)
    requests=Request.objects.filter(person=stu)
    return render(request,'uchange_app/myrequest.html',{'user':student_id,'items':requests})

def accept(request,item_id):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    it=get_object_or_404(Item,id=item_id)
    p=get_object_or_404(Person,item_now=it)
    req=Request.objects.filter(person=p)
    p=get_object_or_404(Person,student_id=student_id)
    it=get_object_or_404(Item,id=p.item_now.id)
    req=req.filter(item=it)
    if not req:
        return HttpResponse("You cannot accept the one who didn't send request!")
    else:
        stu1=get_object_or_404(Person,student_id=student_id)
        stu2=get_object_or_404(Person,student_id=req[0].person.student_id)
        d1=Deal(item=stu1.item_now,p1=stu1,p2=stu2,deal_time=timezone.now())
        d1.save()
        d2=Deal(item=stu2.item_now,p1=stu2,p2=stu1,deal_time=timezone.now())
        d2.save()
        tmp=stu1.item_now
        stu1.item_now=stu2.item_now
        stu2.item_now=tmp
        stu1.save()
        stu2.save()
        req=Request.objects.filter(person=stu1)
        for each in req:
            each.delete()
        req=Request.objects.filter(person=stu2)
        for each in req:
            each.delete()
        #return HttpResponse("Exchange Successfully.")
        return item_detail(request,item_id)

def result(request):
    student_id=request.user.username
    stu=get_object_or_404(Person,student_id=student_id)
    if stu.item_original==stu.item_now:
        flag=1
    else:
        flag=0
    give=get_object_or_404(Person,item_now=stu.item_original)
    get=get_object_or_404(Person,item_original=stu.item_now)
    return render(request,'uchange_app/result.html',{'user':student_id,'stu':stu,'give':give,'get':get,'flag':flag})

def init(request):
    student_id=request.user.username
    user=request.user
    item=Item.objects.filter(name="request_add_item")
    stu=Person(student_id=user.username,first_name=user.first_name,last_name=user.last_name,email=user.email,item_now=item[0],item_original=item[0])
    stu.save()
    return HttpResponseRedirect("/home/init_item/")

def init_item(request):
    return render(request,'uchange_app/init_item.html')

def init_item_operate(request):
    student_id=request.user.username
    stu=get_object_or_404(Person,student_id=student_id)
    c={}
    c.update(csrf(request))
    name=request.POST['name']
    description=request.POST['description']
    item=Item(name=name,description=description)
    item.save()
    stu.item_now=item
    stu.item_original=item
    stu.save()
    return HttpResponseRedirect("/home/")

def edit_item(request):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    stu=Person.objects.filter(student_id=student_id)
    item=stu[0].item_original
    return render(request,'uchange_app/edit_item.html',{'item':item})

def edit_item_operate(request):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    stu=Person.objects.filter(student_id=student_id)
    item=stu[0].item_original
    item.name=request.POST['name']
    item.description=request.POST['description']
    item.save()
    return item_detail(request,item.id)

def self_profile(request):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    info=get_object_or_404(Person, student_id=student_id)
    return render(request,'uchange_app/self_profile.html',{'info':info})

def edit_profile(request):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    info=get_object_or_404(Person,student_id=student_id)
    return render(request,'uchange_app/edit_profile.html',{'info':info})

def edit_profile_operate(request):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    user=request.user
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    password=request.POST['password']
    password1=request.POST['password1']
    email=request.POST['email']
    user.first_name=first_name
    user.last_name=last_name
    user.email=email
    stu=get_object_or_404(Person,student_id=user.username)
    stu.first_name=first_name
    stu.last_name=last_name
    stu.email=email
    stu.save()
    if password != "":
        if password!=password1:
            return HttpResponse("Invalid password.")
        else:
            user.set_password(password)
    user.save()
    return HttpResponseRedirect("/home/profile")

def post_comment(request,item_id):
    con=Control.objects.all()
    if con[0].result_switch == 'on':
        return HttpResponseRedirect("/home/result/")
    student_id=request.user.username
    stu=get_object_or_404(Person,student_id=student_id)
    item=get_object_or_404(Item,id=item_id)
    content=request.POST['content']
    com=Comment(person=stu,item=item,content=content,comment_time=timezone.now())
    com.save()
    return HttpResponseRedirect("/home/item/"+item_id)
