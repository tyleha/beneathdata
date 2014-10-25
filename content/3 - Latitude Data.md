Title: Visualizing my location history with Python, Shapely, and Basemap
Date: 2014-10-08 10:31
Tags: location, maps, python, shapely, basemap 
Category: How-to
Slug: visualizing-my-location-history
Author: Tyler Hartley
Status: draft

The vast majority of us have a little GPS device in our pockets all day long that's recording our location and thus our speed, our direction, our activities, and frankly our lives. Some people regard this as terrifying, but, given access to this data, I see an awesome dataset!

If you're not interested in the learning the code to make these graphs, but know me personally, stick around - you might learn a thing or two about me

Let's also discuss what I've learned about how Android + Google store and track your location

To produce these graphs, you'll need a bunch of packages. 

* Matplotlib
* Basemap
* Numpy
* Pandas
* Shapely
* [Fiona](https://pypi.python.org/pypi/Fiona)
* Descartes

And of course, all this code will be executed usin [IPython](), my best friend.

## Working with location data in Pandas

```python
with open('LocationHistory.json') as fh:
    raw = json.loads(fh.read())

ld = pd.DataFrame(raw['locations'])
del raw #free up some memory
ld.rename(columns={'latitudeE7':'latitude', 'longitudeE7':'longitude', 'timestampMs':'timestamp'}, inplace=True)
# convert to typical units
ld['latitude'] = ld['latitude']/float(1e7) 
ld['longitude'] = ld['longitude']/float(1e7)
ld['timestamp'] = ld['timestamp'].map(lambda x: float(x)/1000)
ld['datetime'] = ld.timestamp.map(datetime.datetime.fromtimestamp)
ld = ld[ld.accuracy < 1000] #Ignore locations with location estimates over 1000m
ld.reset_index(drop=True, inplace=True)
```

Now you've got a Pandas DataFrame called `ld` containing all your location history and related fields. We've got latitude, longitude, and a timestamp (obviously), but we also have accuracy, activitys [sic], altitude, heading...Google is clearly trying to do some complex backend analysis of your locaiton history to infer what you're up to and where you're going. But all we need is those first three.

## Working with Shapefiles in Python

The more I learn about mapping, the more I realize how complex it is. There's a whole world out there of programmers dealing with and analyzing geospatial data. It's a serious industry. But to do what we want to do with maps, we're going to have to become experts in a couple hours. We don't have time to learn proprietary GIS software or write our own methods to analyze map data. But Python being Python, we've already got packages to knock this stuff out. 

[Shapefile](http://en.wikipedia.org/wiki/Shapefile) is a widely-used data format for describing points, lines, and polygons. To work with shapefiles, Python gives us [Shapely](https://pypi.python.org/pypi/Shapely). It's got bindings to GEOS, the engine that will perform a lot of the computation, and a clean syntax. Shapely rocks. To briefly read/write shapefiles, we'll use [Fiona](https://pypi.python.org/pypi/Fiona).

To learn Shapely and write this blog post, I leaned heavily on an article from [sensitivecities.com](http://sensitivecities.com/so-youd-like-to-make-a-map-using-python-EN.html). Go pester that guy to write more stuff. Tom MacWright wrote [a great overview](http://www.macwright.org/2012/10/31/gis-with-python-shapely-fiona.html) of the tools we'll be using.

First up, you'll need to download shapefile data for the part of the world you're interested in. I live in Seattle, which like many cities [provides city shapefile map data](https://data.seattle.gov/dataset/data-seattle-gov-GIS-shapefile-datasets/f7tb-rnup) for free[ref]I grabbed the neighborhoods shapefile.[/ref]. The US Census Bureau provides a ton of national shapefiles [here](https://www.census.gov/geo/maps-data/data/tiger.html).

Next, install Fiona, Shapely, and its dependencies. We'll need to import the Shapefile data we downloaded, which is easy as pie:

```python
shapefilename = r'data\Neighborhoods\WGS84\Neighborhoods'
shp = fiona.open(shapefilename+'.shp')
coords = shp.bounds
shp.close()

w, h = coords[2] - coords[0], coords[3] - coords[1]
extra = 0.01
```

Now we'll leverage Basemap to go about actually plotting our shapefiles

```python
m = Basemap(
    projection='tmerc', ellps='WGS84',
    lon_0=np.mean([coords[0], coords[2]]),
    lat_0=np.mean([coords[1], coords[3]]),
    llcrnrlon=coords[0] - extra * w,
    llcrnrlat=coords[1] - (extra * h), 
    urcrnrlon=coords[2] + extra * w,
    urcrnrlat=coords[3] + (extra * h),
    resolution='i',  suppress_ticks=True)
 
_out = m.readshapefile(shapefilename, name='seattle', drawbounds=False, color='none', zorder=2)
```

We'll need the above basemap for both of the following plots.

------------------

## Choropleth Map

Now we're ready to get to work.

#### Compute time spent in each neighborhood

```python
# set up a map dataframe
df_map = pd.DataFrame({
    'poly': [Polygon(hood_points) for hood_points in m.seattle],
    'name': [hood['S_HOOD'] for hood in m.seattle_info]
})
# Convert our latitude and longitude into Basemap cartesian map coordinates
mapped_points = [Point(m(mapped_x, mapped_y)) for mapped_x, mapped_y in zip(ld['longitude'], ld['latitude'])]
all_points = MultiPoint(mapped_points)
# Use prep to optimize polygons for faster computation
hood_polygons = prep(MultiPolygon(list(df_map['poly'].values)))
# Filter out the points that do not fall within the map we're making
city_points = filter(hood_polygons.contains, all_points)
```

Now, `city_points` contains a list of all points that fall within your map. `hood_polygons` is your collection of polygons representing, in my case, each neighborhood in Seattle. 

So, let's compute our choropleth - how many datapoints fall within each neighborhood? (Warning - depending on the size of the `city_points` array, this could take a _while_.)

```python
def num_of_contained_points(apolygon, city_points):
    return int(len(filter(prep(apolygon).contains, city_points)))
    
df_map['hood_count'] = df_map['poly'].apply(num_of_contained_points, args=(city_points,))
df_map['hood_hours'] = df_map.hood_count/60.
```

So now, `df_map.hood_count` contains a count of the number of gps points located within each neighborhood. But what do those counts really mean? It's hard to extract meaningful information knowing that I collected 2,500 "datapoints" in downtown, except to compare against other neighborhoods. And we could do that. Or we could convert `hood_count` into time...

Turns out, that's **really** easy, for one simple reason. From investigating my location history, it seems that unless my phone is off or without reception, Android reports my location _exactly_ every 60 seconds. Not usually 60 seconds, not sometimes 74 seconds, **_60 seconds_**. So if we make the assumption that I keep my phone on 24/7 (true) and I have city-wide cellular reception (also true), then all we need to do is `hood_count/60.0`, as shown above, and how we're talking in hours. 

#### Plot the choropleth

We've got our location data. We've got our shapefiles in order. All that's left - plot! This code gets a bit wordy for a blog format, so check the Gist out here:

[<h4>**Choropleth Map - See The Code**</h4>](https://gist.github.com/tylerhartley/c5ea21e2a4879fcc4151)

Note that you can also remove time spend at certain areas (home, work) from your analysis easily:

---------------

## Hexbin Map

Great way to visualize general density. Think of it as a 3D histogram. With essentially no extra work, we can throw up a hexbin plot of our data, defining the number of hexbins again with `gridsize`. 

[<h4>**Hexbin Map - See The Code**</h4>](https://gist.github.com/tylerhartley/c5ea21e2a4879fcc4151)

I've increased the hexbin size and obfuscated the data, only because this graph is pretty telling about where I live and what I do!

--------------

## Map of Flights Taken

Here's the images, here's the algorithm

Now, ordinarily you would just think this algorithm could be incredibly simple. "If speed is greater than ~200kph, you're flying" because honestly, when else are you going that fast? But there are problems with that approach:

1. GPS location can be inaccurate. You can use the "accuracy" field to filter out cases like this, but not always. Think about it - if we're sampling location at one datapoint per minute (what is generally available in my Google Takeout data) then all it would take is to be off by 200/60 or 3.3 km (~2 miles) and your algorithm would think you were flying! Looking through my location history, this definitley happence ~once a week. So we'll have to address this concern in the algo.
2. This one caught me off guard. When I fly, I activate "airplane mode" which, as far as I could tell, deactivated wifi/cellular data/GPS. Turns out? It only deactivates the first two. GPS remains active. Consequently, during a given flight, my phone will occasionally collect an (accurate!) location in mid-flight. If we're not careful, our algorithm could interpret each of these datapoints as a layover, and break our single flight into many small ones. That's no good.

We need something quick and dirty that can address these concerns. It really isn't too hard:

Now, finding consecutive numbers in an array is actually harder than it looks. I ended up going down a stackoverflow rabbit hole trying to optimize the search algorithm and, in the end, stuck with the first thing I came up with. 

[<h4>**Flights Taken Map - See The Code**</h4>](https://gist.github.com/tylerhartley/c5ea21e2a4879fcc4151)