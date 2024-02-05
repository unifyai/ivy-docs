Build a Chatbot
===============

Now you've made your `first request <https://unify.ai/docs/hub/home/make_your_first_request.html>`_,
you're ready to build a simple chatbot in Python, on top of our unified endpoints!

The Agent
---------

Under the hood, chatbots are very simple to implement. All LLM endpoints are *stateless*,
and therefore the entire conversation history is repeatedly fed as input to the model.
All that is required of the local agent is to store this history, and correctly pass it to the model.

We define a simple chatbot class below, with the only public function being :code:`run`.
The example assumes that your API key is stored in the environment variable :code:`UNIFY_KEY`.

.. code-block:: python

    import os
    import sys
    import openai
    import requests


    class Agent:

        def __init__(self, model: str):
            self._message_history = []
            self._model = model
            self._paused = False
            try:
                self._key = os.environ["UNIFY_KEY"]
            except KeyError:
                raise Exception("Please set your UNIFY_KEY environment variable")
            self._base_url = "https://api.unify.ai/v0/"
            self._headers = {
                "accept": "application/json",
                "Authorization": "Bearer " + self._key,
            }
            self._oai_client = openai.OpenAI(
                base_url=self._base_url,
                api_key=self._key
            )

        def _get_credits(self):
            response = requests.get(self._base_url + "get_credits", headers=self._headers)
            return eval(response.content.decode())["credits"]

        def _process_input(self, inp: str, show_credits: bool):
            pre_credits = self._get_credits()
            self._update_message_history(inp)
            response = self._oai_client.chat.completions.create(
                model=self._model,
                messages=self._message_history,
                stream=True
            )
            words = ''
            for tok in response:
                delta = tok.choices[0].delta
                if not delta:
                    self._message_history.append({
                        'role': 'assistant',
                        'content': words
                    })
                    break
                elif delta.content:
                    words += delta.content
                    yield delta.content
                else:
                    continue
            if show_credits:
                sys.stdout.write("\n(spent {:.6f} credits)".format(pre_credits - self._get_credits()))

        def _update_message_history(self, inp):
            self._message_history.append({
                'role': 'user',
                'content': inp
            })

        @property
        def model(self):
            return self._model

        @model.setter
        def model(self, value):
            error_message = "model string must use the OpenAI format: <uploaded_by>/<model_name>@<provider_name>"
            assert type(value) is str, error_message
            model_name, provider_name = value.split('/')[-1].split("@")
            assert len(model_name) and len(provider_name), error_message
            self._model = value

        # Public Methods

        def clear_chat_history(self):
            self._message_history.clear()

        def run(self, show_credits: bool = False):
            if not self._paused:
                sys.stdout.write("Let's have a chat. (Enter `pause` to pause and `quit` to exit)\n")
                self.clear_chat_history()
            else:
                sys.stdout.write("Welcome back! (Remember, enter `pause` to pause and `quit` to exit)\n")
            self._paused = False
            while True:
                sys.stdout.write('> ')
                inp = input()
                if inp == 'quit':
                    self.clear_chat_history()
                    break
                elif inp == 'pause':
                    self._paused = True
                    break
                for word in self._process_input(inp, show_credits):
                    sys.stdout.write(word)
                    sys.stdout.flush()
                sys.stdout.write('\n')





Let's Chat!
-----------

Provided our environment variable :code:`UNIFY_KEY` is set correctly,
we can now simply instantiate this agent and chat with it, using the format
:code:`<uploaded_by>/<model_name>@<provider_name>` as per the `OpenAI API Format
<https://unify.ai/docs/hub/home/make_your_first_request.html#using-the-openai-api-format>`_,
like so:

.. code-block:: python

    agent = Agent("llama-2-70b-chat@anyscale")
    agent.run()

This will start an interactive session, where you can converse with the model:

.. code-block::

    Let's have a chat. (Enter `pause` to pause and `quit` to exit)
    > Hi, nice to meet you. My name is Foo Barrymore, and I am 25 years old.
     Nice to meet you too, Foo! I'm just an AI, I don't have a personal name, but I'm here to help you with any questions or concerns you might have. How has your day been so far?
    > How old am I?
     You are 25 years old, as you mentioned in your introduction.
    > Your memory is astounding
     Thank you! I'm glad to hear that.

We also included an option to print the credits spent after each interaction in the
simple model above. This option is set in the constructor,
but it can be overwritten during the run command, as follows:

.. code-block:: python

    agent.run(show_credits=True)

Each response from the chatbot will then be appended with the credits spent:

.. code-block::

    Let's have a chat. (Enter `pause` to pause and `quit` to exit)
    > What is the capital of Spain?
     The capital of Spain is Madrid.
    (spent 0.000014 credits)

You can also switch the provider half-way through the conversation easily.
We can start with a small model for answering simple questions, such as fact recall,
and then move to a larger model for a more complex task, such as creative writing.

.. code-block:: python

    agent = Agent("llama-2-7b-chat@anyscale")
    agent.run(show_credits=True)

.. code-block::

    Let's have a chat. (Enter `pause` to pause and `quit` to exit)
    > What is the capital of Portugal?
     The capital of Portugal is Lisbon.
    (spent 0.000002 credits)
    > My name is José Mourinho.
     Okay. Nice to meet you José.
    (spent 0.000002 credits)
    > pause

.. code-block:: python

    agent.model = "llama-2-70b-chat@anyscale"
    agent.run(show_credits=True)

.. code-block::

    Welcome back! (Remember, enter `pause` to pause and `quit` to exit)
    > Please write me a poem about my life in Lisbon, using my name in the poem.
     Sure, here's a short poem about your life in Lisbon, using your name:

    José Mourinho, a man of great renown,
    In Lisbon, a city of ancient crown.
    You walked its streets, with purpose and drive,
    A man on a mission, with a burning fire inside.

    You breathed in the scent of the ocean's spray,
    And felt the warmth of the sun on your face each day.
    You marveled at the beauty of the city's old town,
    And felt at home, in this place you'd found.

    You savored the flavors of the local cuisine,
    And quenched your thirst with a glass of fine wine.
    You listened to the music of the street performers,
    And felt the rhythm of the city's vibrant pulse.

    José Mourinho, a man of great ambition,
    In Lisbon, a city of endless tradition.
    You found your place, in this ancient land,
    And made your mark, with a helping hand.

    For in Lisbon, you found your home,
    A place where your heart would forever roam.
    José Mourinho, a man of great fame,
    In Lisbon, a city that would forever bear your name.
    (spent 0.000260 credits)

Switching between providers mid-conversation makes it much easier to maximize quality,
maximize runtime performance based on the latest metrics, and also save on costs!
