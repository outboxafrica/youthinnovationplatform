from django import forms
from crispy_forms.layout import Field, Submit, Div, Layout
from crispy_forms.helper import FormHelper


class ContactForm(forms.Form):
    Your_email_address = forms.EmailField(required=True)
    Subject = forms.CharField(required=True, max_length=200)
    Message = forms.CharField(required=True,
                                      widget=forms.Textarea)
    # contact_message = forms.CharField(required=True, max_length=500)

    #font-family: "/FiraSans-Thin/";

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        text_small = "width: 30vw;border-radius: 30px;border-style: none;border-color: transparent;background-color: " \
                     "#eee;padding-left: 20px;padding-right: 20px;padding-bottom: 5px;padding-top: 5px;height: 33px;" \
                     "border: none;"
        text_large = "width: 30vw;border-radius: 15px;border-style: none;border-color: transparent;background-color: " \
                     "#eee;padding-left: 20px;padding-right: 20px;padding-bottom: 5px;padding-top: 5px; height:70px;"

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('Your_email_address', style=text_small, title="Your email address"),
            Field('Subject', style=text_small, title="Subject"),
            Field('Message', style=text_large, title="Message"),
            Submit('submit', 'Send', css_class='cancelBtn')
        )
