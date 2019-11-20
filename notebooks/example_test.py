

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
import xskillscore as xs
import xesmf as xe
from tqdm.autonotebook import tqdm  # Fancy progress bars for our loops!
import intake
# util.py is in the local directory
# it contains code that is common across project notebooks
# or routines that are too extensive and might otherwise clutter
# the notebook design
import util 

import Ngl,Nio
#%matplotlib inline
#plt.rcParams['figure.figsize'] = 12, 6
#%config InlineBackend.figure_format = 'retina' 

#---- 