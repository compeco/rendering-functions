"""
Testing module for fem_plt
"""
import os
from nose.tools import ok_ as ok
from nose.tools import eq_ as eq
import numpy as  np
import fem_plt

def getTestMeshData():
    """
    generate a simple mesh
    """
    vertices = np.array([[0.0,0.0],[0.0,1.0],[1.0,0.0],[1.0,-0.5]],'d')
    elements = np.array([[0,1,2],[0,2,3]],'i')
    u = vertices[:,0]**2
    return vertices, elements, u

def compare_images(expected,actual,tol):
    """
    Do a diff of the image files
    """
    from matplotlib.testing.compare import compare_images
    from matplotlib.testing.noseclasses import (KnownFailureTest,
                                                KnownFailureDidNotFailTest,
                                                ImageComparisonFailure)
    err = compare_images(expected, actual,tol, in_decorator=True)
    type(err)
    try:
        if not os.path.exists(expected):
            raise ImageComparisonFailure(
                'image does not exist: %s' % expected)
        if err:
            raise ImageComparisonFailure(
                """images not close: {actual}s vs. {expected}s
RMS = {rms}.3f)
See {diff}""".format(**err))
    except ImageComparisonFailure:
        raise

def test_contourf_c0p1():
    """
    Test the basic  contour plot
    """
    from matplotlib import pyplot  as plt
    vertices, elements, u = getTestMeshData()
    fig,ax = plt.subplots()
    fem_plt.contourf_c0p1(ax,vertices,elements,u)
    #uncomment this  to generate an image with only the diff "IMAGE ERROR"
    #ax.annotate('IMAGE ERROR', fontsize=22,xy=(0.5, 1.), xytext=(0.5,1.))
    actual = "contourf_c0p1.png"
    expected = os.path.join("test_images",actual)
    plt.savefig(actual)
    compare_images(expected,actual,tol=1.0e-3)

if __name__ == '__main__':
    import nose
    nose.main()
