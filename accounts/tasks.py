from celery import shared_task
from django.shortcuts import get_object_or_404
from .models import OTP
import time


@shared_task(name='otp_code_inspired_delete')
def otp_code_inspired_delete(pk):
    time.sleep(180)
    obj = get_object_or_404(OTP.objects.all(), pk=pk)
    if not obj.verified:
        obj.delete()


@shared_task(name='otp_code_verified_delete')
def otp_code_verified_delete(pk):
    time.sleep(180)
    obj = get_object_or_404(OTP.objects.all(), pk=pk)
    if obj.verified:
        obj.delete()
