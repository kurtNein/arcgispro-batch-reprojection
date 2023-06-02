"""
This was created for Penn State University GEOG485 Lesson 2 by Kurt Neinstedt.
This script takes a folder directory and a shapefile path as inputs, and reprojects data in the folder directory
to the projection of the shapefile.
"""
import arcpy as ap
import arcpy.management as am
import os

target_folder = r'C:\GEOG485\Lesson2\Lesson2Data'
template_shapefile = ap.GetParameterAsText()


def reproject_in_place(in_shapefile, out_shapefile, desired_spatial_ref):
    am.Project(in_shapefile,
               out_shapefile + "projected",
               ap.SpatialReference(template_shapefile),
               None,
               ap.SpatialReference(in_shapefile)
               )


def main(folder, shapefile):
    pass


if __name__ == '__main__':
    main(target_folder, template_shapefile)
