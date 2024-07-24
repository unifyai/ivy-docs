Universal API
==============

There’s a sea of models and providers, with new LLMs coming out all the time.
Each provider has its own API keys, account balance, and subtle nuances in how the models are queried.

The Unify Universal API provides:

- A single, common interface for all models and providers
- One account, with one balance and one API key

You can interact with the API through a HTTP request from any programming language, through our own Unify Python package, or through the OpenAI Python package.

Authentication
--------------
You need an API key to query the API. `Sign up for an account <https://console.unify.ai/login>`_, and get your API key from the `console <https://console.unify.ai/>`_.

Querying the API
----------------
There are three ways to query the API:

- HTTP request
- Unify Python package
- OpenAI Python package


HTTP Request
^^^^^^^^^^^^
Run the following command in a terminal (replacing :code:`$UNIFY_API_KEY` with your own).

.. code-block::

    curl -X 'POST' \
        'https://api.unify.ai/v0/chat/completions' \
        -H 'Authorization: Bearer $UNIFY_API_KEY' \
        -H 'Content-Type: application/json' \
        -d '{
        "model": "llama-3-8b-chat@fireworks-ai",
            "messages": [{"role": "user", "content": "Say hello."}]
        }'

The :code:`model` field is used to specify both the model and the provider, in the format :code:`model@provider`. You can find a list of models and providers either in our `chat <https://unify.ai/chat>`_ interface, or through our `runtime benchmarks <https://unify.ai/benchmarks>`_.

Requests can be made from any language, for example using Python:

.. code-block:: python

    import requests

    url = "https://api.unify.ai/v0/chat/completions"
    headers = {
        "Authorization": "Bearer UNIFY_API_KEY",
    }
    payload = {
        "model": "llama-3-8b-chat@together-ai",
        "messages": [{"role": "user", "content": "Say hello."}]
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

The response from a request should look something like this:

.. code-block:: python

    {
    "model": "llama-3-8b-chat@together-ai",
    "created": 1718888877,
    "id": "896bfc1ae84271aa-LHR",
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 25,
        "prompt_tokens": 13,
        "total_tokens": 38,
        "cost": 7.6e-06
    },
    "choices": [
        {
        "finish_reason": "stop",
        "index": 0,
        "message": {
            "content": "Hello! It's nice to meet you. Is there something I can help you with or would you like to chat?",
            "role": "assistant",
        },
        "seed": 11563975138181362140
        }
    ]
    }

The output from the LLM is accessed via :code:`choices[0].message.content`.
The :code:`usage` field contains the number of prompt/completion tokens, as well as the total cost of the request, in US$.
In the request you can specify other common parameters, like
:code:`temperature`, :code:`stream` and :code:`max_tokens`.

You can specify all of the parameters that OpenAI supports, but they may not be compatible with every model or provider.

Unify Python Package
^^^^^^^^^^^^^^^^^^^^
First, download our `Python package <https://github.com/unifyai/unify>`_ with :code:`pip install unifyai`.

There is complete documentation in the `readme <https://github.com/unifyai/unify/blob/main/README.md>`_.
Sample inference

.. code-block:: python

    from unify import Unify
    client = Unify("llama-3-8b-chat@fireworks-ai", api_key="$UNIFY_API_KEY")
    response = client.generate("Say hi.")

OpenAI Python Package
^^^^^^^^^^^^^^^^^^^^^
The Unify API is designed to be compatible with the OpenAI standard, so if you have existing code that uses the OpenAI Python package, it's straightforward to try out our API.

.. code-block:: python

    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.unify.ai/v0/",
        api_key="YOUR_UNIFY_KEY"
    )

    stream = client.chat.completions.create(
        model="mistral-7b-instruct-v0.3@fireworks-ai",
        messages=[{"role": "user", "content": "Say hi."}],
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")

Remember that the :code:`model` field needs to contain a string of the form :code:`model@provider`.

OpenAI NodeJS Package
^^^^^^^^^^^^^^^^^^^^^
Likewise, if you have existing code that uses the OpenAI NodeJS package, it's straightforward to try out our API.

.. code-block:: javascript

    const openai = new OpenAI({
      baseUrl: "https://api.unify.ai/v0/",
      apiKey: "YOUR_UNIFY_KEY"
    });

    const stream = await openai.chat.completions.create({
      model: "mistral-7b-instruct-v0.3@fireworks-ai",
      messages: [{"role": "user", "content": "Say hi."}],
      stream: true
    });

Again, remember that the :code:`model` field needs to contain a string of the form :code:`model@provider`.

Billing
-------
You only have to manage the balance and billing details for your Unify account, and we handle the spending with each provider behind the scenes.

You can see your balance, top-up your balance, and set automatic refill on the `billing page <https://console.unify.ai/billing>`_.

You can get your current credit balance with a HTTP request:

.. code-block::

    curl -X 'GET' \
    'https://api.unify.ai/v0/get_credits' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY'

which will return something like:

.. code-block::

    {
    "id": "your_user_id",
    "credits": 232.32
    }

Advanced features
-----------------
Custom endpoints
^^^^^^^^^^^^^^^^^
If you have a custom model which is deployed as an endpoint on (for example a fine-tuned model with OpenAI or Together AI) you can `add your own custom endpoint <https://console.unify.ai/endpoints>`_.

To create a custom endpoint, you need the Endpoint URL and the relevant API key. You can query a custom endpoint using the model string :code:`<endpoint-name>@custom`

LLM Fallbacks
^^^^^^^^^^^^^^
Sometimes individual providers have outages, which can disrupt live workflows in production. 

To combat this, set a list of fallback models, so if one provider is down or fails for some reason, the request will go to the next model on the list, and so on, until either the request succeeds, or the end of the list is reached.

To specify the list of fallback models, use :code:`->` between individual model tags, so the model string becomes :code:`model_a@provider_a->model_b@provider_b`.

There is no limit on the number of models that can be specified. The :code:`model` field in the response contains the model and provider that the request actually went to.
