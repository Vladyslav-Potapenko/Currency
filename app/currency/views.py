from django.shortcuts import render

from django.http.response import HttpResponse

from currency.models import Rate, Contact_us



def rate_list(request):
    # results = []
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }
    # for rate in rates:
    #     results.append(
    #         f'{rate.id}'
    #     )
    # return HttpResponse(str(results))
    return render(request, 'rate_list.html', context)

def Contact_us_list(request):
    results = []
    contact_us_list = Contact_us.objects.all()
    for contactus in contact_us_list:
        results.append(
            f'ID: {contactus.id}, Email:{contactus.email_from}, Subject: {contactus.subject}, Message: {contactus.message}'  # noqa: E501
        )

    return HttpResponse(str(results))


# def rate_list(request):
#     rates = Rate.objects.all()
#     context = {
#         'rates': rates
#     }
#     return render(request, rate_list, context)