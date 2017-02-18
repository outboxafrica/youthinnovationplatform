from django.shortcuts import render
from . forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

# Create your views here.


def contact_index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            contact_email = request.POST.get(
                'Your_email_address'
            , '')
            contact_subject = request.POST.get(
                'Subject'
            , '')
            message = request.POST.get('Message', '')
            template = get_template('contact_us/contact_template.txt')
            context = {
                'contact_email': contact_email,
                'contact_subject': contact_subject,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
    else:
        form = ContactForm()
    form = ContactForm()
    return render(request, 'contact_us/contact_index.html', {'form':form})
