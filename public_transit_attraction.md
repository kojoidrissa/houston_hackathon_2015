#Working with a team to find attractions reachable by public transit
I've added in the "Bike + Bus/Train" option

##Min Viable
-  Location start
-  Category: Food or drink
-  Transit time
    +  Round trip based on duration of stay


##Transit times
We want people to be able to sort their trips based on transit time. So, we need to know 
-  How does the Houston Metro app calcuate trip times?
-  How does Google Maps calculate it's trip times? Do they pull from Houston Metro's API or do they have their own thing?


##ArcGIS account
HOUHACK15
rastafarian15
city of birth: Narnia

-  esriurl.com/begingeo: GeoDev How-tos: Getting Started with the ArcGIS Platform for Developers
-  [ArcGIS Services Directory](http://mycity.houstontx.gov/ArcGIS10/rest/services/)
-  [Welcome to the official City of Houston's My City ArcGIS Maps](http://mycity.maps.arcgis.com/home/)

ArcGIS has a routing service; it's premium & requires credits.

HTML5 Geolocation
Conference room, via my laptop: (29.751984600000004, -95.37531399999999)



##STOPS
-  stop_id
-  stop_lat
-  stop_long
-  stop_name

##STOP_TIMES
-  trip_id
-  arrival_time
-  departure_time
-  stop_id
-  stop_sequence

##TRIPS
-  trip_id
-  route_id

##ROUTES
-  route_id
-  route_short_name
-  route_long_name