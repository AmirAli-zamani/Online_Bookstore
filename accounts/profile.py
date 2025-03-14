from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user_comments = request.user.comments.all()
    return render(request, 'accounts/profile.html', {'comments': user_comments})
