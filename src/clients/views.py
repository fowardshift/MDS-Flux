from django.shortcuts import redirect, render
from .models import Client
from .forms import ClientForm

# Create your views here.
def list_clients (request):
    clients= Client.objects.all()
    return render (request, 'clients/clients.html', {'clients' : clients})

def create_client (request):
    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_clients)

    return render(request, 'clients/clients-form.html', {'form': form})

def update_client (request, id):
    client = Client.objects.get(id=id)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect(list_clients)

    return render(request, 'clients/clients-form.html', {'form': form, 'client': client}) 

def delete_client (request, id):
    client = Client.objects.get(id=id)

    if request.method == 'POST':
        client.delete()
        return redirect(list_clients)
        
    return render(request, 'clients/client-delete.html', {'client' : client})