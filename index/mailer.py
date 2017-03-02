from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


class UNDPMailer():
    def sendVerification(self, email, code, url):
        mail = EmailMultiAlternatives(
            subject="UNDP Email Verification",
            body="Please open " + url + "users/verify/" + code
                 + " in your browser.",
            from_email="UNDP Django <undp_django@gmail.com>",
            to=[email],
            headers={"Reply-To": "undp_django@gmail.com"}
        )
        mail.attach_alternative("Click <a href=\"" + url + "verify/" + code
                                + "\">here</a> to activate your account. This link will expire in 24 hours.", "text/html")

        mail.send()

    def sendResetEmail(self, email, code, url):
        mail = EmailMultiAlternatives(
            subject="NDP Password reset link",
            body="Please open " + url + "users/verify/" + code
                 + " in your browser.",
            from_email="UNDP Django <undp_django@gmail.com>",
            to=[email],
            headers={"Reply-To": "undp_django@gmail.com"}
        )
        mail.attach_alternative("Click <a href=\"" + url + "confirm_password/" + code
                                + "\">here</a> to reset your password. This link will expire in 24 hours.", "text/html")

        mail.send()
