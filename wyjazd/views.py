from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Wyjazd
from .dFormularz import WyjazdFormularz, WyjazdSzukaj
# Create your views here.



def delegacja_print_view(request,id):
    obj= Wyjazd.objects.get(id = id)
    context = {
        'Wyjazd':obj
    }

    return render (request, "print_view.html", context)

def delegacja_find_view(request,*args,**kwargs):

    find_wyjazd = WyjazdSzukaj()
    context ={
        'form': find_wyjazd
    }
    if request.POST:
         path = "../print_view/" + str(request.POST['id_wyszukiwania'])
         return redirect (path)
    return render (request,'find_view.html', context)




def delegacja_create_view(request,*args,**kwargs):

    d_nowa = WyjazdFormularz()
    if request.method == 'POST':
        d_nowa = WyjazdFormularz(request.POST)
        if d_nowa.is_valid():
             new = Wyjazd.objects.create(**d_nowa.cleaned_data)
             new_path= "../print_view/"+str(new.id)
             return redirect(new_path)
        else:
             print(d_nowa.errors)


    context = {
       'form': d_nowa
    }

    return render (request, "create_view.html", context)




# Create your views here.
