Python Client for Google Cloud Data Catalog API (`Alpha`_)
==========================================================

`Google Cloud Data Catalog API`_: A fully managed and highly scalable data discovery and metadata management
service.

- `Client Library Documentation`_
- `Product Documentation`_

.. _Alpha: https://github.com/googleapis/google-cloud-python/blob/master/README.rst
.. _Google Cloud Data Catalog API: https://cloud.google.com/datacatalog
.. _Client Library Documentation: https://googleapis.github.io/google-cloud-python/latest/datacatalog/usage.html
.. _Product Documentation:  https://cloud.google.com/datacatalog

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Google Cloud Data Catalog API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Google Cloud Data Catalog API.:  https://cloud.google.com/datacatalog
.. _Setup Authentication.: https://googleapis.github.io/google-cloud-python/latest/core/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-datacatalog


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-datacatalog

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Google Cloud Data Catalog API
   API to see other available methods on the client.
-  Read the `Google Cloud Data Catalog API Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `repository’s main README`_ to see the full list of Cloud
   APIs that we cover.

.. _Google Cloud Data Catalog API Product documentation:  https://cloud.google.com/datacatalog
.. _repository’s main README: https://github.com/googleapis/google-cloud-python/blob/master/README.rst

Api Reference
-------------
.. toctree::
    :maxdepth: 2

    gapic/v1beta1/api
    gapic/v1beta1/types