[![DOI](https://zenodo.org/badge/265254045.svg)](https://zenodo.org/doi/10.5281/zenodo.10442485)

# metarepo
`metarepo` is short for meta-repository, a GitHub repository that contains instructions to reproduce results in a published work. This repo is a template for creating your own metarepo.

[![Use the `metarepo` template|32x32](https://github.com/new?template_name=metarepo&template_owner=IMMM-SFA)]

## Purpose
A meta-repository creates a single point of access for someone to find all of the components that were used to create a published work for the purpose of reproducibility. This repository should contain references to all minted data and software as well as any ancillary code used to transform the source data, create figures for your publication, conduct the experiment, and / or execute the contributing software.

## Lost? Start here
- Don't know how to use GitHub? Check out their [tutorial](https://docs.github.com/en/get-started/start-your-journey/hello-world).
- Want a video walk-through of what a metarepo is, why they're important, and how to create one? [Here ya go](https://youtu.be/1dJOXdm-Wvc?t=180). 


## Workflow
These are the big picture steps for how to start from scratch and end up with a complete metarepo. There are more in depth steps below.

A. [Use the template to initialize your own meta-repo](#a-use-the-template-to-initialize-your-own-meta-repo)

B. [Edit the README to provide instructions for how to reproduce your results](#b-edit-the-readme-to-provide-instructions-for-how-to-reproduce-your-results)

C. [Upload all materials necessary to reproduce your results](#c-upload-all-materials-necessary-to-reproduce-your-results)

D. [Add a DOI to your metarepo](#d-add-a-doi-to-your-metarepo)

E. [Add your metarepo citation to your paper](#e-add-your-metarepo-citation-to-your-paper)

### A. Use the template to initialize your own meta-repo
Click `Use this template` on the [main repository page](https://github.com/IMMM-SFA/metarepo/) (shows up above `Clone or download`) and click `Create a new repository`. Fill in your `Repository name` (naming conventions below), the `Description`, select whether you want the repository to be `Public` or `Private`, and leave `Include all branches` unchecked. Click `Create repository`. You'll be taken to the new repository you created.

Note: The following naming conventions should be used when naming your repository:  
- Single author:  `lastname_year_journal`
- Multi author:  `lastname-etal_year_journal`
- Multiple publications in the same journal:  `lastname-etal_year-letter_journal` (e.g., `human-etal_2020-b_nature`)

### B. Edit the README to provide instructions for how to reproduce your results

A sample metarepo template is provided in this repository named `metarepo_template.md`.  

You now want to replace the `README.md` file with the `metarepo_template.md`. To do this, do the following:
1. Clone your new repository to your local machine
2. Change directories into your new meta-repository directory you just cloned
3. Rename `metarepo_template.md` as `README.md` by running `mv metarepo_template.md README.md`
4. Run `git add README.md` to stage the new file that will show up on load in your remote GitHub repository
5. Run `git rm metarepo_template.md` to remove the not-renamed file from GitHub
6. Run `git commit -m "set README to the metarepo template"` to set the changes
7. Run `git push` to send the changes to your remote GitHub repository

Now you have the metarepo template as your README! The next step is to fill out all the applicable sections on your README. This can be done either locally (in the cloned GitHub repo on your computer using the `add`, `commit`, and `push` workflow), or in browser on the GitHub website. 

### C. Upload all materials necessary to reproduce your results

If your experiment includes scripts, upload those to the `scripts` directory. No data should be stored in your metarepo, data should be uploaded to a data storage service. For IM3 folks, use [MSD-LIVE](https://msdlive.org/).

### D. Add a DOI to your metarepo

[This tutorial](https://coderefinery.github.io/github-without-command-line/doi/) walks through three main steps for adding a DOI to your metarepo, the three steps are summarized below. Note that this should be done after your metarepo is public and up to date with your current results. If your experiment or results change at any time, update your metarepo and create a new release. It is important to version and release your meta-repository due to changes that may occur during the publication review process. If you do not know how to conduct a release on GitHub when linked with Zenodo, please contact [chris.vernon@pnnl.gov](mailto:chris.vernon@pnnl.gov) to get set up. 

1. Activate the repository on Zenodo. If your metarepo is a part of the [IMMM-SFA](https://github.com/IMMM-SFA) GitHub organization, you may need a member of the DSC team to help you with this.
2. Create a “release” for your metarepo in GitHub. Generally you can start with `v1.0.0`.
3. Get a DOI from Zenodo and dd the DOI badge to your repository. 

### E. Add your metarepo citation to your paper

Lastly, and very importantly, you need to add your metarepo citation to your paper so that people can find the beautiful reproducible instructions you've created. 

1. Edit the `CITATION.cff` file to contain the correct author(s) (name, ORCID ID), version, DOI, and URL. 
2. Click on the `Cite this repository` button on the right side of the main page of your metarepo. Copy either the APA or BibTex format. 
3. Add the citation to your paper. 

## Additional (not required) steps
### Customize your `.gitignore` file
A general `.gitignore` for use with Python or R development is included. However, you may wish to customize this to the needs of your project. The `.gitignore` file lets Git know what to push to the remote repository and what needs to be ignored and stay local.


## Best Practices
- Don't bog down your repository with a bunch of raw data.  Instead archive and mint a DOI for your data and provide the reference in this repository with instructions for downloading and using. If you are a part of IM3, use [MSD-LIVE](https://msdlive.org/) to store data. 
- Test that the instructions in your metarepo are enough to completely recreate your experiment. 
- Remove all the instructive text throughout your metarepo once you're done. 


## :star: Stellar Examples

- [burleyson-etal_2024_applied_energy](https://github.com/IMMM-SFA/burleyson-etal_2024_applied_energy)
- [ssembatya-etal_2024_earths_future](https://github.com/IMMM-SFA/ssembatya-etal_2024_earths_future)

## Have more questions? 

Ask a question in the [Discussion Section](https://github.com/IMMM-SFA/metarepo/discussions)!