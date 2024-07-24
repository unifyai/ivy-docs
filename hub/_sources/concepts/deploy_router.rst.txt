Deploying a router
==================

In this section, we'll learn how to use the Unify router through the API.

.. note::
    If you haven't done so, we recommend you learn how to `make a request <https://unify.ai/docs/api/first_request.html>`_ first to get familiar with using the Unify API.

Using the base router
---------------------

Optimizing a metric
^^^^^^^^^^^^^^^^^^^

When making requests, you can leverage the information from the `benchmark interface <https://unify.ai/docs/concepts/benchmarks.html>`_
to automatically route to the best performing provider for the metric you choose. 

Benchmark values change over time, so dynamically routing ensures you always get the best option without having to monitor the data yourself.

To use the base router, you only need to change the provier name to one of the supported configurations. Currently, we support the following configs:

- :code:`lowest-input-cost` / :code:`input-cost`
- :code:`lowest-output-cost` / :code:`output-cost`
- :code:`lowest-itl` / :code:`itl`
- :code:`lowest-ttft` / :code:`ttft`
- :code:`highest-tks-per-sec` / :code:`tks-per-sec`

For e.g, with the Python package, we can route to the lowest TTFT endpoints as follows:

.. code-block:: python

    import os
    from unify import Unify

    # Assuming you added "UNIFY_KEY" to your environment variables. Otherwise you would specify the api_key argument.
    unify = Unify("mistral-7b-instruct-v0.3@lowest-ttft")

    response = unify.generate("Explain who Newton was and his entire theory of gravitation. Give a long detailed response please and explain all of his achievements")


Defining thresholds
^^^^^^^^^^^^^^^^^^^

Additionally, you have the option to include multiple thresholds for other metrics in each configuration.

This feature enables you to get, for example, the highest tokens per second (:code:`highest-tks-per-sec`) for any provider whose :code:`ttft` is lower than a specific threshold. To set this up, just append :code:`<[float][metric]` to your preferred mode when specifying a provider. To keep things simple, we have added aliases for :code:`output-cost` (:code:`oc`), :code:`input-cost` (:code:`ic`) and :code:`output-tks-per-sec` (:code:`ots`). 

Let's illustrate this with some examples:

- :code:`lowest-itl<0.5input-cost` - In this case, the request will be routed to the provider with the lowest
  Inter-Token-Latency that has an Input Cost smaller than 0.5 credits per million tokens.
- :code:`highest-tks-per-sec<1output-cost` - Likewise, in this scenario, the request will be directed to the provider
  offering the highest Output Tokens per Second, provided their cost is below 1 credit per million tokens.
- :code:`ttft<0.5ic<15itl` - Now we have something similar to the first example, but we are using :code:`ic` as
  an alias to :code:`input-cost`, and we have also added :code:`<15itl` to only consider endpoints
  that have an Inter-Token-Latency of less than 15 ms.

Depending on the specified threshold, there might be scenarios where no providers meet the criteria,
rendering the request unfulfillable. In such cases, the API response will be a 404 error with the corresponding
explanation. You can detect this and change your policy doing something like:


.. code-block:: python

    import os
    from unify import Unify

    prompt = "Explain who Newton was and his entire theory of gravitation. Give a long detailed response please and explain all of his achievements"

    # This won't work since no provider has this price! (yet?)
    unify = Unify("mistral-7b-instruct-v0.3@lowest-itl<0.001ic")

    response = unify.generate(prompt)

    if response.status_code == 404:
      # We'll get the cheapest endpoint as a fallback
      payload["model"] = "mistral-7b-instruct-v0.3@lowest-input-cost"
      response = unify.generate(prompt)


.. raw:: html

    <div style="text-align: center;">
      <iframe width="420" height="315" allow="fullscreen;"
        src="https://www.youtube.com/embed/SBwr32iSU8Q?si=Rj3xknJEg0765Psb" class="video">
      </iframe>            
    </div>

Using a custom router
---------------------

If you `trained a custom router <https://unify.ai/docs/interfaces/building_router.html>`_, you can deploy it with the Unify API much like using any other endpoint. Assuming we want to deploy the custom router we trained before, we can use the configuration Id in the same API call code to send our prompts to our custom router as follows:

.. code-block:: python

    import os
    from unify import Unify

    # Assuming you added "UNIFY_KEY" to your environment variables. Otherwise you would specify the api_key argument.
    unify = Unify("gpt-claude-llama3-calls->no-anthropic_8.28e-03_4.66e-0.4_1.00e-06@custom")

    response = unify.generate("Explain who Newton was and his entire theory of gravitation. Give a long detailed response please and explain all of his achievements")

.. note::
    You can also query the API with a CuRL request, among others. Just like explained in the first request page.

Round Up
--------

That’s it! You now know how to deploy a router to send your prompts to the best endpoints for the metrics or tasks you care about. You can now start optimizing your LLM applications!
