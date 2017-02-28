from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineCheckboxes
from projects.models import Innovation


class StartupStageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StartupStageForm, self).__init__(*args, **kwargs)
        self.fields['idea_stage'].label = "Please select the stage of your startup*"
    idea_stage = forms.ChoiceField(
        choices=(('1', "I have an idea"),
                 ('2', "I have an idea and have something to show"),
                 ('3', "I'm thinking about target and direction for my idea"),
                 ('4', "I'm testing my business with actual users"),
                 ('5', "I'm looking to grow my business"),
                 ('6', "I'm looking to maintain growth"), ),
        widget=forms.RadioSelect, )

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('idea_stage'),
        FormActions(
            Button('cancel','Cancel', css_class='cancelBtn'),
            Submit(
                'next',
                'Submit',
                css_class="cancelBtn"
            ),
        ),
    )

    class Meta:
        model = Innovation
        fields = ('idea_stage', )