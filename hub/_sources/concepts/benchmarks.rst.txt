Benchmarks
==========

The main goal of the Hub is to allow you to use the endpoint (and model!) that better suits your use case. This is not a trivial decision to make, and therefore it needs to be made based on data.

We have the goal of benchmarking every single inference endpoint exposing LLMs out there, so being transparent with the way we do these measurements is necessary to avoid unfair comparisons and objectiveness.

That's why we want to be crystal clear with our methodology ⬇️ and our code, which is available in `this repo <https://github.com/unifyai/aibench-llm-endpoints>`_!

----

Design Principles
=================

- **Community-driven:** We invite everyone to audit or improve the logic and the code. We are building these benchmarks for the community, so contributions and discussions around them are more than welcome!

- **User-centric:** The logic we use is subject to certain factors external to the model. In the case of publicly available endpoints, how different providers set up their infrastructure (e.g. autoscaling), or the amount of requests they are receiving at the moment of the benchmark will have an effect on the measurements. While these details may distort the efficiency and optimizations behind certain endpoints, they ultimately reflect in the experience for an external user. This benchmark is not designed to measure model performance internally in a controlled environment, but to measure performance from a user perspective

- **Model and Provider-agnostic:** While some metrics are more relevant to certain scenarios (e.g. cold start time in model endpoints that scale to zero), we try to make as few assumptions as possible on the providers or technologies being benchmarked. We only assume that endpoints take a string as the input and return a streaming response.

----

Methodology
============

Tokenizer
---------

To avoid biases towards any model-specific tokenizer, we calculate all metrics using the same tokenizer across different models. We have chosen the `cl100k_base` tokenizer from OpenAI's `tiktoken <https://github.com/openai/tiktoken>`_ library for this since it’s MIT licensed and already widely adopted by the community.

Inputs and Outputs
-------------------

To fairly assess optimizations such as speculative decoding, we use real text as the input and avoid using randomly generated data. The length of the input affects prefill time and therefore can affect the responsiveness of the system. To account for this, we run the benchmark with two input regimes.

- Short inputs: Using sentences with an average length of 200 tokens and a standard deviation of 20.
- Long inputs: Using sentences with an average length of 1000 tokens and a standard deviation of 100.

To build these clusters, we programmatically select sentences from `BookCorpus <https://huggingface.co/datasets/bookcorpus>`_ and create two subsets of it. For instruct/chat models to answer appropriately and ensure a long enough response, we preface each prompt with :code:`Repeat the following lines <#> times without generating the EOS token earlier than that`, where :code:`<#>` is randomly sampled.

For the outputs, we use randomized discrete values from the same distributions (i.e. N(200, 20) for short inputs and N(1000, 100) for long ones) to cap the number of tokens in the output. This ensures variable output length, which is necessary to consider algorithms such as Paged Attention or Dynamic Batching.

When running one benchmark across different endpoints, we seed each runner with the same initial value, so that the inputs are the same for all endpoints.

Computation
------------

To execute the benchmarks, we run three processes periodically from three different regions: **Hong Kong, Belgium and Iowa**. Each one of these processes is triggered every three hours and benchmarks every available endpoint.

To evaluate how endpoints respond to higher-volume traffic, we conduct the benchmarks under two different load scenarios: **1 single request and 20 concurrent requests**..

Accounting for the different input policies, we run a total of 4 benchmarks for each endpoint every time a region benchmark is triggered.


Metrics
-------

Several key metrics are captured and calculated during the benchmarking process:

- **Time to First Token (TTFT):** Time between request initiation and the arrival of the first streaming response packet. TTFT directly reflects the prompt processing speed, offering insights into the efficiency of the model's initial response. A lower TTFT signifies quicker engagement, which is crucial for applications that require dynamic interactions or real-time feedback.

- **End to End Latency:** Time between request initiation and the arrival of the final packet in the streaming response. This metric provides a holistic view of the response time, including processing and transmission.

- **Inter Token Latency (ITL):** Average time between consecutive tokens in the response. We compute this as :code:`(End to End Latency) / (Output Tokens - 1)`.  ITL provides valuable information about the pacing of token generation and the overall temporal dynamics within the model's output. As expected, a lower ITL signifies a more cohesive and fluid generation of tokens, which contributes to a more seamless and human-like interaction with the model.

- **Number of Output Tokens per Second:** Relation between the number of tokens generated and the time taken. We don't consider the TTFT here, so this is equivalent to :code:`1 / ITL`. In this case, a higher Number of Output Tokens per Second means a faster and more productive model output. It's important to note that this is **not** a measurement of the throughput of the inference server since it doesn't account for batched inputs.

- **Cold Start:** Time taken for a server to boot up in environments where the number of active instances can get to zero. We consider a threshold of 15 seconds. What this means is that we do an initial "dumb" request to the endpoint and record its TTFT. If this TTFT is greater than 15 seconds, we measure the time it takes to get the second token. If the ratio between the TTFT and first ITL measurements is at least 10:1, we consider the TTFT to be Cold Start time. Once this process has finished. We start the benchmark process in the warmed-up instance. This metric reflects the time it takes for the system to be ready for processing requests, rendering it essential for users relying on prompt and consistent model responses, allowing you to account for any potential initialization delays in the responses and ensuring a more accurate expectation of the model's responsiveness.

- **Cost**: Last but not least, we present information about the cost of querying the model. This is usually different for the input tokens and the response tokens, so it can be beneficial to choose different models depending on the end task. As an example, to summarize a document, a provider with lower price in the input tokens would be better, even if it comes with a slightly higher price in the output. On the other hand, if you want to generate long-format content, a provider with a lower price per generated token will be the most appropriate option.

Data Presentation
-----------------

When aggregating metrics, particularly in benchmark regimes with multiple concurrent requests, we calculate and present the P90 (90th percentile) value from the set of measurements. We choose the P90 to reduce the influence of extreme values and provide a reliable snapshot of the model's performance.

When applicable, aggregated data is shown both in the plots and the benchmark tables.

Additionally, we also include a MA5 view (Moving Average of the last 5 measurements) in the graphs. This smoothing technique helps mitigate short-term fluctuations and should provide a clearer trend representation over time.

Not computed / No metrics are available yet
*******************************************

In some cases, you will find :code:`Not computed` instead of a value, or even a :code:`No metrics are available yet` message instead of the benchmark data. This basically means that we don't have valid data to show you. Most of the time, this means we have hit a rate limit or there is an internal issue. We try to stay on top of these messages and we are probably working on (1) getting our quotas increased for the specific endpoint/provider or (2) fixing the problem. We'll try to get you the data ASAP!

----

Considerations and Limitations
==============================

We try to tackle some of the more significant limitations of benchmarking inference endpoints. For example, network latency, by running the benchmarks in different regions; or unreliable point-measurements, by continuously benchmarking the endpoints and plotting their trends over time.

However, there are still some relevant considerations to have in mind. Our methodology at the moment is solely focused on performance, which means that we don't look at the output of the models. Nonetheless, even accounting for the public-facing nature of these endpoints (no gibberish allowed!), there might be some implementation differences that affect the output quality, such as quantization/compression of the models, different context window sizes, or different speculative decoding models, among others. We are working towards mitigating this as well, so stay tuned!
