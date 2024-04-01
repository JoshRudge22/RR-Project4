from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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