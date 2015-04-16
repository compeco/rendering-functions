from nose.tools import ok_ as ok
from nose.tools import eq_ as eq
from matplotlib.testing.decorators import image_comparison
import numpy as  np
import fem_plt

def getTestMeshData():
    vertices = np.array([[0.0,0.0],[0.0,1.0],[1.0,0.0],[1.0,-0.5]],'d')
    elements = np.array([[0,1,2],[0,2,3]],'i')
    u = vertices[:,0]**2
    return vertices, elements, u

#@image_comparison(baseline_images=['contourf_c0p1'])
def test_contourf_c0p1():
    from matplotlib import pyplot  as plt
    vertices, elements, u = getTestMeshData()
    fig,ax = plt.subplots()
    fem_plt.contourf_c0p1(ax,vertices,elements,u)
