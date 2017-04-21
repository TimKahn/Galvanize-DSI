Data Viz for DS Notes
=====================

Objectives:
-----------

1. Understand the key principles of informative design.
2. Put these principles to use with Python packages, including:
    •seaborn
    •bokeh
    •plotly
    •folium


"The Thinking Eye"
---------------------

How do we display information so that it is easily interpretable to the viewer?

Our eyes are connected to or brains...

But we are easily fooled! Think of any optical illusion, sometimes our brains get in the way...

How can we avoid mis-interpretation?

The Grammar of Graphics
---------------------

We can control how our data gets represented in a graphic _(plot, graph, chart, etc.)_.

We can change:

    •size
    •color
    •weight
    •position
    •shape
    •scale
    •etc...

#### Size:

Bubblecharts: we change the size of the marker printed to reflect the input data.

#### Color:

Scatterplots: we change the color of the points to reflect the classification of the data.

Or change the opacity of the points to give us a sense of density in the plot.

We can also give a **colorscale** to show a range of secondary data values.

#### Weight:

Changing the weight of lines helps key in the reader about what is important in the figure.

#### Position:

By changing where things are positioned, we are giving a sense of hierarchy or importance or a progression of time. _(Gestalt - things are not seen in a vacuum. They are influenced by what is around it)_.

#### Shape:

Many times we won't have the luxury of reproducing or graphics in full-color _(especially if we are publishing / printing the result)_. We can use shape or texture to represent classes in these cases.

#### Scale:

Many times we are looking for subtle changes in values in the data, and others we are looking for vast differences. We can change the scale of our axes to help us visualize linear or log based effects.

Pitfalls
--------

Don't Do What Donny Don't Does...

As is often the case, **Less is More**! Do not overload our readers with too much information. Keep it simple, or risk losing interpretability.

_Rediculogram_

Our eyes work best with contrast. Don't use colors that aren't readable _(like putting small, bright yellow points on a light gray background)_.

Why not just use the default colors? The greyscale equivalencies are not the same. Fully saturated yellow does not _read_ as dark as fully saturated red.

_Joseph Albers and %grayscale equivalencies_

Or use too many saturated colors. You will just confuse the reader as to what is important.

_Bad map with waaay too many colors_

Some Terminology
----------------

#### Common Color Spaces
**RGBa** - Red, Green, Blue, alpha.

This gives how much of each color gets added from each channel _(with alpha being the opacity)_. Since most displays work from adding red, green, and blue pixels this is pretty standard for digital graphics. RGB values will typically be in 8-bit scale _(0-255)_, and rarely be scaled to [0, 1]. Alpha values are almost always [0, 1], or a percentage equivalent.

**Hexidecimal**.

This is an RGB encoding that scales values to two Hexidecimal values per channel _(so ranging from '00' to 'FF')_. It is usually denoted with a '#' in front. For example red looks like this: '#FF0000', and green: '#00FF00'. This is a common standard for web / HTML / CSS applications.

**CMYK** - Cyan, Magenta, Yellow, Black _(or Process Color)_.

For physically printed material, it will often go through a four process printing press layering ink from these four colors.

**HSV** - Hue, Saturation, value.

This is often referred to as a 'cylidrical color geometry'. Hue is the angular component _(with primary red at 0deg, primary green at 120deg, and primary blue at 240deg)_. Saturation is the radial dimension with range[0,1] with zero saturation being white for all hues, and a saturation of one being the full expression of that hue. Value is the central or axial dimension and is in the range [0,1] with black at zero value and the full hue at a value of one.

#### Gamut

This is the range of all colors that can be represented. This is limited by the colorspace used, the process in which it is being printed, or just by human perception.

#### Pixel

The smallest portion of an image is the pixel, a portmanteau of _"picture"_ and _"element"_. The 3d volume equivalent is a voxel.

#### DPI and LPI _(or Resolution)_

Dots per inch and lines per inch. This is how many pixels will occupy a physical space. Screen resolution will typically be 72 or 92 dpi depending on the OS. For printing purposes, a dpi above 300 is desirable. Resolution, literally is the ability to resolve two items being distinct _(think about statistical Power here)_.

Empty resolution / Nyquist Sampling / Aliasing / Moiré

SVG and scale independent graphics.


IN THE YEAR 2000
----------------

Interactive plotting...plotly.

Have students recreate chloropleth of murder data from Erich's pandas lecture.

John Snow - Cholera Maps
