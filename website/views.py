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
		send_mail(your_name + your_subject, your_message, your_email, ['omkarh.work@gmail.com', 'omkarh@gmail.com'],)

		return render(request, 'home.html' ,{'your_name': your_name})
	else:
		return render(request, 'home.html', {})