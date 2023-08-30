# Script for copying the matplotlib styles to all conda environments

## Usage
1. create a style you desire in the `styles` folder. Check the [matplotlib page](https://matplotlib.org/stable/tutorials/introductory/customizing.html#the-default-matplotlibrc-file) for attributes you can change.
2. check the style with [plots_demo.ipynb](plots_demo.ipynb)
3. run [copy_styles.py](copy_styles.py) to copy all the styles to all conda environments

**Note:** the script will overwrite the styles in the conda environments

So far tested on Mac, however should work on Linux and Windows as well.

## Further improvements
- include [temp styling](https://matplotlib.org/stable/tutorials/introductory/customizing.html#temporary-styling) for example for phase plots