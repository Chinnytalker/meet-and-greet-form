from django import forms
from .models import Fans




class FanForm(forms.ModelForm):
    will_you_have_a_guest_with_you = forms.TypedChoiceField(
        label="Will you have a guest with you?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        initial='1',
        required=True,
    )
    would_you_like_to_be_updated_about_the_upcoming_tour = forms.TypedChoiceField(
        label="Would you like to be updated about the upcoming tour?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        initial='1',
        required=True,
    )
    how_long_have_you_been_supporting_leeminho = forms.TypedChoiceField(
        label="How long have you been supporting Lee Min Ho?",
        choices=((1, "Less than a year"), (2, "1-3 years"), (3, "More than 3 years")),
        coerce=int,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        initial='1',
        required=True,
    )
    do_you_have_his_membership_card = forms.TypedChoiceField(
        label="Do you have his membership card?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        initial='1',
        required=True,
    )
    which_category_of_fan_card_do_you_have = forms.TypedChoiceField(
        label="Which category of fan card do you have?",
        choices=((1, "Bronze"), (2, "Silver"), (3, "VIP"), (4, "V VIP")),
        coerce=int,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        initial='1',
        required=True,
    )
    do_you_have_ticket_for_minhoverse = forms.TypedChoiceField(
        label="Do you have ticket for Minhoverse?",
        choices=((1, "Yes"), (0, "No")),
        coerce=lambda x: bool(int(x)),
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        initial='1',
        required=True,
    )

    class Meta:
        model = Fans
        fields = [
            'name', 'date_of_birth', 'address', 'phone_no', 'email', 'occupation', 'age',
            'civil_status', 'citizenship', 'height', 'weight', 'religion', 'language',
            'will_you_have_a_guest_with_you', 'would_you_like_to_be_updated_about_the_upcoming_tour',
            'how_long_have_you_been_supporting_leeminho', 'do_you_have_his_membership_card',
            'which_category_of_fan_card_do_you_have', 'do_you_have_ticket_for_minhoverse','if_yes_which_of_the_ticket_category_and_country_do_you_have',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'civil_status': forms.TextInput(attrs={'class': 'form-control'}),
            'citizenship': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'religion': forms.TextInput(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'if_yes_which_of_the_ticket_category_and_country_do_you_have' : forms.TextInput(attrs={'class': 'form-control'}),
        }







class PaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=[('paypal', 'PayPal Bank Transfer'), ('bitcoin', 'Bitcoin')],
        widget=forms.RadioSelect,
        label="Select Payment Method"
    )


class PaymentSlipForm(forms.ModelForm):
    class Meta:
        model = Fans
        fields = ['payment_slip']

