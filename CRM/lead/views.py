from django.shortcuts import render,redirect
from .forms import CreateLead
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def create_lead(request):
    if request.method == 'POST':
        form = CreateLead(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save() 
            return redirect('dashboard')
    else:    
        form = CreateLead()
    return render(request,'lead/create_lead.html',{'form':form})    