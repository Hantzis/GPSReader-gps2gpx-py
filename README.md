# GPSReader-gps2gpx-py
Little Python script for translate GPS .txt files from GPSReader.exe to GPX format.

I wrote this script originally because i've try to upload a 360 video taken with a Insta360 camera to Mapillary. That camera comes with a stitcher, who export a 360 video, that vide can be uploaded to Mapillary, but Mapillarye requests for a separated GPX track file when a video is uploaded. Insta360 stitcher comes with a tool called "GPSReader.exe" which dumps the track of camera record with info like WGS84 coordinates, elevation, datetime, etc; in a txt file with JSON format.

This script translate from this (TXT (actually JSON)):

```json
{"altitude":1550.19995117188,"dts":25,"gps_fix_type":3,"horizontal_accuracy":0.959999978542328,"latitude":20.664298,"longitude":-103.362843666667,"pts":25,"speed_accuracy":0.0,"time_gps_epoch":1530809527.8,"velocity_east":6.65024900436401,"velocity_north":-2.46130895614624,"velocity_up":0.0,"vertical_accuracy":0.959999978542328}
```

To this (GPX (actually XML)):

```xml
  <trkpt lat="20.814938333" lon="-103.461783667">
      <ele>1602.099975586</ele>
      <time>2018-07-10T14:12:41.3Z</time>
  </trkpt>
```

# Dependencies

this scripts uses libraries that you must to install in your python distribution, maybe with pip:

- tqdm
- bs4

# Usage

```bash
python3 gps2gpx.py file.txt
```
The output gpx file will be a file with the same name than original but with .gpx extension created in the same path.

----
Maybe later i'll put features like reproject coordinates or change timezone, etc.
