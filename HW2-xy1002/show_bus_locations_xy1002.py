import urllib.request as urllib
import sys
import json

import numpy as np


def get_jsonparsed_data(url):
    """
    from http://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """

    response = urllib.urlopen(url)
    return json.loads(response.read().decode("utf-8"))

apikey = sys.argv[1]
busline = sys.argv[2]
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'%(apikey,busline)

jsonData = get_jsonparsed_data(url)


num = np.size(jsonData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
print ('Bus Line : {}'.format(busline))
print ('Number of Active Buses : {}'.format(num))
for i in range(0,num):
   Latitude = get_jsonparsed_data(url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
   Longitude = get_jsonparsed_data(url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
   print ('Bus {} is at latitude {} and longitude {}'.format(i,Latitude,Longitude))


