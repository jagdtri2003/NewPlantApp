import os
from flask import Flask, redirect, request,render_template

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51NZGQSSAIIsk5INfTwzmAEohra8wP9LOTXinBIj2OdaSXR6whzJJvyjz4OSiFSkRz9W6JZEiqdsiOqN2Zw9GlS9Z00Stwuz4rD'

app = Flask(__name__,
            static_url_path='',
            static_folder='public',template_folder='temp')

YOUR_DOMAIN = 'http://localhost:4242'

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/create-checkout-session', methods=['POST','GET'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1NZHdLSAIIsk5INfDnE90LFE',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)