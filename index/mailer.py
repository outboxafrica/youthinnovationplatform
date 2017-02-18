from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


class UNDPMailer():
    def sendVerification(self, email, code, url):
        mail = EmailMultiAlternatives(
            subject="UNDP Verification",
            body="Please open " + url + "users/verify/" + code
                 + " in your browser.",
            from_email="UNDP Django <undp_django@gmail.com>",
            to=[email],
            headers={"Reply-To": "undp_django@gmail.com"}
        )
        mail.attach_alternative("Click <a href=\"" + url + "users/verify/" + code
                                + "\">here</a> to activate your account", "text/html")

        mail.send()
