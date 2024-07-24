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
  :caption: Concepts

  concepts/unify_api.rst
  concepts/benchmarks.rst
  concepts/router.rst

..  reference/images.rst

.. autosummary::
  :toctree: docs/unify
  :template: top_level_toc_recursive.rst
  :recursive:
  :hide-table:
  :caption: API

  unify

.. toctree::
  :hidden:
  :maxdepth: -1
  :caption: Console

  console/connecting_stack.rst
  console/running_benchmarks.rst
  console/building_router.rst

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
  :caption: On-Prem

  on_prem/on_prem_access
  on_prem/sso.rst
