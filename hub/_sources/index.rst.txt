.. title:: Home

.. include:: home/home.rst

.. toctree::
  :hidden:
  :maxdepth: -1

  Welcome to Unify! <self>
  API Reference <https://api.unify.ai/v0/docs>

.. toctree::
  :hidden:
  :maxdepth: -1
  :caption: API

  api/unify_api.rst
  api/benchmarks.rst
  api/router.rst

..  reference/images.rst

.. autosummary::
  :toctree: docs/unify
  :template: top_level_toc_recursive.rst
  :recursive:
  :hide-table:
  :caption: Docs

  unify

.. toctree::
  :hidden:
  :maxdepth: 4
  :caption: Demos

  demos/unify.rst
  demos/langchain.rst
  demos/llamaindex.rst

.. toctree::
  :hidden:
  :maxdepth: -1
  :caption: Interfaces

  interfaces/connecting_stack.rst
  interfaces/running_benchmarks.rst
  interfaces/building_router.rst

..
  .. toctree::
    :hidden:
    :maxdepth: -1
    :caption: Tools

    tools/openapi.rst
    tools/python_library.rst

.. toctree::
  :hidden:
  :maxdepth: -1
  :caption: Concepts

  concepts/endpoints.rst
  concepts/benchmarks.rst
  concepts/routing.rst
..  concepts/on_prem_images.rst
