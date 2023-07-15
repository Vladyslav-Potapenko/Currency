from django.shortcuts import render

from currency.models import Rate, Contact_us


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }
    return render(request, 'rate_list.html', context)


def Contact_us_list(request):
    Contact_us_list = Contact_us.objects.all()
    context = {
        'contact_us': Contact_us_list
    }
    return render(request, 'contact_us.html', context)
