## Capstone Proposal -- Address Prediction for AirDNA
Tim Kahn / 5.27.2017

#### Overview:
AirDNA has a robust model for predicting the AirBNB revenue potential of a property based on AirBNB rates/occupancy at comparable properties nearby.  As they expand into automatated property valuation -- how much is a property actually worth, given its AirBNB revenue potential? -- they need address-specific information for AirBNB rentals in order to compare directly with market data, like MLS listings.

#### Challenge / Goal:
AirBNB publishes a good deal of information in its listings, but not the address -- you only get that when you book a stay.  Maps on the AirBNB website show the general vicinity of the property as a circle, not as a point; the actual location of the property is randomized within the circle.  My goal is to 'predict' the addresses by comparing features of AirBNB listings to other data (e.g., from county recorder & tax assessor records), and provide a confidence measure for those predictions.

#### Data:
**Datasets:**
* AirDNA's 'proprietary' data for Denver, scraped from AirBNB listings.
* (Hopefully, still TBD) similar data scraped from a competing service (Homeaway, VRBO) that includes reliable latitude/longitude.
* County recorder data
* Tax assessor data

**Possible obstacle:**  
One fundamental challenge is creating labeled training & test data.  The hope is that we can get labels by comparing AirBNB listings to other platforms' listings (Homeaway, VRBO) that reveal latitude/longitude.  Only listings with very close matches (on host name, description, etc.) will be used as training / test data, since this is actually a prediction too!  We believe that there is enough redundancy in listings across platforms for this to work.

#### Ideas / methods
* Attempt to tackle each zip code independently.
* Use a similarity score between features of AirBNB data and tax assessor data to get most likely match, then...
* Use logistic regression, random forest, or boosting to classify correct matches (positive) vs. bad matches (negative).  Features could be boolean or differences:
```
"AirBNB Host Name == First Name on Deed"
"AirBNB data shows swimming pool == Assessor data shows swimming pool"
"Bedrooms on AirBNB listing - Bedrooms in Assessor Data"
```

* Extra credit: Bayesian methods.  If we correctly classify some portion of the properties in a zip code, is our posterior probability of classifying the remaining properties greater than the prior?
* Extra credit: Extracting street numbers from images using a CNN.

#### Presentation:
MVP is a slide presentation and/or poster.  If time and results allow, a web app with a visualization of the model within a given zip code would be awesome.
