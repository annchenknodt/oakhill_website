from django.shortcuts import render
from django.core.mail import send_mail
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

			## send email alert
			message="\n".join(['New contact form submission!\n',
			'Name: '+data['name_first']+" "+data['name_last'],
			'Email: '+data['email'],
			'Phone: '+data['phone'],
			'Address: '+data['address_st1']+" "+data['address_st2']+" "+data['address_city']+" "+data['address_state']+" "+data['address_zip']
			])

			send_mail('My Subject', message, 'aknodt@gmail.com', ['aknodt@gmail.com'], fail_silently=False)

			return render(request, 'confirmation.html')	

		else:
			print("NAY")
			val=0

	else:
		
		form = InputForm()

	return render(request, 'input.html',{'form':form})	