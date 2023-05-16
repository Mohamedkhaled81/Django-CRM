from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .forms import CreateLead
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Leads
# Create your views here.

@login_required
def create_lead(request):
    if request.method == 'POST':
        form = CreateLead(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save() 
            messages.add_message(request, messages.SUCCESS, "The Lead was created")
            return redirect('list_leads')
        
    else:    
        form = CreateLead()
    return render(request,'lead/create_lead.html',{'form':form})    



@login_required
def list_leads(request):
    leads = Leads.objects.filter(created_by = request.user)
    if leads:
        return render(request,'lead/list_leads.html',{'leads':leads})
    return render(request,'lead/list_leads.html')


@login_required
def detail_lead(request,id):
    lead = get_object_or_404(Leads,created_by = request.user,id = id)
    return render(request,'lead/detail_lead.html',{'lead':lead})    




@login_required
def mod_lead(request,id):
    lead = get_object_or_404(Leads,created_by = request.user,id = id)
    if request.method == 'POST':
        mod_form = CreateLead(request.POST,instance=lead)
        if mod_form.is_valid():
            mod_form.save()
            messages.add_message(request, messages.SUCCESS, "The Lead was modified")
            return redirect('detail_lead',id = id)

    mod_form = CreateLead(instance=lead)    
    return render(request,'lead/modify_lead.html',{'form':mod_form})
    

@login_required
def delete_lead(request,id):
    lead = get_object_or_404(Leads,created_by = request.user,id = id)
    lead.delete()
    messages.add_message(request, messages.SUCCESS, "The Lead was deleted")
    return redirect('list_leads')