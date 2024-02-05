from rest_framework import serializers

from currency.models import Rate, Source, Contact_us

from app.currency.tasks import send_email_from_background
from django.conf import settings


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sell',
            'created'
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'name',
            'source_url',
            'phone',
            'logo'
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_us
        fields = (
            'email_from',
            'subject',
            'message',
        )

    def create(self, validated_data):
        instance = super(ContactUsSerializer, self).create(validated_data)
        recipient = settings.DEFAULT_FROM_EMAIL # noqa F841
        subject = 'User Contact Us'
        body = f'''
            Email to reply: {validated_data.get('email_from')}.
            Subject: {validated_data.get('subject')}.
            Body: {validated_data.get('message')}.
        '''
        send_email_from_background.delay(subject, body)

        return instance

    def update(self, instance, validated_data):
        instance.email_from = validated_data.get('email_from', instance.email_from)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance
