import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt


#Reading tiff file:
raster_image=rasterio.open('composite.tif')

#creating Histogram:
rasterio.plot.show_hist(raster_image, bins=50, histtype='stepfilled', lw=1.0, stacked=False, alpha=0.5)

#reading multiple bands:
band1=raster_image.read(1)
band2=raster_image.read(2)
band3=raster_image.read(3)


#Creating a figure of 15 by 15 inches:
figure=plt.figure(figsize=(15,15))
fig1=figure.add_subplot(5,5,1)
fig2=figure.add_subplot(5,5,2)
fig3=figure.add_subplot(5,5,3)
Gray_scale=figure.add_subplot(5,5,4)


fig1.imshow(band1,cmap='Reds')
fig2.imshow(band2,cmap='Greens')
fig3.imshow(band3,cmap='Blues')
Gray_scale.imshow(band3,cmap='gray')



#checking number of bands and Dimensions:
width=raster_image.width
height=raster_image.height
bands=raster_image.count
print(f'height is {height}, width is {width}.\nNumber of bands are {bands}.')


#Checking "Coordinate Reference System (CRS)"(it will provide you with
#information about the coordinate reference system used by the image.)
print(raster_image.crs)
#output: EPSG:32642

#EPSG: This is the standard way of referencing coordinate systems and other
#geospatial parameters. It stands for "European Petroleum Survey Group," which
#was an organization that initially created this standard. The EPSG codes are
#widely used to uniquely identify various spatial reference systems.

#32642: This specific EPSG code (32642) corresponds to a particular coordinate
#reference system. In this case, EPSG:32642 refers to the WGS 84 / UTM zone
#42N projection.

#WGS 84: This is the World Geodetic System 1984, which is a global datum
#commonly used for representing the Earth's shape and orientation in GPS
#and geospatial applications.

#UTM zone 42N: UTM stands for Universal Transverse Mercator, which is a commonly
#used map projection system. "Zone 42N" indicates that the image is using the
#UTM projection in the Northern Hemisphere's zone 42.



#Checking MetaData:
MetaData=raster_image.meta
print(f"Meta Data of the Raster Image:\n{MetaData}")

#Displaying Images:
plt.show()



