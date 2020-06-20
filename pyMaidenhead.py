#!/usr/bin/python3
# ----------------------------------------------------------------------------
#       _____)                     ______               )   ___
#     /                           (, /    )            (__/_____)     /)
#    /   ___   __   _   _ __        /---(  _____/        /       ____(/  _
#   /     / ) / (__(/__(/_/ (_   ) / ____)(_)  /(__     /       (_)(_(__(/_
#  (____ /                      (_/ (         /        (______)
#
# ----------------------------------------------------------------------------

# setup needed packages
import warnings
import argparse
import math
import pyAlphaNumericLookup
import pyGIS


def main():
    """Main entry.  Parse user input"""
    def printConsole(lat, lon, loc):
        strLoc = ""
        if args.verbose:
            if int(lat) in range(0, 90) and int(lon) in range(-180, 0):
                print("Locator: {}".format(strLoc.join(loc)))
                print("Lat: {} North, Lon: {} West".format(abs(lat), abs(lon)))
            elif int(lat) in range(0, -90) and int(lon) in range(-180, 0):
                print("Locator: {}".format(strLoc.join(loc)))
                print("Lat: {} South, Lon: {} West".format(abs(lat), abs(lon)))
            elif int(lat) in range(0, 90) and int(lon) in range(0, 180):
                print("Locator: {}".format(strLoc.join(loc)))
                print("Lat: {} North, Lon: {} East".format(abs(lat), abs(lon)))
            elif int(lat) in range(0, -90) and int(lon) in range(0.0, 180):
                print("Locator: {}".format(strLoc.join(loc)))
                print("Lat: {} South, Lon: {} East".format(abs(lat), abs(lon)))
            else:
                print("Locator: {} is NOT valid".format(strLoc.join(loc)))

        else:
            print("{},{}".format(lat, lon))

    letters = pyAlphaNumericLookup.lookupTable()
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose",
                        help="increase output verbosity", action="store_true")
    parser.add_argument(
        "locator", help="Maidenhead Grid Locator \n ex. FE34,DO46gs,CN23ha24")
    args = parser.parse_args()
    loc = list(args.locator)  # Convert Maidenhead locator to list

    # print(loc)
    size = len(loc)  # Get size of list
    if size == 4:
        # Simplest 2 pair Maidenhead locator
        alpha1 = loc[0]
        alpha2 = loc[1]
        numeric1 = float(loc[2])
        numeric2 = float(loc[3])
        lon = ((dict(letters)[alpha1] * 20) + (numeric1 * 2)) - 180
        lat = ((dict(letters)[alpha2] * 10) + (numeric2 * 1)) - 90
        printConsole(lat, lon, loc)
    elif size == 6:
        # 3 Pair Maidenhead Locator
        alpha1 = loc[0]
        alpha2 = loc[1]
        alpha3 = loc[4]
        alpha4 = loc[5]
        numeric1 = float(loc[2])
        numeric2 = float(loc[3])
        lon = ((dict(letters)[alpha1] * 20) + (numeric1 * 2)) - 180
        lon = lon + dict(letters)[alpha3] * (5/60)
        lat = ((dict(letters)[alpha2] * 10) + (numeric2 * 1)
               ) - 90 + (dict(letters)[alpha4] * 0.04166666666)
        printConsole(lat, lon, loc)
    elif size == 8:
        # 3 Pair Maidenhead Locator
        alpha1 = loc[0]
        alpha2 = loc[1]
        alpha3 = loc[4]
        alpha4 = loc[5]
        numeric1 = float(loc[2])
        numeric2 = float(loc[3])
        numeric3 = float(loc[6])
        numeric4 = float(loc[7])
        lon = ((dict(letters)[alpha1] * 20) + (numeric1 * 2)) - 180 + \
            (dict(letters)[alpha3] * (5/60)) + (numeric3 * (30/3600))
        lat = ((dict(letters)[alpha2] * 10) + (numeric2 * 1)) - 90 + \
            (dict(letters)[alpha4] * (2.5/60)) + (numeric4 * (15/3600))
        printConsole(lat, lon, loc)
    else:
        # Improper Locator
        lat = 9999.9999
        lon = 9999.9999
        printConsole(lat, lon, loc)


if __name__ == "__main__":
    """Main Funtion"""
    main()
