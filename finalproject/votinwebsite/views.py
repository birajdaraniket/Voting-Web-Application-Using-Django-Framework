from django.http import HttpResponse
from django.shortcuts import render
from votinwebsite.models import count  # Assuming Count is the model for counting votes
from votinwebsite.models import login  # Assuming Login is the model for user login
from votinwebsite.models import signup
from votinwebsite.models import contact
from votinwebsite.models import partyregistration
def home(request):
    if request.method == "POST":
        new_count = count()
        partyname = request.POST.get("partyname")
        votecount = request.POST.get("votecount")
        
        new_count.partyname = partyname
        new_count.votecount = votecount
        
        new_count.save()
        
        return HttpResponse("Data inserted")
      
    return render(request, 'count.html') 

def user_login(request):
    if request.method == "POST":
        new_login = login()
        VoterID = request.POST.get("VoterID")
        password = request.POST.get("password")
        
        new_login.VoterID = VoterID
        new_login.password = password
        
        new_login.save()
        
        return HttpResponse("Data inserted")
      
    return render(request, 'login.html')
 
def con(request):
   # return HttpResponse()
     if request.method == "POST":
        co = contact()
        name = request.POST.get("name")
        email= request.POST.get("email")
        message= request.POST.get("message")
       
    
        
        
        co.name = name
        co.email = email
        co.message=message
        
      
        co.save()
        
        return HttpResponse("Data inserted")
      
     return render(request,'contact.html')
   
def sign(request):
 
    if request.method == "POST":
        si = signup()
        name = request.POST.get("name")
        password= request.POST.get("password")
        village= request.POST.get("village")
        age= request.POST.get("age")
    
        
        
        si.name = name
        si.password = password
        si.village=village
        si.age=age
      
        si.save()
        
        return HttpResponse("Data inserted")
      
    return render(request, 'signup.html')

   
def res(request):
     if request.method == "POST":
        re = signup()
        partyname= request.POST.get("partyname")
        candidatename= request.POST.get("candidatename")
        vote= request.POST.get("vote")
        votes= request.POST.get("votes")
    
        
        
        re.partyname= partyname
        re.candidatename = candidatename
        re.vote=vote
        re.votes=votes
      
        re.save()
        return HttpResponse("Data inserted")
      
     return render(request, 'result.html')
   
   
def party(request):
   # return HttpResponse()
      if request.method == "POST":
        pa = partyregistration()
        partyname= request.POST.get("partyname")
        partyleader= request.POST.get("partyleader")
        
        pa.partyname= partyname
        pa.partyleader = partyleader
        
        pa.save()
        
        return HttpResponse("Data inserted")
      
      return render(request, 'partyregistration.html')
   
def index(request):    
    return render(request, 'index.html') 
  