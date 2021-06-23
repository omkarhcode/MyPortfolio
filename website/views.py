from django.shortcuts import render
from django.core.mail import send_mail


def home(request):

	# Get data from contact from on home page
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_subject = request.POST['your-subject']
		your_message = request.POST['your-message']

		# Send an E-mail
		# send_mail(subject, message, from_email, recipient_list)
		send_mail(" omkarh.info - "+ your_subject,
			 	"FROM - "+your_name +", EMAIL - "+your_email +", SUBJECT - "+ your_subject+", MESSAGE - "+your_message + " ---Sent from a contact form on omkarh.info---",
			  	your_email,
			   	['omkarh.work@gmail.com'],
			   )

		return render(request, 'home.html' ,{'your_name': your_name})
	else:
		return render(request, 'home.html', {})