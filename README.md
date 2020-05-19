<!--your zenodo badge here-->

># meta-repository
>Template repository for a single point of access meta-repository to reproduce an experiment
>
>## Instructions for use
>NOTE:  Delete this instructional section after creating your template!
>
>### Purpose
>A meta-repository allows us to create a single point of access for someone to find all of the components that were used to create a published work for the purpose of reproducibility.  This repository should contain references to all minted data and software as well as house any ancillary code used to transform the source data, create figures for your publication, conduct the experiment, and / or execute the contributing software.
>
>### Using the Template
>Simply click `Use this template` on the main repository page (shows up to the left of `Clone or download`) and fill in your `Repository name`, the `Description`, select whether you want the repository to be `Public` or `Private`, and leave `Include all branches` unchecked.
>
>### Naming your meta-repository
>The following naming conventions should be used when naming your repository:  
>- Single author:  `lastname_year_journal`
>- Multi author:  `lastname-etal_year_journal`
>- Multiple publications in the same journal:  `lastname-etal_year-letter_journal` (e.g., `human-etal_2020-b_nature`)
>
>### Cutomize your `.gitignore` file
>A general `.gitignore` for use with Python development is included.  However, you may wish to customize this to the needs of your project.
>
>### Suggestions
>- Don't bog down your repository with a bunch of raw data.  Instead archive and mint a DOI for your data and provide the reference in this repository with instructions for use. 
>- Create complete and tested documentation for how to use what is in this repository to reproduce your experiment.
>
>### Creating a minted release for your meta-repository
>It is important to version and release your meta-repository as well due to changes that may occur during the publication review process.  If you do not know how to conduct a release on GitHub when linked with Zenodo, please contact chris.vernon@pnnl.gov to get set up.  The first line of this file is a space holder for your Zenodo DOI badge.
>
>
>### The following is the template for you to fill in with your own information


# lastname-etal_year_journal
One sentence describing your research

## Abstract
Your abstract here.

## Code reference
References for each minted software release for all code involved.  If you have modified a codebase that is outside of a formal release, and the modifications are not planned on being merged back into a version, fork the parent repository and add a `.<shortname>` to the version number of the parent and conduct your own name.  For example, `v1.2.5.hydro`.

#### Example:

Human, I.M. (2020, January 1). human/myrepo: v1.2.5.hydro (Version v1.2.5.hydro). Zenodo. https://doi.org/some-doi-number

## Journal reference
Update your journal reference here after acceptance.

## Data reference

### Input data
Reference for each minted data source for your input data.  

#### Example:

Human, I.M. (2020). My dataset name [Data set]. DataHub. https://doi.org/some-doi-number

### Output data
Reference for each minted data source for your output data.  

## Contributing models
| Model | Version | Repository Link | DOI |
|-------|---------|-----------------|-----|
| <model 1> | <version> | <link to code repository> | <link to DOI dataset> |
| <model 2> | <version> | <link to code repository> | <link to DOI dataset> |

## Reproduce my experiement
Fill in detailed info here or link to other documentation that is a thorough walkthrough of how to use what is in this repository to reproduce your experiment.

