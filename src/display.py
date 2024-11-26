from matplotlib import colors
import matplotlib.pyplot as plt

def display_enhanced(qr_code: list):
    """Displays the given QR-Code as an actual QR-Code using matplotlib."""
    clrs = ["red","white","black"]
    bounds = [-1,-.5,.5,1]
    cmap = colors.ListedColormap(clrs)
    norm = colors.BoundaryNorm(bounds,cmap.N)
    plt.figure(frameon=False)
    plt.tick_params(bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False)
    plt.imshow(qr_code,cmap=cmap, norm=norm)
    plt.show()
