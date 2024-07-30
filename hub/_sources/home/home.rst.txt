Welcome to Unify!
=================

We're on a mission to unify and simplify the LLM landscape. Unify lets you:

* **🔑 Use any LLM from any Provider**: With a single interface, you can use all LLMs from all providers by simply changing one string. No need to manage several API keys or handle different input-output formats. Unify handles all of that for you!

* **📊 Improve LLM Performance**: Add your own custom tests and evals, and benchmark your own prompts on all models and providers. Comparing quality, cost and speed, and iterate on your system prompt until all test cases pass, and you can deploy your app!

* **🔀 Route to the Best LLM**: Improve quality, cost and speed by routing to the perfect model and provider for each individual prompt.

Getting Started
---------------

It's easiest to get started using our Python client. Simply install the package:

.. code-block:: bash

    pip install unifyai

`Sign up <https://console.unify.ai>`_ to get your API key. Then you're ready to go! 🚀

.. code-block:: python

    import unify
    client = unify.Unify("gpt-4o@openai", api_key=<your_key>)
    client.generate("hello world!")

You can also save your key as :code:`UNIFY_KEY` in your environment variables, avoiding the need to use the :code:`api_key` argument.

You can list all available endpoints like so, any of which can be passed into the client:

.. code-block:: python

    import unify
    import random
    endpoints = unify.utils.list_endpoints()
    endpoint = random.choice(endpoints)
    client = unify.Unify(endpoint)
    client.generate("hello world!")

That's it! You now have all models and providers at your fingertips ✨