# 2022 Summer School for Astrostatistics in Crete

Notebooks from the teaching sessions and the workshops of the
[2022 Summer School for Astrostatistics in Crete](
https://astro.physics.uoc.gr/Conferences/Astrostatistics_School_Crete_2022)

Our Slack Workspace:
[2022 Summer School Slack Workspace](https://astrostatisti-g9x1513.slack.com)

## Getting Started

The repository is organized in one folder per subject.
You will have to download the notebooks and create a `conda` environment.
See "Installing" below.

### Prerequisites

```
Python v3.9
Jupyter notebook
conda
```
Instructions on retrieving `Jupyter notebook` are here: https://jupyter.org.

See https://docs.conda.io/en/latest/ for instructions on installing `conda`.

### Installing

First download or clone this repository on your machine:

```
git clone https://github.com/astrostatistics-in-crete/2022_summer_school.git
```

Then create a new conda environment and install the necessary python packages:

```
conda create --channel conda-forge --name astrostat22 python=3.9
conda activate astrostat22
conda install auto-sklearn=0.14.6
conda install nb_conda=2.2.1 astropy=5.2.1 pandas=1.5.3 emcee=3.1.4 corner=2.2.1 seaborn=0.12.2
conda install ipynbname=2021.3.2 prettytable=3.6.0 mlxtend=0.21.0
pip install tensorflow==2.11.0 pipelinehelper==0.7.8 cutecharts==1.2.0
conda install keras=2.11.0
conda install wand=0.6.10
```

You are now ready to run the notebooks! Remember that in order to use the
notebooks in a different terminal or after restarting the machine, you just need
to activate the environment:

```
conda activate astrostat22
```

## Running the notebooks

Run the following command at the parent folder to access all notebooks of the
school.

```
jupyter notebook
```
## Authors

* **Andrews, Jeff** - Northwestern University

* **Bonfini, Paolo** - Ballista Technologies

* **Kovlakas, Kostantinos** - University of Geneva

* **Maravelias, Grigoris** - National Observatory of Athens & FORTH

## References

All the material provided here (notebooks and scripts) is licenced
under the [Creative Commons BY-SA](https://creativecommons.org/licenses/by-sa/3.0/)
licence.

The notebooks have adopted publicly available material from
several sources that are properly credited.
All the references to published papers, data, and software tools are
properly addressed within each notebook.


## Acknowledgments

If the material you learned through this summer school directly
and significantly contributed to your work, we invite you to
include the following acknowledgement in your manuscript:


> *We wish to thank the "2022 Summer School for Astrostatistics in Crete" for providing training on the statistical methods adopted in this work.*
