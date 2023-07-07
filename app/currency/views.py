# from django.shortcuts import render
from django.http.response import HttpResponse

from currency.models import Rate, Contact_us


def rate_list(request):
    results = []
    rates = Rate.objects.all()
    for rate in rates:
        results.append(
            f'{rate.id}'
        )
    return HttpResponse(str(results))


def Contact_us_list(request):
    results = []
    contact_us_list = Contact_us.objects.all()
    for contactus in contact_us_list:
        results.append(
            f'ID: {contactus.id}, Email:{contactus.email_from}, Subject: {contactus.subject}, Message: {contactus.message}'  # noqa: E501
        )

    return HttpResponse(str(results))
