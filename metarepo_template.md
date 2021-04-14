<!--your zenodo badge here-->

# lastname-etal_year_journal

**A long-term global energy-economic model of carbon dioxide release from fossil fuel use**

Jae Edmonds<sup>1\*</sup> and John Reilly<sup>1</sup>

<sup>1 </sup> Institute for Energy Analysis, Oak Ridge Associated Universities, 1346 Connecticut Avenue, NW, Washington, DC 20036, USA
\* corresponding author:  email@pnl.gov

## Abstract
In this paper the authors develop a long-term global energy-economic model which is capable of assessing alternative energy evolutions over periods of up to 100 years. The authors have sought to construct the model so that it can perform its assigned task with as simple a modelling system as possible. The model structure is fully documented and a brief summary of results is given.

## Journal reference
Edmonds, J., & Reilly, J. (1983). A long-term global energy-economic model of carbon dioxide release from fossil fuel use. Energy Economics, 5(2), 74-88. DOI: https://doi.org/10.1016/0140-9883(83)90014-2

## Code reference
References for each minted software release for all code involved.  If you have modified a codebase that is outside of a formal release, and the modifications are not planned on being merged back into a version, fork the parent repository and add a `.<shortname>` to the version number of the parent and conduct your own name.  For example, `v1.2.5.hydro`.

## Data reference

### Input data
Reference for each minted data source for your input data.  For example:

Human, I.M. (2020). My input dataset name [Data set]. DataHub. https://doi.org/some-doi-number

### Output data
Reference for each minted data source for your output data.  For example:

Human, I.M. (2020). My output dataset name [Data set]. DataHub. https://doi.org/some-doi-number

## Contributing modeling software
| Model | Version | Repository Link | DOI |
|-------|---------|-----------------|-----|
| model 1 | version | link to code repository | link to DOI dataset |
| model 2 | version | link to code repository | link to DOI dataset |
| component 1 | version | link to code repository | link to DOI dataset |

## Reproduce my experiement
Fill in detailed info here or link to other documentation that is a thorough walkthrough of how to use what is in this repository to reproduce your experiment.


1. Install the software components required to conduct the experiement from [Contributing modeling software](#Contributing modeling software)
2. Download and install the supporting input data required to conduct the experiement from [Input data](#Input data)
3. Run the following scripts in the `workflow` directory to re-create this experiment:
| Script Name | Description | How to Run |
| --- | --- | --- |
| `step_one.py` | Script to run the first part of my experiment | `python3 step_one.py -f /path/to/inputdata/file_one.csv`
| `step_two.py` | Script to run the last part of my experiment | `python3 step_two.py -o /path/to/my/outputdir`
4. Download and unzip the output data from my experiment [Output data](#Output data)
5. Run the following scripts in the `workflow` directory to compare my outputs to those from the publication
| Script Name | Description | How to Run |
| --- | --- | --- |
| `compare.py` | Script to compare my outputs to the original | `python3 compare.py --orig /path/to/original/data.csv --new /path/to/new/data.csv`
