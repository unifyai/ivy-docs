Pricing and Credits
===================

The Hub has a credit system where each credit corresponds to 1 USD. These credits are consumed when querying
models through the Hub API. There are **no charges on top of the provider cost**; the consumed credits directly reflect the cost
associated with the specific request made to the endpoint.

This means that the cost will depend on your input and can be calculated using the pricing metrics displayed alongside
each provider endpoint on the corresponding model pages.

We're currently integrating a payment system to allow you to purchase additional credits for your Hub API usage. Meanwhile,
we're granting each user the equivalent of $2.50 in free credits per week if they are using the Hub.
Feel free to dive in, explore, and share any feedback with us!

You will soon be able to check this out properly in a dashboard, but in the meantime, you can query the
`Get Credits Endpoint <https://unify.ai/docs/hub/reference/endpoints.html#get-credits>`_ of the Hub API to get your
current credit balance.

Top-up Code
-----------

You may have received a code to increase your number of free weekly credits, if that's the case, you can 
activate it doing a request to this endpoint:

.. code-block:: bash

    curl -X 'POST' \
    'https://api.unify.ai/v0/promo?code=<CODE>' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer <YOUR_UNIFY_KEY>' \

Simply replace :code:`<CODE>` with your top up code and :code:`<YOUR_UNIFY_KEY>` with your API Key and 
do the request 🚀
