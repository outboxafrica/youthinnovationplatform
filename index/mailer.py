from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

import sendgrid
from sendgrid.helpers.mail import *


class UNDPMailer():
    def __init__(self):
        self.from_email = 'undp_django@gmail.com'

    def sendVerification(self, email, code, url):
        # mail = EmailMultiAlternatives(
        #     subject="UNDP Account Verification",
        #     body="Please open " + url + "users/verify/" + code
        #          + " in your browser.",
        #     from_email="UNDP Django <undp_django@gmail.com>",
        #     to=[email],
        #     headers={"Reply-To": "undp_django@gmail.com"}
        # )
        # mail.attach_alternative("Click <a href=\"" + url + "verify/" + code
        #                         + "\">Here</a> to activate your account. This link will expire in 24 hours.", "text/html")
        #
        # mail.send()

        body = "Please open " + url + "users/verify/" + code + " in your browser."

        return send_mail(
                "UNDP Account Verification",
                body,
                self.from_email,
                [email,],
                fail_silently=False)

    def sendResetEmail(self, email, code, url):
        # mail = EmailMultiAlternatives(
        #     subject="UNDP Password Reset Link",
        #     body="Please open " + url + "users/verify/" + code
        #          + " in your browser.",
        #     from_email="UNDP Django <undp_django@gmail.com>",
        #     to=[email],
        #     headers={"Reply-To": "undp_django@gmail.com"}
        # )
        # mail.attach_alternative("Click <a href=\"" + url + "confirm_password/" + code
        #                         + "\">here</a> to reset your password. This link will expire in 24 hours.", "text/html")
        #
        # mail.send()

        body = "Please open " + url + "users/verify/" + code + " in your browser."

        return send_mail(
            "UNDP Password Reset Link",
            body,
            self.from_email,
            [email,],
            fail_silently=False)

    def send_account_recover_email(self, email, code, url):
        mail = EmailMultiAlternatives(
            subject="UNDP Account Recovery Link",
            body="Please open " + url + "users/verify/" + code
                 + " in your browser.",
            from_email="UNDP Django <undp_django@gmail.com>",
            to=[email],
            headers={"Reply-To": "undp_django@gmail.com"}
        )
        mail.attach_alternative("Click <a href=\"" + url + "verify/" + code
                                + "\">here</a> to recover your account. This link will expire in 24 hours.", "text/html")

        mail.send()
        body = "Please open " + url + "users/verify/" + code + " in your browser.",

        return send_mail(
            "UNDP Account Recovery Link",
            body,
            self.from_email,
            [email,],
            fail_silently=False)
