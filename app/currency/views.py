from django.http.response import HttpResponse, HttpResponseRedirect, Http404   # noqa F401
from django.shortcuts import render, get_object_or_404
from currency.models import Rate, Contact_us, Source

from currency.forms import RateForm, SourceForm


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }
    return render(request, 'rate_list.html', context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'form': form
    }
    return render(request, 'rate_create.html', context)


def rate_update(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':

        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/list/')

    elif request.method == 'GET':
        form = RateForm(instance=rate)

    context = {
        'form': form
    }
    return render(request, 'rate_update.html', context)


def rate_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'GET':
        context = {
            'object': rate
        }
        return render(request, 'rate_delete.html', context)
    elif request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')


def rate_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'rate': rate
    }
    return render(request, 'rate_details.html', context)


def source_list(request):
    sources = Source.objects.all()
    context = {
        'sources': sources
    }
    return render(request, 'source_list.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    elif request.method == 'GET':
        form = SourceForm()

    context = {
        'form': form
    }
    return render(request, 'source_create.html', context)


def source_update(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':

        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')

    elif request.method == 'GET':
        form = SourceForm(instance=source)

    context = {
        'form': form
    }
    return render(request, 'source_update.html', context)


def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'GET':
        context = {
            'object': source
        }
        return render(request, 'source_delete.html', context)
    elif request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/list/')


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)

    context = {
        'source': source
    }
    return render(request, 'source_details.html', context)


def Contact_us_list(request):
    Contact_us_list = Contact_us.objects.all()
    context = {
        'contact_us': Contact_us_list
    }
    return render(request, 'contact_us.html', context)
