from django.shortcuts import render, redirect
from .forms import ContactForm, HiringForm
from .models import ContactUsForm, Hiring

def home(request):
    return render(request, 'index.html')

def advertising(request):
    return render(request, 'advertising.html')

def submitted_contact(request):
    return render(request, 'submitted-contact.html')

def submitted_hiring(request):
    return render(request, 'submitted-hiring.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = form.cleaned_data['message']
            best_time_to_contact = form.cleaned_data['best_time_to_contact']
            contact_form_data = ContactUsForm.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                message=message,
                best_time_to_contact=best_time_to_contact
            )
            return redirect('submitted-contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def hiring_form(request):
    if request.method == 'POST':
        form = HiringForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('submitted-hiring')
    else:
        form = HiringForm()

    return render(request, 'hiring.html', {'form': form})
