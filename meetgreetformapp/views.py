from django.shortcuts import render, redirect, get_object_or_404
from .forms import FanForm, PaymentForm, PaymentSlipForm
from django.conf import settings
from django.core.mail import EmailMessage
from .models import Fans
import requests

def fan_meet_and_greet(request):
    if request.method == 'POST':
        form = FanForm(request.POST)
        if form.is_valid():
            fan_data = form.cleaned_data
            # Convert date_of_birth to string
            fan_data['date_of_birth'] = fan_data['date_of_birth'].isoformat()
            request.session['fan_data'] = fan_data
            return redirect('payment')
    else:
        form = FanForm()
    return render(request, 'fans/fan_form.html', {'form': form})

def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_data = form.cleaned_data
            # Assuming you have a way to get the fan_id, for example from the session
            fan_data = request.session.get('fan_data')
            if fan_data:
                fan = Fans.objects.create(**fan_data)
                payment_data['fan_id'] = fan.id
                request.session['payment_data'] = payment_data
                return redirect('payment_details')
    else:
        form = PaymentForm()
    return render(request, 'fans/payment.html', {'form': form})

def payment_details(request):
    payment_data = request.session.get('payment_data')
    if not payment_data:
        return redirect('payment')

    fan = get_object_or_404(Fans, pk=payment_data['fan_id'])

    if request.method == "POST":
        form = PaymentSlipForm(request.POST, request.FILES, instance=fan)
        if form.is_valid():
            form.save()
            # Prepare email content with all user's details
            email_subject = 'Payment Received'
            email_body = (
                f'User {fan.name} has made a payment. Details:\n\n'
                f'Name: {fan.name}\n'
                f'Date of Birth: {fan.date_of_birth}\n'
                f'Address: {fan.address}\n'
                f'Phone: {fan.phone_no}\n'
                f'Email: {fan.email}\n'
                f'Occupation: {fan.occupation}\n'
                f'Age: {fan.age}\n'
                f'Civil Status: {fan.civil_status}\n'
                f'Citizenship: {fan.citizenship}\n'
                f'Height: {fan.height}\n'
                f'Weight: {fan.weight}\n'
                f'Religion: {fan.religion}\n'
                f'Language: {fan.language}\n'
                f'Will you have a guest with you: {fan.will_you_have_a_guest_with_you}\n'
                f'Would you like to be updated about the upcoming tour: {fan.would_you_like_to_be_updated_about_the_upcoming_tour}\n'
                f'How long have you been supporting Lee Minho: {fan.how_long_have_you_been_supporting_leeminho}\n'
                f'Do you have his membership card: {fan.do_you_have_his_membership_card}\n'
                f'Which category of fan card do you have: {fan.which_category_of_fan_card_do_you_have}\n'
                f'Do you have a ticket for Minhoverse: {fan.do_you_have_ticket_for_minhoverse}\n'
            )

            # Create email message
            email = EmailMessage(
                email_subject,
                email_body,
                fan.email,  # from_email
                ['nwachukwuclinton2@gmail.com'],  # to_email
            )

            # Attach the payment slip
            if fan.payment_slip:
                email.attach(fan.payment_slip.name, fan.payment_slip.read(), fan.payment_slip.content_type)

            # Send email
            email.send(fail_silently=False)
            return redirect('success')
    else:
        form = PaymentSlipForm(instance=fan)

    if payment_data['payment_method'] == 'paypal':
        payment_info = {
            'method': 'PayPal',
            'details': settings.PAYPAL_EMAIL
        }
    elif payment_data['payment_method'] == 'bitcoin':
        payment_info = {
            'method': 'Bitcoin',
            'details': settings.BITCOIN_ADDRESS
        }

    context = {
        'payment_info': payment_info,
        'form': form,
        'fan': fan,
    }
    return render(request, 'fans/payment_details.html', context)

def success(request):
    fan_data = request.session.get('fan_data')
    payment_data = request.session.get('payment_data')
    return render(request, 'fans/success.html', {'fan_data': fan_data, 'payment_data': payment_data})









# integrate good logic for payements
# def payment(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             payment_data = form.cleaned_data
#             request.session['payment_data'] = payment_data
#             if payment_data['payment_method'] == 'paypal':
#                 payment_success = process_paypal_payment(payment_data)
#             elif payment_data['payment_method'] == 'bitcoin':
#                 payment_success, invoice_url = process_bitcoin_payment()
#                 if payment_success:
#                     return redirect(invoice_url)
#
#             if payment_success:
#                 return redirect('success')
#             else:
#                 form.add_error(None, "Payment failed. Please try again.")
#     else:
#         form = PaymentForm()
#     return render(request, 'fans/payment.html', {'form': form})
#
#
# def success(request):
#     fan_data = request.session.get('fan_data')
#     payment_data = request.session.get('payment_data')
#     return render(request, 'fans/success.html', {'fan_data': fan_data, 'payment_data': payment_data})
#
#
# def process_paypal_payment(payment_data):
#     try:
#         access_token = get_paypal_access_token()
#         headers = {
#             'Content-Type': 'application/json',
#             'Authorization': f'Bearer {access_token}'
#         }
#         data = {
#             'intent': 'sale',
#             'payer': {
#                 'payment_method': 'paypal'
#             },
#             'transactions': [{
#                 'amount': {
#                     'total': '50.00',
#                     'currency': 'USD'
#                 },
#                 'description': 'Fan Meet and Greet Payment'
#             }],
#             'redirect_urls': {
#                 'return_url': 'http://localhost:8000/success',
#                 'cancel_url': 'http://localhost:8000/payment'
#             }
#         }
#         response = requests.post('https://api.sandbox.paypal.com/v1/payments/payment', headers=headers, json=data)
#         response_data = response.json()
#         for link in response_data['links']:
#             if link['rel'] == 'approval_url':
#                 approval_url = link['href']
#                 return True, approval_url
#         return False, None
#     except Exception as e:
#         print(e)
#         return False, None
#
#
# def get_paypal_access_token():
#     url = f'https://api.{settings.PAYPAL_MODE}.paypal.com/v1/oauth2/token'
#     headers = {
#         'Accept': 'application/json',
#         'Accept-Language': 'en_US'
#     }
#     data = {
#         'grant_type': 'client_credentials'
#     }
#     response = requests.post(url, headers=headers, data=data,
#                              auth=(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_CLIENT_SECRET))
#     response_data = response.json()
#     return response_data['access_token']
#
#
# def process_bitcoin_payment():
#     try:
#         client = BTCPayClient(
#             host=settings.BTCPAY_SERVER_URL,
#             api_key=settings.BTCPAY_API_KEY,
#             store_id=settings.BTCPAY_STORE_ID
#         )
#         invoice = client.create_invoice({
#             'price': 5000,
#             'currency': 'USD',
#             'buyer': {
#                 'name': 'Fan Meet and Greet'
#             }
#         })
#         return True, invoice['url']
#     except Exception as e:
#         print(e)
#         return False, None