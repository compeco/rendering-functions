"""
A module for plotting general finite element approximations
"""

def contourf_c0p1(ax,vertices, elements, u):
    """
    Filled contour plot  of scalar on 2D unstructured  mesh
    """
    ax.tricontourf(vertices[:,0],vertices[:,1],elements,u)
    
