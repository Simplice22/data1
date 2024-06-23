import pandas as pd
import numpy as np 

import seaborn as sns
import matplotlib.pyplot as plt


from ipywidgets import interact
from bokeh.plotting import figure,show
from bokeh.io import  push_notebook,output_notebook
output_notebook()
push_notebook()
from bokeh.models.widgets import Panel, Tabs
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import StandardScaler
from bokeh.transform import factor_cmap