"""
This was created for Penn State University GEOG485 Lesson 2 by Kurt Neinstedt.
This script takes a folder directory and a shapefile path as inputs, and reprojects data in the folder directory
to the projection of the shapefile.
"""
import arcpy as ap
import arcpy.management as am
import os

target_folder = r'C:\GEOG485\Lesson2\Lesson2Data\CountyLines.shp'
template_shapefile = r'C:\GEOG485\Lesson2\Lesson2Data\CityBoundaries.shp'  # ap.GetParameterAsText(1)


def reproject_in_place(in_shapefile, template_shapefile):
    try:
        am.Project(in_shapefile,
                   os.path.join(in_shapefile, "_projected"),
                   ap.SpatialReference(template_shapefile),
                   None,
                   ap.SpatialReference(in_shapefile)
                   )
    except TypeError:
        print("TypeError: Check arguments.")


def main(file, shapefile):
    print(ap.SpatialReference(shapefile))
    template_reference = ap.SpatialReference(shapefile)
    reproject_in_place(file, template_reference)


if __name__ == '__main__':
    #main(target_folder, template_shapefile)
    am.Project(target_folder,
               os.path.join(r'C:\GEOG485\Lesson2\Lesson2Data\CountyLines_projected.shp'),
               ap.Describe(template_shapefile).spatialReference,
               None)
