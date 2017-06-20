from django.shortcuts import render

def index (request):
	return render(request, 'index.html', {})

def Booking (request):
	return render(request, 'Booking.html', {})

def About (request):
	return render(request, 'About.html', {})

def contact (request):
	return render(request, 'contact.html', {})
