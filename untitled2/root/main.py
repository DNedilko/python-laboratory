import numpy as np
from skimage import measure
​
import plotly.offline
​
# Set up mesh
n = 250
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
z = np.linspace(-3,3,n)
X, Y, Z =  np.meshgrid(x, y, z)
​
# Create mesh function
def f_heart(x,y,z):
    F = 320 * ((-x**2 * z**3 -9*y**2 * z**3/80) +
               (x**2 + 9*y**2/4 + z**2-1)**3)
    return F
​
​
def plotly_triangular_mesh(vertices, faces, intensities=f_heart, colorscale="Viridis",
                           showscale=False, reversescale=False, plot_edges=False):
    # vertices = a numpy array of shape (n_vertices, 3)
    # faces = a numpy array of shape (n_faces, 3)
    # intensities can be either a function of (x,y,z) or a list of values
​
    x, y, z = vertices.T
    I, J, K = faces.T
    if hasattr(intensities, '__call__'):
        intensity = intensities(x, y, z)  # the intensities are computed here via the passed function,
        # that returns a list of vertices intensities
​
    elif isinstance(intensities, (list, np.ndarray)):
        intensity = intensities  # intensities are given in a list
    else:
        raise ValueError("intensities can be either a function or a list, np.array")
​
    mesh = dict(type='mesh3d',
                x=x,
                y=y,
                z=z,
                colorscale=colorscale,
                reversescale=reversescale,
                intensity=intensity,
                i=I,
                j=J,
                k=K,
                name='',
                showscale=showscale
                )
​
    if showscale is True:
        mesh.update(colorbar=dict(thickness=20, ticklen=4, len=0.75))
​
    if plot_edges is False:  # the triangle sides are not plotted
        return [mesh]
    else:  # plot edges
        # define the lists Xe, Ye, Ze, of x, y, resp z coordinates of edge end points for each triangle
        # None separates data corresponding to two consecutive triangles
        tri_vertices = vertices[faces]
        Xe = []
        Ye = []
        Ze = []
        for T in tri_vertices:
            Xe += [T[k % 3][0] for k in range(4)] + [None]
            Ye += [T[k % 3][1] for k in range(4)] + [None]
            Ze += [T[k % 3][2] for k in range(4)] + [None]
​
        # define the lines to be plotted
        lines = dict(type='scatter3d',
                     x=Xe,
                     y=Ye,
                     z=Ze,
                     mode='lines',
                     name='',
                     line=dict(color='rgb(70,70,70)', width=1)
​
                     )
​
        return [mesh, lines]
# Obtain value to at every point in mesh
vol = f_heart(X,Y,Z)
​
# Extract a 2D surface mesh from a 3D volume (F=0)
verts, faces = measure.marching_cubes_classic(vol, 0, spacing=(0.1, 0.1, 0.1))
​
pl_BrBG=[[0.0, 'rgb(252, 0, 13)'],
         [0.1, 'rgb(252, 0, 23)'],
         [0.2, 'rgb(252, 0, 23)'],
         [0.3, 'rgb(222, 0, 23)'],
         [0.4, 'rgb(222, 0, 23)'],
         [0.5, 'rgb(222, 0, 23)'],
         [0.6, 'rgb(222, 0, 23)'],
         [0.7, 'rgb(222, 0, 23)'],
         [0.8, 'rgb(252, 0, 23)'],
         [0.9, 'rgb(252, 0, 23)'],
         [1.0, 'rgb(252, 0, 23)']]
data = plotly_triangular_mesh(verts, faces, colorscale=pl_BrBG, showscale=False)
​
​
​
​
​
axis = dict(showbackground=True,
            backgroundcolor="rgb(230, 230,230)",
            gridcolor="rgb(255, 255, 255)",
            zerolinecolor="rgb(255, 255, 255)")
​
noaxis = dict(visible=False)
​
layout = dict(
         title='Made with <3 and Python',
         font=dict(family='Balto'),
         showlegend=False,
         width=800,
         height=800,
         scene=dict(xaxis=axis,
                    yaxis=axis,
                    zaxis=axis,
                    aspectratio=dict(x=1,
                                     y=1,
                                     z=1)
                    )
        )
​
fig = dict(data=data, layout=layout)
​
​
​
plotly.offline.plot(fig)
