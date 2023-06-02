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


def reproject_in_place(in_shapefile, desired_spatial_ref):
    try:
        am.Project(in_shapefile,
                   os.path.join(in_shapefile, "_projected"),
                   ap.SpatialReference(template_shapefile),
                   None,
                   ap.SpatialReference(in_shapefile)
                   )
    except:
        pass


def main(folder, shapefile):
    template_reference = ap.SpatialReference(template_shapefile)
    for file in os.listdir(folder):
        reproject_in_place(file, template_reference)


if __name__ == '__main__':
    main(target_folder, template_shapefile)
