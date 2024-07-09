SSO (Single Sign On)
=======

Steps to use on-prem SSO microservice.

1. Once granted access, run :code:`docker pull unifyai/sso:latest`

2. Then run :code:`docker run -dt -p 8000:8000 –env-file <env_file_path> unifyai/sso:latest`

3. The env file should look like this.

.. code-block:: bash

    DEEPINFRA_API_KEY=
    STABILITY_API_KEY=
    MISTRAL_AI_API_KEY=
    PERPLEXITY_AI_API_KEY=
    ANYSCALE_API_KEY=
    OCTOAI_API_KEY=
    OPENAI_API_KEY=
    TOGETHER_AI_API_KEY=
    REPLICATE_API_KEY=
    LEPTON_AI_API_KEY=
    FIREWORKS_AI_API_KEY=
    ANTHROPIC_API_KEY=
    ###
    VERTEXAI_SERVICE_ACC_JSON=
    VERTEXAI_GCLOUD_PATH=
    VERTEXAI_PROJECT=
    VERTEXAI_LOCATION=

4. Now you have your sso service running locally which you can use like this.
    - Using python + requests
    .. code-block:: python

        import requests
        messages = [{"role": "user", "content": "What's the weather like in San Francisco, Tokyo, and Paris?"}]

        res = requests.post("http://localhost:8000/chat/completions", json={
            "model": "claude-3-haiku@anthropic",
            "messages": messages,
        },).json()

    - Using our python client
    .. code-block:: python

        from unify import Unify
        api = Unify("claude-3-haiku@anthropic", api_key=<RANDOM_KEY_WONT_BE_USED>)
        api.client.base_url = “http://localhost:8000”
        api.generate("What is the meaning of life?")
        

    - Using curl
    .. code-block:: bash

        curl -X 'POST' \
        'http://localhost:8000/chat/completions' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "model": "claude-3-haiku@anthropic",
            "messages": [{
                "role": "user",
                "content": "Explain who Newton was and his entire theory of gravitation. Give a long detailed response please and explain all of his achievements"
            }],
        }'
        




