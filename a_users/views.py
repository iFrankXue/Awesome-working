from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm

# Create your views here.
def profile_view(request):
    profile = request.user.profile
    context = {
        'profile': profile
    }
    return render(request, 'a_users/profile.html', context)


def profile_edit_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileForm(instance=request.user.profile)  

    context = {
        'form': form    
    }
    return render(request, 'a_users/profile_edit.html', context)