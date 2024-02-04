Providers
=========

Another one of the main concepts in the Hub is the **provider**. Let's dive into it 🤿

What is a Provider?
-------------------

You can think of a provider as a end-to-end deployment stack. Each provider comes with its unique set of features, performance capabilities,
pricing, and so on. The Hub exposes an HTTP endpoint for every individual providers, allowing you to query the one
that best fits your requirements while using a consistent request format and the same `API key <https://unify.ai/docs/hub/home/getting_access.html>`_.

If you look at the page of `one of the models <http://unify.ai/hub/llama-2-70b-chat>`_, you'll find the different
providers and endpoints where this model is available (with their corresponding benchmark results!).

..
  TODO: Image of the dashboard

Types of Providers
------------------

We can categorze providers into various types, but fear not! Despite their differences under the hood, your developer experience
is the same across all of them. The boundaries may sometimes seem a bit blurry here, but the following is a good mental model.

Regardless of the services powering the endpoint, it's important to highlight that the Hub benchmarks them equally. This ensures that
you have the flexibility the query the most suitable one for your specific use case without any kind of vendor lock-in.

Public endpoints
^^^^^^^^^^^^^^^^
When working with popular models such as LLMs or Image Generation pipelines, it's easy to find public endpoints offering inference
as a service. Providers such as `stability.ai <https://stability.ai/>`_, `Anyscale <https://www.anyscale.com/endpoints>`_, or
`together.ai <https://www.together.ai/>`_ expose APIs to query the models they are hosting in a straighforward manner, eliminating
the need for any deployment. As mentioned earlier, this type of endpoints are only available in the `models managed by
Unify <https://unify.ai/docs/hub/concepts/models.html#models-uploaded-by-us>`_, and not in those uploaded by users.

Deployment services
^^^^^^^^^^^^^^^^^^^
On the other hand, there are several companies and services operating one level below, allowing developers to select or load a specific model
and deploy it in the cloud. Similarly, these services expose the model through an endpoint, often passing on the hourly cost of the instance
where the model is executed to the user. Providers such as `OctoML <https://octoml.ai/>`_, `Replicate <https://replicate.com/>`_ or
the `Hugging Face Inference Endpoints <https://huggingface.co/inference-endpoints>`_ fall under this category.

Managed Infrastructure
^^^^^^^^^^^^^^^^^^^^^^
Last but certainly not least, we can go lower in the stack. Here we don't go through companies building deployment services, which reduces
the cost of running the endpoints. Instead, we build our own infrastructure. For instance, when deploying a quantizied model using CPU instances
and a model-specific inference server, or leveraging specialized hardware like the Intel Gaudi 2 accelerators, manual infrastructure
management becomes necessary.

In these scenarios, we mix and match specialized tools to optimize model deployment at various stages of the stack, ultimately exposing them to you
through endpoints, just like the two other groups.


Round Up
--------

We have seen what a provider is and how different types are all unified as part of the Hub. We have also mentioned the benchmarks
a few times now, so let's talk about them in more detail in the next section.
