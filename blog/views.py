from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Entry
from .forms import EntryForm

def entry_list(request):	
	entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/entry_list.html',{'entries':entries})

def entry_detail(request,pk):
	entry = get_object_or_404(Entry, pk=pk)
	return render(request, 'blog/entry_detail.html',{'entry':entry})

def entry_new(request):
	form=EntryForm()
	return render(request, 'blog/entry_edit.html', {'form':form})

# Create your views here.
