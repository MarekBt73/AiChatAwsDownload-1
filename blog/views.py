from django.shortcuts import render


def home(request):
    return render(request, 'blog/home.html')

def contact(request):
    return render(request, 'blog/contact.html')


def custom_page_not_found_view(request, exception):
    return render(request, 'blog/404.html', {}, status=404)