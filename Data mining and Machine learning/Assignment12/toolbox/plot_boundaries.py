# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:05:21 2018

@author: Roel bouman, Lisa Tostrams (Modified by Martan van der Straaten)

Simple decision boundary plotter for scikit-learn Classifiers

from toolbox.plot_boundaries import plot_boundaries

clf = sklearn.___.(...)
clf.fit(X,y)

plot_boundaries((X,y,clf))

Extended with:
plot_boundaries_3d(X,y,clf, angle=None)

Here angle is ignored if it is not set, but if you define it you will look at the 3d plot from 
a... different angle.

It does so as follows, we define angle=(e,a) and set elev=e and azim=a

"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from mpl_toolkits.mplot3d import Axes3D
        
def plot_boundaries(X,y,model):
    y_hat = model.predict(X)
    x0 = np.arange(min(X[:,0])-0.5, max(X[:,0])+0.5, 0.01)
    x1 = np.arange(min(X[:,1])-0.5, max(X[:,1])+0.5, 0.01)
    xx, yy = np.meshgrid(x0, x1, sparse=False)
    space = np.asarray([xx.flatten(),yy.flatten()]).T
    z = model.predict(space)

    plt.scatter(X[(y_hat==1),0],X[(y_hat==1),1],label='Predicted 1', c="r", marker="o", s=50)
    plt.scatter(X[(y_hat==0),0],X[(y_hat==0),1],label='Predicted 0', c="b", marker="o", s=50)
    plt.scatter(X[(y==1),0],X[(y==1),1],label='True 1', c="r", marker=".", s=70, zorder=3)
    plt.scatter(X[(y==0),0],X[(y==0),1],label='True 0', c="b", marker=".", s=70, zorder=3)
    h = plt.contourf(x0,x1,np.reshape(z,[len(x1),len(x0)]), levels=[0,0.5,1],colors=('b','r'),alpha=0.1)
    plt.legend(numpoints=1, markerscale=.75, prop={'size': 12}, bbox_to_anchor=(1, 0.5))

def plot_boundaries_3d(X,y,model, angle=None):
    fig = plt.figure(figsize=(10, 8), constrained_layout=True)
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)

    ax.scatter(X[y==0,0], X[y==0,1], X[y==0,2], label="0")
    ax.scatter(X[y==1,0], X[y==1,1], X[y==1,2], label="1")
    ax.set_xlabel('$X_1$')
    ax.set_ylabel('$X_2$')
    ax.set_zlabel('$X_1*X_2$')

    # Extract SVM weights
    w = model.coef_[0]
    b = model.intercept_[0]

    # Create grid for x1 and x2
    x1_range = np.linspace(0, 1, 20)
    x2_range = np.linspace(0, 1, 20)
    X1, X2 = np.meshgrid(x1_range, x2_range)

    # Compute X3 from the plane equation:
    # w1*x1 + w2*x2 + w3*x1*x2 + b = 0
    # Solve for X3 = x1*x2
    X3 = -(w[0] * X1 + w[1] * X2 + b) / w[2]

    # Plot the decision boundary plane
    ax.plot_surface(X1, X2, X3, alpha=0.4, color='green')

    if angle:
        elev, azim = angle
        ax.view_init(elev=elev, azim=azim)

    ax.set_box_aspect(None, zoom=0.95)

    plt.legend()
    plt.show()