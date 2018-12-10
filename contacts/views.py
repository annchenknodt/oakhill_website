from django.shortcuts import render
from .forms import InputForm
from .models import Contact

def getContact(request):
	
	if request.method == 'POST':

		form = InputForm(request.POST)
		
		if form.is_valid():

			data=form.cleaned_data

			## save to database
			new_contact=Contact.objects.create(**data)
			new_contact.save()

			return render(request, 'confirmation.html')	

		else:
			print("NAY")
			val=0

	else:
		
		form = InputForm()

	return render(request, 'input.html',{'form':form})	