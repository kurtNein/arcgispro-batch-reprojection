"""
This was created for Penn State University GEOG485 Lesson 2 by Kurt Neinstedt.
This script takes a folder directory and a shapefile path as inputs, and reprojects data in the folder directory
to the projection of the shapefile.
"""

import arcpy as ap
import arcpy.management as am
import os

target_folder = r'C:\GEOG485\Lesson2\Lesson2Data'
template_shapefile = r'C:\GEOG485\Lesson2\Lesson2Data\CityBoundaries.shp'  # ap.GetParameterAsText(1)


def get_spatial_reference(shapefile):
    spatial_reference = ap.Describe(shapefile).spatialReference
    print(spatial_reference)
    return spatial_reference


def reproject_in_place(shapefile, spatial_reference):
    out_shapefile = os.path.join(target_folder, shapefile.split('.')[0]) + "_projected"
    try:
        am.Project(shapefile,
                   out_shapefile,
                   spatial_reference,
                   )
        print(f'Successfully reprojected file at {out_shapefile}')
    except Exception:
        print("Error with projection... skipped")


def main(folder, shapefile):
    for file in os.listdir(folder):
        try:
            print(f'Accessing {file}...')
            file_path = os.path.join(target_folder, file)
            template_reference = get_spatial_reference(shapefile)
            reproject_in_place(file_path, template_reference)

        except Exception:
            print("Error in main")
            pass


if __name__ == '__main__':
    main(target_folder, template_shapefile)
