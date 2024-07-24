Routing
========
Learn how to use the LLM routing endpoints.

What is LLM routing?
---------------------

LLM routing allows you to be flexible about which model handles each prompt. Flexibility can be advantageous for several reasons:

1. Small models are (in general) faster and cheaper, whereas bigger models are more capable.
2. Tasks often contain a range of difficulties.
3. Different providers have different latencies, and these **change** over time.
4. New models come out every week, each having different strengths and weaknesses.

LLM routing provides:

- Faster and cheaper responses when a smaller model is capable of answering
- Continuous improvement: ‘riding the wave’ of new model releases
- Ability to maximise throughput or minimise latency based on live runtime statistics

Foundation router
------------------
We have trained a general-purpose router on a wide variety of prompts. 
To query the foundation router, select a green star on the graph on the `chat interface <https://unify.ai/chat>`_ and copy the router string.

For example :code:`router@q:1|c:4.65e-03|t:2.08e-05|i:2.07e-03`

The parameters stand for the relative weighing of: quality, cost, time-to-first-token, and inter-token latency. They are completely customizable, but it’s most meaningful to select a configuration directly from the graph.


Filtering endpoints
^^^^^^^^^^^^^^^^^^^^
You can restrict the model and providers that are routed between, by specifying them in the router string as follows:

:code:`router@models:model1,model2,model3|providers:provider1,provider2`


Maximising throughput
^^^^^^^^^^^^^^^^^^^^^^
When using the router, if provider specific rate-limits are hit then the router moves on to the next best model. This means that you can get much higher throughput than is available from a single provider.


Fine-tuned custom router
-------------------------
We’ve found that the best results for LLM routing come when you train on similar prompts to those that are going to be used in production.
To train a custom router, you need to:

- Prepare a training dataset
- Train a router, and visualise the results
- Query your trained router

Preparing a dataset
^^^^^^^^^^^^^^^^^^^^
The format for the dataset is the same as the one used in `benchmarking <https://unify.ai/docs/api/benchmarks.html>`_, i.e.
a JSONL file with entries of the form :code:`{"prompt": xxx, "ref_answer": yyy}`. Reference answers are optional, but improve accuracy of the final system.

Training a router (beta)
^^^^^^^^^^^^^^^^^^^^^^^^
In your `dashboard <https://console.unify.ai/dashboard>`_, click :code:`Select Benchmark` and then :code:`Train a router`, to upload your dataset.

After uploading the dataset, a router will be trained. Once it's finished training, you'll receive an email, and the graph will be displayed in your `dashboard <https://console.unify.ai/dashboard>`_.
Here you will be able to choose a router configuration, and copy the router string to use in the API.