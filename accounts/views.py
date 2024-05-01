from django.shortcuts import redirect


def redirect_login(request):
    return redirect(f"/user/{request.user.pk}/")