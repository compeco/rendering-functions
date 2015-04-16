def contour_c0p1(vertices, element, C):
    fig, ax = plt.subplots()
    ax.tricontourf(vertices[:,0],vertices[:,1],elements,C)
