import sys, time, json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from tqdm import tqdm
import xml.dom.minidom

args = sys.argv

with open(args[1], encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

soup = BeautifulSoup('<gpx version="1.1" creator="Nizhi Saeba" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"><trk><trkseg></trkseg></trk></gpx>', features='xml')

puntos = data['extended_gps_info']
print("\n\nConvirtiendo " + str(len(puntos)) + " puntos GPS a GPX\n")

for i in tqdm(puntos):

    punto = soup.new_tag("trkpt", lat=i['latitude'], lon=i['longitude'])
    punto.append(soup.new_tag("ele"))
    punto.ele.append(str(i['altitude']))
    punto.append(soup.new_tag("time"))
    punto.time.append((datetime.fromtimestamp(i['time_gps_epoch']) + timedelta(hours=0)).strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
    soup.trk.trkseg.append(punto)

print("Escribiendo GPX...")
xml_str = xml.dom.minidom.parseString(str(soup))
pretty_xml_as_string = xml_str.toprettyxml()
pretty_xml_as_string += "\n"

with open(args[1].split(".")[0] + ".gpx", "w") as f:
    f.write(pretty_xml_as_string)

print("Finalizado")
