# Project Title

Notebooks from the teaching sessions and the workshops of the
[2022 Summer School for Astrostatistics in Crete](
https://astro.physics.uoc.gr/Conferences/Astrostatistics_School_Crete_2022)

## Getting Started

The repository is organized in one folder per subject.
You will have to download the notebooks as well as the data
(which are on an other server).
See "Installing" below.

### Prerequisites 

```
Python v3.9
Jupyter notebook
```
Instructions on retrieveing Jupyter notebook are here: https://jupyter.org

### Installing

First download or clone this repository on your machine:

```
git clone https://github.com/astrostatistics-in-crete/2022_summer_school.git
```

Then download the data. 
To do this, from within the repository folder, run:

```
python get_data.py
```
This will automatically create the "data" subfolders within each 
subject folder, and download the data.

If you are running the notebooks from the school, run:

```
./new_day.sh
```

This will download the data, set up the conda environment and
start the jupyter notebook. 

## Running the notebooks

```
jupyter-notebook <notebook_name>.ipynb &
```
## Authors

* **Andrew, Jeff** - Northwestern University

* **Bonfini, Paolo** - Ballista Technologies

* **Kovlakas, Kostantinos** - University of Geneva

* **Maravelias, Grigoris** - National Observatory of Athens & FORTH

## References

All the material provided here (notebooks and scripts) is licenced
under the [Creative Commons BY-SA](https://creativecommons.org/licenses/by-sa/3.0/)
licence.

The notebooks have adopted publicly available material from
several sources, most notably [AstroML](http://www.astroml.org).
All the references to published papers, data, and software tools are
properly addressed within each notebook.


## Acknowledgments

If the material you learned through this summer school directly
and significantly contributed to your work, we invite you to
include the following acknowledgement in your manuscript:

```
We wish to thank the "2022 Summer School for Astrostatistics in Crete" for providing training on the statistical methods adopted in this work.
```
