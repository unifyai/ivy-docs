Benchmarking
=============

When comparing LLMs, there is a constant tradeoff to make between quality, cost and latency. Stronger models are (in general) slower and more expensive - and sometimes overkill for the task at hand. Complicating matters further, new models are released weekly, each claiming to be state-of-the-art.

Benchmarking on your data lets you see how each of the different models perform on your task.

.. image:: ../images/benchmarks.png
  :align: center
  :width: 800
  :alt: Benchmarks Image.

You can compare how quality relates to cost and latency, with live stats pulled from our `runtime benchmarks <https://unify.ai/benchmarks>`_.

When new models come out, simply re-run the benchmark to see how they perform on your task.


Preparing your dataset
-----------------------
First create a dataset which is representative of the task you want to evaluate.
You will need a list of prompts, optionally including a reference, *gold-standard* answer. Datasets containing reference answers tend to get more accurate benchmarks.

The file itself should be in JSONL format, with one entry per line, as in the example below.

.. code-block::

    {"prompt": "This is the first prompt", "ref_answer": "This is the first reference answer"}
    {"prompt": "This is the second prompt", "ref_answer": "This is the second reference answer"}

Use at least 50 prompts to get the most accurate results. Currently there is an maximum limit of 500 prompts, for most tasks we don’t tend to see much extra detail past ~250.

Benchmarking your dataset
-------------------------
In `your dashboard <https://console.unify.ai/dashboard>`_, clicking :code:`Select benchmark` and then :code:`Benchmark your prompts` opens the interface to upload a dataset.

When the benchmark finishes, you'll receive an email, and the graph will be displayed in your `dashboard <https://console.unify.ai/dashboard>`_.

The x-axis can be set to represent :code:`cost`, :code:`time-to-first-token`, or :code:`inter-token latency`, and on either a linear or log scale.

How does it work?
^^^^^^^^^^^^^^^^^^
Currently, we use gpt4o-as-a-judge (cf. https://arxiv.org/abs/2306.05685), to evaluate the quality of each model’s responses.


