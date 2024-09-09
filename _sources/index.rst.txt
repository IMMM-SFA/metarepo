|DOI|

.. |DOI| image:: https://zenodo.org/badge/265254045.svg
   :target: https://zenodo.org/doi/10.5281/zenodo.10442485

metarepo
========

.. toctree::
   :maxdepth: 2

``metarepo`` is short for meta-repository, a GitHub repository that contains instructions to reproduce results in a published work. This page contains instructions on how to use this repo as a template for creating your own metarepo.

Purpose
-------

A metarepo creates a single point of access for someone to find
all of the components that were used to create a published work for the
purpose of reproducibility. This repository should contain references to
all minted data and software as well as any ancillary code used to
transform the source data, create figures for your publication, conduct
the experiment, and run the contributing software if applicable.

Lost? Start here
----------------

-  Don't know how to use GitHub? Check out their
   `tutorial <https://docs.github.com/en/get-started/start-your-journey/hello-world>`_.
-  Want a video walk-through of what a metarepo is, why they're
   important, and how to create one?

.. youtube:: 1dJOXdm-Wvc
   :url_parameters: ?start=180
   :privacy_mode:
   :align: center
   :width: 100%

Workflow
--------

These are the big picture steps for how to start from scratch and end up
with a complete metarepo. There are more in depth steps below.

A. `Use the template to initialize your own metarepo <#a-use-the-template-to-initialize-your-own-metarepo>`_

B. `Edit the README to provide instructions for how to reproduce your results <#b-edit-the-readme-to-provide-instructions-for-how-to-reproduce-your-results>`_

C. `Upload all materials necessary to reproduce your results <#c-upload-all-materials-necessary-to-reproduce-your-results>`_

D. `Add a DOI to your metarepo <#d-add-a-doi-to-your-metarepo>`_

E. `Add your metarepo citation to your paper <#e-add-your-metarepo-citation-to-your-paper>`_


