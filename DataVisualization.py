import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import nibabel as nib

class ArrayView(object):

    # xvalues: numpy 1D array of X values
    # functionToEvaluate should be in the form:
    # def gaussian(x, *args):
    #   m1, s1 = args
    #    ret = scipy.stats.norm.pdf(x, loc=m1, scale=s1) # x peut etre un array ici, pas forcement un scalaire
    #    return ret # renvoie un scalaire ou un array, suivant les cas
    # *functionArgs: function arguments
    # Example usage:
    # xvalues = np.linspace(-10.0, 10.0, 0.1)
    # yvalues = gaussian()
    # ArrayView.viewCurve(xvalues, yvalues)
    def viewCurve(xvalues, yvalues):
        plt.clf()
        plt.plot(xvalues, yvalues)

    def view2DArray(arr):
        plt.clf()
        plt.imshow(arr)
    
    # Ported from the Python2 code found in:
    # http://nbarbey.github.io/2011/07/08/matplotlib-slider.html
    # Changed:
    # xrange -> range
    # get rid of 'axisbg'
    # remove erroneous line breaks
    def view3DArray(cube, axis=2, **kwargs):
        # check dim
        if not cube.ndim == 4:
            raise ValueError("cube should be an ndarray with ndim == 4")

        if cube.shape[3] != 3:
            raise ValueError("cube's last dimension should be 3")
      
        minVal = np.min(cube)
        maxVal = np.max(cube)
    
        if minVal < 0.0 or maxVal > 1.0:
            raise ValueError("cube values cannot be outside the range [0,1]") 
        
        # generate figure
        fig = plt.figure()
        ax = plt.subplot(111)
        fig.subplots_adjust(left=0.25, bottom=0.25)
    
        # select first image
        s = [slice(0, 1) if i == axis else slice(None) for i in range(3)]
        im = cube[tuple(s)].squeeze()
    
        # display image
        l = ax.imshow(im, **kwargs)
    
        # define slider
        #axcolor = 'lightgoldenrodyellow'
        ax = fig.add_axes([0.25, 0.1, 0.65, 0.03]) # , axisbg=axcolor)
    
        slider = Slider(ax, 'Axis %i index' % axis, 0, cube.shape[axis] - 1, valinit=0, valfmt='%i')
    
        def update(val):
            ind = int(slider.val)
            s = [slice(ind, ind + 1) if i == axis else slice(None) for i in range(3)]
            im = cube[tuple(s)].squeeze()
            l.set_data(im, **kwargs)
            fig.canvas.draw()
    
        slider.on_changed(update)
    
        plt.show()




if __name__ == "__main__":

    data = nib.load("C:/Users/ioomar/eclipse-workspace/autoencoders/data/P10020F.nii.gz")
    data = data.get_fdata()
    data = data[250:330,300:380,0:80]
    #Normalization
    data = (data[:,:,:] - np.min(data))/(np.max(data) - np.min(data))

    #reshape
    data = data.reshape(data.shape[0], data.shape[1], data.shape[2], 1)

    data_cube = np.append( data , data , axis = 3)
    data_cube = np.append( data_cube,  data , axis = 3)
    print(data_cube.shape)

    #visualization 3D
    ArrayView.view3DArray(data_cube)
