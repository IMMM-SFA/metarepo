[![DOI](https://zenodo.org/badge/265119113.svg)](https://zenodo.org/badge/latestdoi/265119113)

# metarepo
Template repository for a single point of access meta-repository to reproduce an experiment

## Purpose
A meta-repository creates a single point of access for someone to find all of the components that were used to create a published work for the purpose of reproducibility.  This repository should contain references to all minted data and software as well as house any ancillary code used to transform the source data, create figures for your publication, conduct the experiment, and / or execute the contributing software.

## Using the template
Simply click `Use this template` on the main repository page (shows up to the left of `Clone or download`) and fill in your `Repository name`, the `Description`, select whether you want the repository to be `Public` or `Private`, and leave `Include all branches` unchecked.

## Naming your meta-repository
The following naming conventions should be used when naming your repository:  
- Single author:  `lastname_year_journal`
- Multi author:  `lastname-etal_year_journal`
- Multiple publications in the same journal:  `lastname-etal_year-letter_journal` (e.g., `human-etal_2020-b_nature`)

## Customize your `.gitignore` file
A general `.gitignore` for use with Python or R development is included.  However, you may wish to customize this to the needs of your project.  The `.gitignore` file lets Git know what to push to the remote repository and what needs to be ignored and stay local.

## Suggestions
- Don't bog down your repository with a bunch of raw data.  Instead archive and mint a DOI for your data and provide the reference in this repository with instructions for use.
- Create complete and tested documentation for how to use what is in this repository to reproduce your experiment.

## Creating a minted release for your meta-repository
It is important to version and release your meta-repository as well due to changes that may occur during the publication review process.  If you do not know how to conduct a release on GitHub when linked with Zenodo, please contact chris.vernon@pnnl.gov to get set up.  

## The meta-repository markdown template
A sample meta-repository template is provided in this repository in the file `metarepo_template.md`.  

To use it, do the following:
1. Create the template repository as mentioned above in [Using the template](#using-the-template)
2. Clone your new repository to you local machine
3. Change directories into your new meta-repository directory you just cloned
4. Run `git rm README.md` to delete this file (`README.md`) and commit it using `git commit -m 'remove instructions'`
5. Rename `metarepo_template.md` as `README.md`
6. Run `git add README.md` to stage the new file that will show up on load in your remote GitHub repository
7. Run `git rm metarepo_template.md` to remove the original template
8. Run `git commit -m 'set up new template as readme'` to set the changes
9. Run `git push` to send the changes to your remote GitHub repository
10. Modify the `README.md` file to represent your experiement and use the `add`, `commit`, `push` workflow to update your remote repository
