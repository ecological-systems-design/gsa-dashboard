.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

==============================================================
Global Sensitivity Analysis of Life Cycle Assessment Dashboard
==============================================================

About this app
==============
This dashboard attempts to combine the motivation behind Global Sensitivity Analysis
of Life Cycle Assessment, with necessary computations and visualization of the results -
all in one place.

The dashboard has been implemented with `Dash <https://dash.plotly.com/>`_ - framework for
building data apps that was written on top of Plotly.js and React.js. Non enterprise
version of Dash has the `MIT license <https://github.com/plotly/dash/blob/dev/LICENSE>`_.

Note that the app is not well tested, but it does work on the example Brightway project
"Uncertainties Chaerhan" that you can import using
`dev/import_chaerhan.py <https://github.com/aleksandra-kim/gsa_dash/blob/main/dev/import_chaerhan.py>`_

Presentation video
==================
`Video <https://youtu.be/wiyNC4-BKwk>`_ submitted for the `Depart de Sentier visualization contest <https://github.com/Depart-de-Sentier/visualization-contest-2022>`_.

Visualizations
==============

.. image:: https://raw.githubusercontent.com/aleksandra-kim/gsa_dash/main/gsa_dash/images/mc.png
  :width: 100%
  :alt: Monte Carlo simulations

.. image:: https://raw.githubusercontent.com/aleksandra-kim/gsa_dash/main/gsa_dash/images/gsa.png
  :width: 100%
  :alt: Global sensitivity analysis

How to run this app
===================
1. Clone the repository.
2. Open terminal inside the root folder.
3. Create and activate new virtual environment. For example, with ``conda``:

.. code-block:: bash

   $ conda create -y -n gsa-dashboard python=3.10
   $ conda activate gsa-dashboard

4. Install the packages:

.. code-block:: bash

   $ conda install -y -c conda-forge -c cmutel brightway25
   $ conda install -y -c conda-forge intel-openmp=2021.4
   $ conda install -y -c anaconda scikit-learn
   $ conda install -y -c plotly plotly=5.13.0
   $ conda install -y -c conda-forge dash dash-bootstrap-components celery
   $ pip install "dash[diskcache]"

5. Run the app:

.. code-block:: bash

   $ python gsa_dash/app.py

6. View the app by opening `<http://127.0.0.1:8050>`_ in a browser.

7. Stop the program with ``CTRL+C`` or ``CTRL+Z`` commands.

8. If you run it again, and see the message Port 8050 is in use by another program,
then find the PID of the process and kill it (very elegant, I know):

.. code-block:: bash

   $ lsof -i tcp:8050
   $ kill -9 <PID>

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.4. For details and usage
information on PyScaffold see https://pyscaffold.org/.
