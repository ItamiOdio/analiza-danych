import numpy as np
import pandas as pd
from plotnine import *

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

n = 100
centra = [(-6,-6), (0,0), (6,6), (9,9)]
X, y = make_blobs(n_samples=n, n_features=2, centers=centra, cluster_std=1, random_state=0)

df = pd.DataFrame(X, columns = ['x1', 'x2'])

df['Grupy']= y

print(df)

plot1 = (ggplot(df, aes(x='x1', y ='x2', color='factor(Grupy)')) +
 geom_point() +
 theme_minimal() +
 labs(color = 'grupy'))