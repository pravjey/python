from bottle import default_app, route, template, request
import requests
import math
import time



# Global variables

HOST = "drpjeya.pythonanywhere.com"
responsive = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"

google_api_key = ""
google_client_id = ""
google_client_secret = ""

@route('/')
def home():
    output = template("home.tpl")
    return output

def getData(api):
    request = requests.get(api)
    request_json = request.json()
    return request_json

def haversine(a1,a2,b1,b2):
    radius = 6371
    phi1 = a1*math.pi/180
    phi2 = a2*math.pi/180
    lambda1 = b1*math.pi/180
    lambda2 = b2*math.pi/180
    phi_delta = phi2 - phi1
    lambda_delta = lambda2 - lambda1
    a = (math.sin(phi_delta/2))**2 + math.cos(phi1)*math.cos(phi2)*(math.cos(lambda_delta/2))**2
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    d = (radius * c)/1000
    return d

def getDistance(latitude, longitude):
    distance = 0
    for i in range(0,len(latitude)-1,2):
        distance = distance + haversine(latitude[i], latitude[i+1],longitude[i],longitude[i+1])
    return distance

def getMap(previousLat2,previousLong2,startLat,startLong):
    marker1 = "markers=size:small%color:red%7Clabel:S%7C" + str(startLat)+","+str(startLong)
    marker2 = "markers=size:small%color:red%7Clabel:C%7C" + str(previousLat2)+","+str(previousLong2)
    staticmap = "https://maps.googleapis.com/maps/api/staticmap?center="+str(previousLat2)+","+str(previousLong2)+"&zoom=6&size=600x600&maptype=roadmap&" + marker1 + "&" + marker2 + "&key="+google_api_key
    embedmap = "https://www.google.com/maps/embed/v1/directions?key="+google_api_key+"&origin="+str(startLat)+","+str(startLong)+"&destination="+str(previousLat2)+","+str(previousLong2)
    image1 = "<img src=\"" + str(staticmap) + "\"</img>"
    image2 = "<iframe width=\"600\" height=\"600\" frameborder=\"10px\" style=\"border:1px solid black;\" src=\"" + embedmap + "\" allowfullscreen></iframe>"
    return image1, image2

def getLocation(latitude,longitude):
    location_dict = getData("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+str(latitude)+"% "+str(longitude)+"&inputtype=textquery&key="+google_api_key)
    if (len(location_dict["candidates"]) == 0) & ("formatted_address" in location_dict["candidates"][0].keys()):
        location = "\t" + location_dict["candidates"][0]["formatted_address"]
    else:
        #placeid = str(location_dict["candidates"][0]["place_id"])
        #placedetails = getData("https://maps.googleapis.com/maps/api/place/details/json?place_id="+placeid+"&key="+google_api_key)
        #if placedetails["result"]["formatted_address"] == placedetails["result"]["name"]:
        n = 1000
        nearby =  getData("https://maps.googleapis.com/maps/api/place/nearbysearch/json?" + str(latitude)+","+str(longitude)+"&radius=" + str(n) + "&key="+google_api_key)
        if nearby["results"]:
            latitude = nearby["results"][0]["geometry"]["location"]["lat"]
            longitude = nearby["results"][0]["geometry"]["location"]["lng"]
            location = "\t " + str(n) + " metres near " + str(getLocation(latitude,longitude))
        else:
            n += 1000
            location = "\t" + str(getData("https://maps.googleapis.com/maps/api/place/nearbysearch/json?" + str(latitude)+","+str(longitude)+"&radius=" + str(n) + "&key="+google_api_key))
    return location

def issPage(previousLat2,previousLong2,distance,clock,startLat,startLong):
    title = "<title>As far as the International Space Station flies</title>" + responsive
    heading = "<h1>" + "How fast does ths International Space Station go?" + "</h1>"
    backlink = "<p><a href=\"\/" + HOST + "\">Back to home page</a>"
    startPos = "Starting position of ISS \t Latitude: " + str(startLat) + "\tLongitude: " + str(startLong) + "\t" + str(getLocation(startLat,startLong))
    closePos = "<p>Closing position of ISS \t Latitude: " + str(previousLat2) + "\tLongitude: " + str(previousLong2) + "\t" + str(getLocation(previousLat2,previousLong2))
    distanceText = "<p>Distance travelled so far: " + str(distance) + " km in " + str(clock) + " seconds."
    speed = distance / clock
    speedText = "<p>Average speed: " + str(speed) + " km//s."
    mapImage1, mapImage2 = getMap(previousLat2,previousLong2,startLat,startLong)
    mapImage1 = "<h2>Static map showing ISS position</h2>" + mapImage1
    mapImage2 = "<h2>Dynamic map showing ISS position (Zoom in/out)</h2>" + mapImage2
    return title + heading + startPos + closePos + distanceText + speedText + "<p>" + mapImage1 + mapImage2 + backlink

@route('/iss', method="POST")
def getIss():
    timeTotal = int(request.forms["timeTotal"])
    timeInterval = int(request.forms["timeInterval"])
    issLocation = getData('http://api.open-notify.org/iss-now.json')
    startLat = previousLat1 = float(issLocation["iss_position"]["latitude"])
    startLong = previousLong1 = float(issLocation["iss_position"]["longitude"])
    latitude = [previousLat1]
    longitude = [previousLong1]
    clock = 0
    while clock < timeTotal:
        start = time.time()
        end = time.time()
        while (end-start) < timeInterval:
            issLocation = getData('http://api.open-notify.org/iss-now.json')
            previousLat2 = float(issLocation["iss_position"]["latitude"])
            previousLong2 = float(issLocation["iss_position"]["longitude"])
            end = time.time()
        latitude.append(previousLat2)
        longitude.append(previousLong2)
        clock = clock + (end - start)
        previousLat1 = previousLat2
        previousLong1 = previousLong2
    distance = getDistance(latitude,longitude)
    output = issPage(previousLat2,previousLong2,distance,clock,startLat,startLong)
    return output

application = default_app()
