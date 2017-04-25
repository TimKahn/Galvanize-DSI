The Birth of Modern Epidemiology
=========================

London in 1854 had a huge problem on its hands. Hundreds of citizens were dying rapidly from Cholera.

At the time the mortality rate for someone who contracted cholera was over 50%. So staying healthy was of utmost importance. But what was the source of the outbreak?

One pioneering physician decided to find where the root of the problem was. Dr. John Snow had some intuition that contaminated public water pumps were the cause. Because indoor plumbing was rare, most Londoners got their water from these pumps in the streets. But how could he gain some insight about his intuition and find _which_ water pump was the problem?

Like all good scientists, he started by collecting data. Going door-to-door throughout Soho, Dr. Snow with the help of a local Reverend collected information on where residents were dying. Because he was looking for _geographical_ clusters, Dr. Snow used a map to tally how many people had died from cholera in each house. Information about hotspots could now be easily interpreted visually and the offending water pump would most likely be the one closest to the cluster.

Let's now recreate John Snow's famous cholera map using python and Folium _(a mapping package that uses leaflet.js)_.

First we will need to install Folium _(use conda)_, a package that let's us leverage the power JavaScript mapping tools inside python:

`$ conda install folium`

Next we will have to get Dr. Snow's data in a format we can map easily. in the `data` folder you'll find a csv file containing latitude and longitude in the `geometry` column, and data for the number of residents that died at that location in the `count` column.

Like is often the case in Data Science, you will have to clean up your data file. You have to strip out unwanted formatting for the Lat and Lon values.

**Hint:** Use the RegEx package `re` to substitute out the formatting we don't need and to split into separate values for Lat and Lon.

We should now have three columns, one for death count, one for latitude, and one for longitude.

Look at the tail of your data. Do you notice something funny?

The locations of the public water pumps have been marked with `count` values of -999. Split this locations into a different dataframe.

Now, let's start building the map.

```python
import folium
first_map = folium.Map(location = [51.513, -0.137])
```

To write out our map as a local html file we can just call

```pyhton
first_map.save("Cholera.html")
```

Find your `Cholera.html` file and open it. You'll see that we get a map of London that runs from a local file that gives us the interactions that we are accustomed to _(like panning, zooming, etc)_.

Let's start adding our points from Dr. Snow's data. In `folium` we add markers with the following syntax:

```python
folium.Marker(location = [51.513418, -0.13793]).add_to(first_map)
```

This needs to be done before we save our map obviously. Unfortunately, `folium` only allows us to write one marker at a time. Use a `for` loop to add all of your data points one-by-one.

By now you have probably noticed that our map breaks almost every rule we talked about in lecture. So let's clean things up a bit. We only need to look at points in Soho, not all of London. When initializing your map object set the `zoom_start` value of our new map to be 16.

Now change the markers to be `CircleMarker`s. Use the `color` and `fill_color` arguments to change the border and fill colors of our points. Pass these colors using hexadecimal or RGBa values as strings. It should look something like this:

```python
folium.CircleMarker(location=[your_latitude, your_longitude],
                    color='rgba(171,52,40, 0.35)').add_to(your_map)
```
Make good color choices here! Think about contrast, brightness, and keeping your map **readable**.

You can also use the `radius` argument to change the size of the CircleMarkers.

The default map has a lot of stuff that makes it hard to read. At the moment, We aren't too concerned with where the closest shoe store is. We can change the style of the map using different `tiles`. These are the images stitched together to build what is the backdrop of your map. You can do this when you initialize your map object:

```python
color_map = folium.Map(location=[51.513, -0.1378],
                        tiles="tile name")
```

Some tile choices include `"Stamen Terrain"`, `"Stamen Toner"`, `"Stamen Watercolor"`, `"Cartodb dark_matter"`, `"Cartodb Positron"`. Pick one you think emphasizes the data, and not the map itself.

Once you make a map you are happy with, try to answer the original question: which water pump would you suspect as the culprit of the cholera outbreak?

#### Extra Credit:

**1.)** Change the size of the points based on the `count` value associated with that position.

**2.)** Let's make the assumption that people are mostly lazy. They probably only get their water from the closest pump. Change the color of your points based on which water pump is the closest. Pick a color for each pump location and color your points based on the pump that is nearest.

**3.)** Let's reframe this problem. Rather than plot the points where the fatalities occurred, plot a `CircleMarker` for each pump that is sized based on the total of closest fatalities.


#### References:

Data from here:

 https://fusiontables.google.com/DataSource?docid=147wlDisDp6NnpNxHQpbnjAQ-iW4dR2MAmFdQxYc#rows:id=1

 This assignment was inspired by this blog post:

http://smartdatawithr.com/en/2017/02/19/leaflet-or-how-geospatial-analysis-can-save-lifes/

More info on folium can be found here:

https://folium.readthedocs.io/en/latest/quickstart.html#getting-started

More info on Dr. John Snow at Wikipedia:

https://en.wikipedia.org/wiki/John_Snow
