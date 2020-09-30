# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:40:22 2020

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.transpose([[1, 0, 0],[np.sqrt(3)/3, 2/3*np.sqrt(3), 0]])
Xt = ([[1, 0, 0],[np.sqrt(3)/3, 2/3*np.sqrt(3), 0]])
y = np.transpose([[1.5, 0.5, 1]])
a = np.dot(np.linalg.inv(np.dot(Xt,X)),np.dot(Xt,y))

lm = LinearRegression(fit_intercept=False)
lm.fit(X,y)
y_pred = lm.predict(X)