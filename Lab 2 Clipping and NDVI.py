import numpy as np
import rasterio
import matplotlib.pyplot as plt
raster_image=rasterio.open('composite.tif')
raster_array=raster_image.read()
clipped_image=raster_array[2,300:900,300:900]
plt.imshow(clipped_image)
plt.show()

#Calculating NDVI Or Desired Parameters
import numpy as np

clipped_img = raster_array[:, 300:900, 300:900]

red_clipped = clipped_img[0].astype('f4')
nir_clipped = clipped_img[1].astype('f4')

ndvi_clipped = (nir_clipped - red_clipped) / (nir_clipped + red_clipped)

ndvi_clipped = np.nan_to_num(ndvi_clipped, nan=-1)

plt.imshow(ndvi_clipped, cmap='viridis')
plt.colorbar()
plt.show()



