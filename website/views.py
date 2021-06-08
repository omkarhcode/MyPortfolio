from django.shortcuts import render


def home(request):

	if request.method == "POST":
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_subject = request.POST['your-subject']
		your_message = request.POST['your-message']
		return render(request, 'home.html' ,{'your_name': your_name})
	
	return render(request, 'home.html', {})