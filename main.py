"""
This was created for Penn State University GEOG485 Lesson 2 by Kurt Neinstedt.
This script takes a folder directory and a shapefile path as inputs, and reprojects data in the folder directory
to the projection of the shapefile.
"""

import arcpy
import os

folder = r'C:\GEOG485\Lesson2\Lesson2Data'
shapefile = arcpy.GetParameterAsText()


def main(in_folder, example_shapefile):
    pass


if __name__ == '__main__':
    main(folder, shapefile)
