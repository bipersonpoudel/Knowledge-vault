from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .forms import postform
from .models import Note
# Create your views here.
def home(request):
    notes=Note.objects.all()
    note = {'notes':notes}

    return render(request,'notes/home.html',{'notes':notes})



def add_note(request):
    
    if request.method=="POST":
        form = postform(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'notes/forms.html',{'form': form})
        return redirect('home')

    else:
        form = postform()
        return render(request,'notes/forms.html',{'form': form})



def note_detail(request,pk):
    note= get_object_or_404(Note,pk=pk)
    return render(request, 'notes/detail.html', {'note': note})




def edit_note(request,pk):
    note=get_object_or_404(Note,pk=pk)
    if request.method=="POST":
        form=postform(request.POST,instance=note)
        if form.is_valid():
            form.save()
        else:
            return render(request,'notes/forms.html',{'form': form})
        return redirect('home')
    else:
        form = postform(instance=note)
        return render(request, 'notes/edit.html', {'form': form})

