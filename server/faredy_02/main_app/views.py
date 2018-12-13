from django.shortcuts import render

def index_view(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'main_app/index.html')
    else:
        return render(request, 'main_app/index.html')
