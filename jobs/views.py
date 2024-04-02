from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Job, Profile, JobApplication
from .forms import ProfileForm, JobApplicationForm

def submitted(request):
    return render(request, 'submitted.html')


def jobs(request):
    jobs = Job.objects.all()
    items_per_page = 5
    paginator = Paginator(jobs, items_per_page)
    page = request.GET.get('page')
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)
    return render(request, 'jobs.html', {'jobs': jobs})

@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile.save()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'profile': profile, 'form': form})

@login_required
def applying(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    user_profile = request.user.profile
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            recipients = ["joshrudge@hotmail.com"]
            send_mail(
                subject,
                message,
                sender,
                recipients,
                fail_silently=False
            )
            return redirect('submitted')
    else:
        form = JobApplicationForm()
    return render(request, 'applying.html', {'form': form, 'job': job, 'user_profile': user_profile})