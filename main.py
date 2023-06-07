"""
This was created for Penn State University GEOG485 Lesson 2 by Kurt Neinstedt.
This script takes a folder directory and a shapefile path as inputs, and reprojects data in the folder directory
to the projection of the shapefile.
"""

import arcpy as ap
import arcpy.management as am

target_folder = r'C:\GEOG485\Lesson2\Lesson2Data'
template_shapefile = r'C:\GEOG485\Lesson2\Lesson2Data\CountyLines.shp'

messages = []


def get_spatial_reference(shapefile) -> object:
    spatial_reference = ap.Describe(shapefile).spatialReference
    return spatial_reference


def is_same_spatial_reference(shapefile_1, shapefile_2) -> bool:
    if get_spatial_reference(shapefile_1).name != get_spatial_reference(shapefile_2).name:
        return True
    else:
        return False


def reproject_in_place(file, template_reference):
    try:
        am.Project(file,
                   file.split('.')[0] + "_projected",
                   template_reference,
                   )
        print(f'Successfully reprojected file at {file}')
        messages.append(file)
    except Exception:
        print("Error with projection... skipped")


def main():
    ap.env.workspace = target_folder
    files = ap.ListFeatureClasses()
    template_reference = get_spatial_reference(template_shapefile)

    for file in files:
        if is_same_spatial_reference(file, template_shapefile):
            reproject_in_place(file, template_reference)
        else:
            print(f'{file} is already in {template_reference.name} and has been skipped.')

    print(f'Reprojected the following files: {messages}')


if __name__ == '__main__':
    main()
