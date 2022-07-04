# plot_PC_3D(X_n, pca, color='red', label='data', offset=False)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import numpy as np
from matplotlib.ticker import FormatStrFormatter

#------------------------------------------------------------------------------    
class Arrow3D(FancyArrowPatch):

    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
#------------------------------------------------------------------------------    
 
#------------------------------------------------------------------------------    
def plot_PC_3D(X, pca, color='grey', label='data', offset=False):

    fig = plt.figure(figsize=(7,7))

    ax = fig.add_subplot(1,1,1, projection='3d')    

    ax.scatter(X[:,0], X[:,1], X[:,2], alpha=0.5)

    # Extracting the first 3 dimensions of the first 3 PCs:
    PCs         = pca.components_[:3,:3]
    eigenvalues = pca.explained_variance_[:3]
        
    # Normalizing eigenvectors by their respective variance
    PCs = 2*np.multiply(PCs, eigenvalues[:, np.newaxis])

    x_MAX = np.max(np.abs(PCs[:3,0]))
    y_MAX = np.max(np.abs(PCs[:3,1]))
    z_MAX = np.max(np.abs(PCs[:3,2]))
    
    if(offset):
    # small offset for visualization purposes
        dPC = [0.0, 0.0, 0.3*np.mean(np.abs(PCs[:,2]))]
        # NOTE: Adding an offset equal to 30% of the mean of the PCs in the 3d
        #       dimension (in absolute value).
    else:
        dPC = [0., 0., 0.]

        
    for p, PC in enumerate(PCs):        
        
        centers = np.array([0,0,0])
        
        PC     = PC       + dPC
        centers = centers + dPC

        a = Arrow3D([centers[0], PC[0]],
                    [centers[1], PC[1]],
                    [centers[2], PC[2]],
                    mutation_scale=20, lw=3, arrowstyle="-|>", color=color,
                    label=label)
        ax.add_artist(a)
        
        if(p==0):
            ax.scatter(centers[0],centers[1],centers[2],s=10,color=color,label=label)
            # dummy point to add label
   
    #ax.set_xlim( -np.abs(x_MAX) , np.abs(x_MAX) )
    #ax.set_ylim( -np.abs(y_MAX) , np.abs(y_MAX) )
    #ax.set_zlim( -np.abs(z_MAX) , np.abs(z_MAX) )
 
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.0e'))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.0e'))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.0e'))
   
    ax.set_xlabel('$X_0$', labelpad=10, fontsize=14)
    ax.set_ylabel('$X_1$', labelpad=10, fontsize=14)
    ax.set_zlabel('$X_2$', labelpad=10, fontsize=14)

    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.tick_params(axis='z', labelsize=10)
    
    # Changing viewing angle:
    ax.view_init(elev=20, azim=35)
                
    plt.legend(bbox_to_anchor=(1.1, 0.5), loc='lower right', ncol=1)
    plt.show()
#------------------------------------------------------------------------------ 
