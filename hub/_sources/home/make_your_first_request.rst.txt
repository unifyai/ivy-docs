Make your First Request
=======================

Before starting to make requests, you will need two things:

#. **A Unify API Key**. If you don't have one yet, you can follow the instructions in
   `Getting Access <https://unify.ai/docs/hub/home/getting_access.html>`_ to generate it.

#. **A model ID**. You can find the model you want to query using the
   `Hub web interface. <https://unify.ai/hub>`_ For this example, we will use the :code:`llama-2-7b-chat`
   model, hosted in :code:`anyscale`. We (Unify) are managing this model, so we can refer to it using only its
   name (as explained `here! <https://unify.ai/docs/hub/concepts/models.html>`_)

Using the :code:`inference` Endpoint
------------------------------------

All models, independently of the task, can be queried through the :code:`inference` endpoint. The API reference for this is
`here. <https://unify.ai/docs/hub/reference/endpoints.html#post-query>`_

In this case, you will have to specify the :code:`model` and the :code:`provider` that you want to use. In our case,
this are :code:`llama-2-7b-chat` and :code:`anyscale`. Additionaly, you'll have to pass the model :code:`arguments`.
For each model, the available :code:`arguments` may vary, you can always double check them in the corresponding model page.

In the header, you will need to include the **Unify API Key** that is associated with your account.

.. note::
    This is just an HTTP POST request, you can interact with the Hub using your preferred language!

Using **cURL**, the request would look like this:

.. code-block:: bash

    curl -X POST "https://api.unify.ai/v0/inference" \
        -H "accept: application/json" \
        -H "Authorization: Bearer YOUR_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
            "model": "llama-2-7b-chat",
            "provider": "anyscale",
            "arguments": {
                "messages": [{
                    "role": "user",
                    "content": "Explain who Newton was and his entire theory of gravitation. Give a long detailed response please and explain all of his achievements"
                }],
                "temperature": 0.5,
                "max_tokens": 1000,
                "stream": true
            }
        }'

If you are using **Python**, you can use the :code:`requests` library to query the model:

.. code-block:: python

    import requests

    url = "https://api.unify.ai/v0/inference"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
    }

    payload = {
        "model": "llama-2-7b-chat",
        "provider": "anyscale",
        "arguments": {
            "messages": [{
                "role": "user",
                "content": "Explain who Newton was and his entire theory of gravitation. Give a long detailed response please and explain all of his achievements"
            }],
            "temperature": 0.5,
            "max_tokens": 1000,
            "stream": True,
        }
    }

    response = requests.post(url, json=payload, headers=headers, stream=True)

    print(response.status_code)

    if response.status_code == 200:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                print(chunk.decode("utf-8"))
    else:
        print(response.text)


Using the OpenAI API Format
---------------------------

We also support the OpenAI API format for :code:`text-generation` models. More specifically, the :code:`/chat/completions` endpoint.
The docs for this endpoint are available `here. <https://unify.ai/docs/hub/reference/endpoints.html#post-chat-completions>`_

This API format wouldn't normally allow you to choose between providers for a given model. To bypass this limitation, the model
name should have the format :code:`<uploaded_by>/<model_name>@<provider_name>`. For example, if :code:`john_doe` uploads a
:code:`llama-2-7b-chat` model and we want to query the endpoint that has been deployed in replicate, we would have to use
:code:`john_doe/llama-2-7b-chat@replicate` as the model id in the OpenAI API. In this case, there is no username, so we will
simply use :code:`llama-2-7b-chat@replicate`.

This is again just an HTTP endpoint, so you can query it using **cURL**:

.. code-block:: bash

    curl -X 'POST' \
        'https://api.unify.ai/v0/chat/completions' \
        -H 'accept: application/json' \
        -H 'Authorization: Bearer YOUR_API_KEY' \
        -H 'Content-Type: application/json' \
        -d '{
        "model": "llama-2-7b-chat@anyscale",
            "messages": [{
                "role": "user",
                "content": "Explain who Newton was and his entire theory of gravitation. Give a long detailed response please and explain all of his achievements"
            }],
            "stream": true
        }'

Or using **Python**:

.. code-block:: python

    import requests

    url = "https://api.unify.ai/v0/chat/completions"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY",
    }

    payload = {
        "model": "llama-2-7b-chat@anyscale",
        "messages": [
            {
                "role": "user",
                "content": "Explain who Newton was and his entire theory of gravitation. Give a long detailed response please and explain all of his achievements"
            }],
        "stream": True
    }

    response = requests.post(url, json=payload, headers=headers, stream=True)

    print(response.status_code)

    if response.status_code == 200:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                print(chunk.decode("utf-8"))
    else:
        print(response.text)

Or any other language!
