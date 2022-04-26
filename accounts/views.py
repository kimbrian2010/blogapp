from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def account(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now login')
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required()
def edit_profile(request):
    if request.method == "POST":
        update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) #removed request.FILE
        if update_form.is_valid() and profile_update_form.is_valid():
            update_form.save()
            profile_update_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'update_form': update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'accounts/editprofile.html', context)
