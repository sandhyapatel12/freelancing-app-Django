from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GigForm
from .models import Gig
from accounts.models import CustomUser, UserProfile
from django.http import QueryDict


# Create your views here.

@login_required(login_url='accounts:login')  # Redirect to login if not logged in
def home(request):
    return render(request, 'main/home.html')


@login_required
def freelancer_dashboard(request):
    # Ensure only freelancers can access
    if request.user.get_user_type_display() != "Freelancer":
        return redirect('home')  # Redirect clients to home or another page
    
    return render(request, 'main/freelancer_dashboard.html')


@login_required
def create_gig(request):
    if request.user.user_type != 'freelancer':
        return redirect('home')

    if request.method == 'POST':
        form = GigForm(request.POST, request.FILES)
        if form.is_valid():
            gig = form.save(commit=False)
            gig.freelancer = request.user
            gig.save()
            return redirect('view_gig', gig_id=gig.id)  # redirect to detail page
    else:
        form = GigForm()
    return render(request, 'main/create_gig.html', {'form': form})

@login_required
def view_gig(request, gig_id):
    gig = get_object_or_404(Gig, id=gig_id, freelancer=request.user)
    return render(request, 'main/view_gig.html', {'gig': gig})


@login_required
def edit_gig(request, gig_id):
    gig = get_object_or_404(Gig, id=gig_id, freelancer=request.user)

    if request.method == 'POST':
        form = GigForm(request.POST, request.FILES, instance=gig)
        if form.is_valid():
            form.save()
            return redirect('view_gig', gig_id=gig.id)
    else:
        form = GigForm(instance=gig)
    return render(request, 'main/edit_gig.html', {'form': form, 'gig': gig})



@login_required
def client_dashboard(request):
    if request.user.user_type != 'client':
        return redirect('home')
    gigs = Gig.objects.all().order_by('-created_at')
    return render(request, 'main/client_dashboard.html', {'gigs': gigs})



def gig_detail(request, gig_id):
    gig = get_object_or_404(Gig, id=gig_id)
    profile, created = UserProfile.objects.get_or_create(user=gig.freelancer)
    skills = profile.skills.split(',') if profile.skills else []

    # Get all gigs by this freelancer except the current one
    gigs = Gig.objects.filter(freelancer=gig.freelancer).exclude(id=gig.id)

    context = {
        'gig': gig,
        'profile': profile,
        'skills': skills,
        'user': gig.freelancer,
        'gigs': gigs,  # Add this line
    }
    return render(request, 'main/gig_detail.html', context)









