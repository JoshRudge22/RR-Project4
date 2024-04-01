from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Job, Profile
from .forms import ProfileForm


def jobs(request):
    jobs = Job.objects.all()
    items_per_page = 6
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
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'profile': profile, 'form': form})