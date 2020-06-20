# pyMaidenhead

## Convert Maidenhead locator into Latitude & Longitude

### Requirements

* python3 imports:
  * argparse

### Usage

* python3 pyMaidenhead.py (locator)
* python3 pyMaidenhead.py -v (--verbose) (locator)
* python3 pyMaidenhead.py -h (--help)

* Simple Output
  * All positions in decimal degrees
  * (-) for West of Meridian, or South of Equator
    * ex. 57.2345, -112.34567

* Verbose Output
  * All positions in decimal degrees
  * Locator: DO46GS
    Lat: 56.74999999988 North, Lon: 111.5 West
