import requests
from currency.utils import to_2_places_decimal
from celery import shared_task
from currency import consts
from django.conf import settings
from django.core.mail import send_mail
from currency.choices import RateCurrencyChoices


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source

    source, _ = Source.objects.get_or_create(
        code_name=consts.PRIVATBANK_CODE_NAME,
        defaults={
            'name': 'PrivatBank'
        }
    )

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11'
    response = requests.get(url)
    response.raise_for_status()

    rates = response.json()

    available_currencies = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR
    }
    for rate in rates:
        buy = to_2_places_decimal(rate['buy'])
        sale = to_2_places_decimal(rate['sale'])
        currency = rate['ccy']

        if currency not in available_currencies:
            continue

        currency = available_currencies[currency]

        last_rate = Rate.objects.filter(source=source, currency=currency)\
            .order_by('-created')\
            .first()

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sale:
            Rate.objects.create(
                buy=buy,
                sell=sale,
                source=source,
                currency=currency
            )


@shared_task
def parse_monobank():
    from currency.models import Rate, Source

    source, _ = Source.objects.get_or_create(
        code_name=consts.MONOBANK_CODE_NAME,
        defaults={
            'name': 'Monobank'
        }
    )

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()

    rates = response.json()

    available_currencies = {
        '840': RateCurrencyChoices.USD,
        '978': RateCurrencyChoices.EUR,
    }

    for rate in rates:
        rateBuy = to_2_places_decimal(rate['rateBuy'])
        rateSell = to_2_places_decimal(rate['rateSell'])
        currency_code = str(rate['currencyCodeA'])
        second_currency = str(rate['currencyCodeB'])

        if currency_code not in available_currencies or second_currency in available_currencies:
            continue

        currency = available_currencies[currency_code]

        last_rate = Rate.objects.filter(source=source, currency=currency)\
            .order_by('-created')\
            .first()

        if last_rate is None or last_rate.buy != rateBuy or last_rate.sell != rateSell:
            Rate.objects.create(
                buy=rateBuy,
                sell=rateSell,
                source=source,
                currency=currency
            )


@shared_task(
    autoretry_for=(ConnectionError,),
    retry_kwargs={'max_retries': 5}
)
def send_email_from_background(subject, body):
    from time import sleep
    sleep(10)

    recipient = settings.DEFAULT_FROM_EMAIL
    send_mail(
        subject,
        body,
        recipient,
        [recipient],
        fail_silently=False
    )
