# Script for copying the matplotlib styles to all conda environments

## Usage
1. create a style you desire in the `styles` folder. Check the [matplotlib page](https://matplotlib.org/stable/tutorials/introductory/customizing.html#the-default-matplotlibrc-file) for attributes you can change.
2. check the style with [plots_demo.ipynb](plots_demo.ipynb)
3. run [copy_styles.py](copy_styles.py) to copy all the styles to all conda environments

**Note:** the script will overwrite the styles in the conda environments

So far tested on Mac, however should work on Linux and Windows as well.

## Further improvements
- include [temp styling](https://matplotlib.org/stable/tutorials/introductory/customizing.html#temporary-styling) for example for phase plots
- make use od [composing styles](https://matplotlib.org/stable/users/explain/customizing.html#customizing-with-style-sheets)

> ### Composing styles
>
> Style sheets are designed to be composed together. So you can have a style sheet that customizes colors and a separate style sheet that alters element sizes for presentations. These styles can easily be combined by passing a list of styles:
>
> ```
> import matplotlib.pyplot as plt
> plt.style.use(['dark_background', 'presentation'])
> ```
> Note that styles further to the right will overwrite values that are already defined by styles on the left.

