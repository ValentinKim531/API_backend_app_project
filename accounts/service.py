from django.core.mail import send_mail
from .models import OTP
from .tasks import otp_code_inspired_delete, otp_code_verified_delete
import logging
from django.conf import settings
logger = logging.getLogger(__name__)


def send_email(request):
    logger.warning("===================")
    email = request.data.get("username")
    code = OTP.generate_code()
    obj = OTP.objects.create(user=email, code=code)
    htmlgen = (f'<p>Ваш код для подтверждения <strong>{code}</strong></p>'
               f'C уважением, команда Sulu sai')
    r = send_mail(
        'Код для подтверждения адреса электронной почты', code,
        f'Sulu sai <{settings.EMAIL_HOST_USER}>',
        [email], fail_silently=False, html_message=htmlgen
    )
    logger.warning(r)
    otp_code_inspired_delete.delay(obj.pk)


def verify_email(request):
    obj = OTP.objects.filter(user=request.data.get('username')).last()
    if request.data['code'] == obj.code:
        obj.verified = True
        obj.save()
        otp_code_verified_delete.delay(obj.pk)
        return {'success': True}
    else:
        return {'success': False}
