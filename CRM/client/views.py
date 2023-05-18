from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import AddClientForm
from django.contrib import messages

@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)
    return render(request, 'client/clients_list.html', {'clients':clients})

@login_required
def clients_detail(request, id):
    client = get_object_or_404(Client, created_by=request.user, pk=id)
    return render(request, 'client/clients_details.html', {'client': client})

@login_required
def create_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save() 
            messages.add_message(request, messages.SUCCESS, "The Client was created")
            return redirect('clients_list')
    else:    
        form = AddClientForm()
    return render(request,'client/client_add.html',{'form':form})    

@login_required
def delete_client(request,id):
    client = get_object_or_404(Client,created_by = request.user,id = id)
    client.delete()
    messages.add_message(request, messages.SUCCESS, "The Client was deleted")
    return redirect('clients_list')

@login_required
def mod_client(request,id):
    client = get_object_or_404(Client,created_by = request.user,id = id)
    if request.method == 'POST':
        mod_form = AddClientForm(request.POST,instance=client)
        if mod_form.is_valid():
            mod_form.save()
            messages.add_message(request, messages.SUCCESS, "The Client was modified")
            return redirect('clients_list')
    mod_form = AddClientForm(instance=client)    
    return render(request,'client/client_edit.html',{'form':mod_form})
    