A. Use the template to initialize your own metarepo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use the template, either click
`here <https://github.com/new?template_name=metarepo&template_owner=IMMM-SFA>`_,
click on the ``Use the metarepo template`` link at the top of this page,
or click ``Use this template`` on the `main repository
page <https://github.com/IMMM-SFA/metarepo/>`_ (shows up above
``Clone or download`` when you're logged in) and click ``Create a new repository``.

If you are a part of IM3, change the ``Owner`` to ``IMMM-SFA``, otherwise, leave it as is. Fill in
your ``Repository name`` (naming conventions below), the
``Description``, select whether you want the repository to be ``Public``
or ``Private``, and leave ``Include all branches`` unchecked. Click
``Create repository``. You'll be taken to the new repository you
created.

Note: The following naming conventions should be used when naming your
repository:

-  Single author: ``lastname_year_journal``
-  Multi author: ``lastname-etal_year_journal``
-  Multiple publications in the same journal:
   ``lastname-etal_year-letter_journal`` (e.g.,
   ``human-etal_2020-a_nature``, ``human-etal_2020-b_nature``)

B. Edit the README to provide instructions for how to reproduce your results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fill out all the applicable sections on your README. This can be done
either in browser on the GitHub website or locally (by cloning the GitHub repo onto your computer using the
``add``, ``commit``, and ``push`` workflow).

C. Upload all materials necessary to reproduce your results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your experiment includes scripts, upload those to the ``scripts`` directory. Include instructions to recreate your environment, for Python 
this would be the Python version and a `requirements.txt <https://pip.pypa.io/en/stable/reference/requirements-file-format/>`_ file. For R, 
include the R version and consider creating a `function that installs the required packages 
<https://stackoverflow.com/questions/38928326/is-there-something-like-requirements-txt-for-r>`_. 
If your paper contains figures, upload both the figure and the code to generate that figure to the ``figures`` 
directory. No data should be stored in your metarepo, data should be
uploaded to a data storage service. IM3 folks should use
`MSD-LIVE <https://msdlive.org/>`_.
   

D. Add a DOI to your metarepo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`This
tutorial <https://coderefinery.github.io/github-without-command-line/doi/>`_
walks through three main steps for adding a DOI to your metarepo, the
three steps are summarized below. Note that this should be done after
your metarepo is public and up to date with your current results. If
your experiment or results change at any time, update your metarepo and
create a new release. It is important to version and release your
metarepo due to changes that may occur during the publication
review process. If you do not know how to conduct a release on GitHub
when linked with Zenodo, please contact `Chris Vernon <mailto:chris.vernon@pnnl.gov>`_ to get set
up.

1. Activate the repository on Zenodo. If your metarepo is a part of the
   `IMMM-SFA <https://github.com/IMMM-SFA>`_ GitHub organization, you
   may need a member of the DSC team to help you with this.
2. Create a “release” for your metarepo in GitHub. Generally you can
   start with ``v1.0.0``.
3. Get a DOI from Zenodo and add the DOI badge to your repository at the top of the ``README.md``.

E. Add your metarepo citation to your paper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lastly, and very importantly, you need to add your metarepo citation to
your paper so that people can find the reproducible
instructions you've created.

1. Edit the ``CITATION.cff`` file to contain the correct author(s)
   (name, ORCID ID), version, DOI, and URL.
2. Click on the ``Cite this repository`` button on the right side of the
   main page of your metarepo. Copy whichever format you prefer.
3. Add the citation to the data availability section of your paper. For example, “All code and data to reproduce the results and figures can be found <citation>.”

Additional (not required) steps
-------------------------------

Customize your ``.gitignore`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A general ``.gitignore`` for use with Python or R development is
included. However, you may wish to customize this to the needs of your
project. The ``.gitignore`` file lets Git know what to push to the
remote repository and what needs to be ignored and stay local.

Best Practices
--------------

-  Don't bog down your repository with a bunch of raw data. Instead
   archive and mint a DOI for your data and provide the reference in
   this repository with instructions for downloading and using. If you
   are a part of IM3, use `MSD-LIVE <https://msdlive.org/>`_ to store
   data.
-  Test that the instructions in your metarepo are enough to completely
   recreate your experiment.
-  Clean up by removing all the ``how to create a metarepo`` text once you're
   done.
-  This workflow is significantly easier when started early in your
   project! Keep your metarepo up to date as you work on your
   experiment.

Stellar Examples
----------------

-  `burleyson-etal_2024_applied_energy <https://github.com/IMMM-SFA/burleyson-etal_2024_applied_energy>`_
-  `ssembatya-etal_2024_earths_future <https://github.com/IMMM-SFA/ssembatya-etal_2024_earths_future>`_
-  `zhao-etal_2023_gmd <https://github.com/JGCRI/zhao-etal_2023_gmd>`_

News and Awards
---------------

The article `Journal of Water Resources Planning and Management's Reproducibility Review Program: Accomplishments, Lessons, and Next Steps <https://ascelibrary.org/doi/10.1061/JWRMD5.WRENG-6559>`_ is a 3-year (2020-2023) summary perspective from ASCE JWRPM making a major effort to evaluate and reward reproducibility. Antonia Hadjimichael's IM3 paper is one of only 13 out of 557 papers that were found to be reproducible and given the highest award. The ASCE/EWRI has put $60K towards the open access awards.

 -  Hadjimichael's paper: `Exploring the Consistency of Water Scarcity Inferences between Large-Scale Hydrologic and Node-Based Water System Model Representations of the Upper Colorado River Basin <https://ascelibrary.org/doi/full/10.1061/JWRMD5.WRENG-5522>`_. 
 -  `metarepo <https://github.com/antonia-had/Hadjimichael-etal_2021_JWRPM>`_. 

Have more questions?
--------------------

Ask a question in the `Discussion
Section <https://github.com/IMMM-SFA/metarepo/discussions>`_!

If you're a part of IM3, reach out to the DSC team (email `Chris
Vernon <mailto:chris.vernon@pnnl.gov>`_)
