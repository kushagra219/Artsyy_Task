from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def UpdatedUserProfile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile:profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'user_profile/profile.html', {'form': form, 'user':user})