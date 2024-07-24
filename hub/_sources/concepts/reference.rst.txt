API Reference
=============

Welcome to the Endpoints API reference!
This page is your go-to resource when it comes to learning about the different Unify API endpoints you can interact with.

.. note::
  If you don't have one yet, `Sign Up <https://console.unify.ai>`_ first to get your API key.

-----

GET /get_credits
----------------

**Get Current Credit Balance**

Retrieve the credit balance for the authenticated account.

**Example Request (curl)**

.. code-block:: bash

  curl -X 'GET' \
    'https://api.unify.ai/v0/get_credits' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY'


**Responses**

- **200 OK**

  Successful operation.

  **Response**
   | Credits balance in the account associated with the API key used for the request.

  **Example Response**

  .. code-block:: bash

    {
      "id": "corresponding_user_id",
      "credits": 232.32
    }

- **401 Unauthorized**

  Invalid API key.

  **Example Response**

  .. code-block:: bash

    {
      "error": "Invalid API key"
    }

- **403 Forbidden**

  Not authenticated.

  **Example Response**

  .. code-block:: bash

    {
      "detail": "Not authenticated"
    }

-----


POST /chat/completions
----------------------

**Query a Text-Generation Model hosted in a given Provider using the OpenAI API format**

Send a given input to the specified model hosted in the specified provider.
This endpoint follows the OpenAI specification for text completion, which is available
`here. <https://platform.openai.com/docs/api-reference/chat/create>`_

To specify the provider, make sure to append its name after the model id using :code:`@`.

**Example Request (curl)**

.. code-block:: bash

    curl -X 'POST' \
    'https://api.unify.ai/v0/chat/completions' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -H 'Content-Type: application/json' \
    -d '{
    "model": "llama-3-8b-chat@anyscale",
    "messages": [
        {
            "role": "user",
            "content": "Explain who Newton was and his entire theory of gravitation. Give a long detailed response please and explain all of his achievements"
        }
    ],
    "stream": false
    }'

**Responses**

- **200 OK**

  Successful operation.

  **Response**
   | Response following the schema of the chat completion object from OpenAI, defined `here. <https://platform.openai.com/docs/api-reference/chat/object>`_

  **Example Response**

  .. code-block:: bash

    {
        'model': 'llama-3-8b-chat@anyscale',
        'created': 1704999905,
        'id': 'meta-llama/Llama-3-8b-chat-hf-xR868C-T4Z-TKLtfXxZSvq57WmhxB34El5ZUuXsAtFU',
        'object': 'chat.completion',
        'usage': {
            'completion_tokens': 512,
            'prompt_tokens': 34,
            'total_tokens': 546
            },
        'choices': [{
            'finish_reason': 'length',
            'index': 0,
            'message': {
                'content': 'Isaac Newton (1643-1727) was a...',
                'role': 'assistant'
            }
        }]
    }

- **401 Unauthorized**

  Invalid API key.

  **Example Response**

  .. code-block:: bash

    {
      "error": "Invalid API key"
    }

- **422 Unprocessable Entity**

  Invalid arguments. The provided arguments don't correspond to the specified model.

  **Example Response**

  .. code-block:: bash

    {
      "error": "The provided arguments don't correspond to the specified model."
    }

-----
