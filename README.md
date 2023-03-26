# 44688-Data Analytics Capstone Project
## 03/13/23 - 04/28/23

# ![Fire Dept logo](https://github.com/ddwalk77/FDIP/blob/main/FD_logo.png "FD_logo") FDIP (Fire Department Incident Prediction)

Debra D. "DeeDee" Walker

Northwest Missouri State University, Maryville MO 64468, USA

S554373@nwmissouri.edu

- ### Abstract

- ### Keywords
fire department · 911 dispatching · emergency · machine learning

## Introduction
Fire departments are not only composed of fire fighters that fight fire, but EMT,
paramedic, and rescue. They respond to a variety of calls through 911 dispatch-
ing. They respond with the police department when needed, to vehicle accidents,
medical calls as the paramedics operate through the same facility or are also fire
fighters, and various rescue operations due to water, machinery, or chemical in-
cidents to name a few. Incidents can vary in number of people needed, the type
of services required, and equipment needed. Because of the diversity in services
required by fire departments due to incident and location types, and addition-
ally requiring the fastest response time, resources must be readily available.
Resources include human resources and equipment. All incidents are logged by
responding first responders through the National Fire Incident Reporting System
by each fire company and some larger municipalities have made this information
readily available through their city website.

- ### Goals of this Research
The goal of this research is to use municipality incident history to predict future
incident locations including type of location, and incident type, and required
staffing. This information can be useful to departments for resource allocation
allowing for proper staffing, equipment availability, and potential training op-
portunities. Utilizing the historical incident date and time along with locations,
we should be able to make predictions on future incident requirements. This in-
formation can be used to strategically place staff. Knowing the type of location
of the incident, high-rise apartment, single family home, manufacturing facility,
etc., and the type of incident, allows for planning of equipment allocation and
staffing requirements. An evaluation of the date and time patterns adds further
value to staffing needs.

## Related Work
Like crime prediction, fire prediction has been evaluated in many municipalities
using several different algorithms for different purposes. FDNY has long been
in the practice, like many urban fire departments, of temporarily relocating
services between fire houses when they are overwhelmed by incidents to ensure
availability for future anticipated incidents[2]. This information was evaluated to
formulate dynamic staffing using algorithms. Data from the San Diego, CA area
was analyzed by a group out of Stanford for predicting emergency incidents as a
project [5]. This work included detailed location information using latitude and
longitude, weather, and demographics of the area. A project out of Vanderbilt
evaluated data from Nashville, TN focusing on the incident severity as a main
factor to prioritize resources, traffic factors, and arrival times [3].

## Data Collection
Data was obtained for this project through the City of New York open data site
[1] and is structured. It consists of seventeen categorical data types, fifteen of
which are nominal and two that are ordinal along with seven numerical data
types, three of which are continuous and four that are discrete. As of the time
of writing this, the data was last updated April 8, 2022, with the initial creation
on July 27, 2016, and is updated annually. It includes all incidents overseen
by fire companies including fire, medical and non-fire emergencies. It contains
twenty-four columns and 4.16 million rows. The data is available for download
and is 1.02GB as a .csv however it is available through an API endpoint. Initially
data to be used from this dataset was noted as the incident type, actions taken,
highest level of care provided, property use, the incident date, borough, and zip
code. The incident date will need further extraction to separate year, month and
hour of the day as the relevant areas to evaluate. The current format is YYYY
MMM DD HH:MM:SS XM.

## Data Cleaning
Initially the data was evaluated on the website from where it was obtained. The
initial review led to the decision to only keep the following features: IM INCIDENT KEY,
INCIDENT TYPE DESC, INCIDENT DATE TIME, UNITS ONSCENE, HIGHEST LEVEL DESC,
TOTAL INCIDENT DURATION, ACTION TAKEN1 DESC, PROPERTY USE DESC, ZIP CODE,
BOROUGH DESC. The dataset was then loaded in to a Python pandas dataframe
and all except the above features were dropped. From there each feature was
handled as follows:

– IM INCIDENT KEY was not altered. This is a unique value for each incident
and is not duplicated.

– INCIDENT TYPE DESC value counts revealed that this field needed to be cat-
egorized. This was completed using the NFIC Incident type cheat sheet [4]
where the series indicates the category. INCIDENT CATEGORY was created to
contain this value and INCIDENT TYPE DESC was dropped. Categories include:
• FIRE
• OVERPRESSURE RUPTURE, EXPLOSION, OVERHEAT-NO FIRE
• RESCUE & EMS
• HAZARDOUS CONDITION-NO FIRE
• SERVICE CALL
• CANCELED, GOOD INTENT
• FALSE ALARM FALSE CALL
• SEVERE WEATHER & NATURAL DISASTER

– INCIDENT DATE TIME was converted to datetime64[ns] and filtered for years
2017-2021. The format is YYYY MMM DD HH:MM:SS XM. The day of the
week and hour of the call were extracted and added as a feature, Day of week
and Hour of day.

– Null values in UNITS ONSCENE were replaced by the mean and the feature
was converted to an integer. Value counts revealed the need for categoriza-
tion and seven categories were created and assigned ranging from one unit to
seven or more units. There were 70,433 replacements made, 3%, with value
of 2.

– HIGHEST LEVEL DESC value counts also revealed the need to simplify and
clean redundant data. Based on counts, the data was placed in seven cat-
egories with one being a lower level incident and seven being the highest.
LEVEL CATEGORY was created to contain this value. HIGHEST LEVEL DESC was
then dropped as the new category replaced this value. Records with null val-
ues were removed. This was 106 records which was .005%.

– TOTAL INCIDENT DURATION is in seconds so this value was converted to hours
and rounded to two decimal places. From here, the data was categorized in
to seven categories: <=15min, 15min-30min, 30min-45min, 45min-1hr, 1-
2hr, 2-3hr, and 3hr>. Records with null values were removed. This was 622
records which was .03%. The duration represents the time from the initial
incident date time to when the scene was cleared.

– ACTION TAKEN1 DESC value counts revealed that similar details that were
represented in INCIDENT TYPE DESC. Due to the complexity and the simpli-
fication through categorization, this feature was dropped.

– Value counts on PROPERTY USE DESC revealed that the majority of the values
are listed as undetermined so this feature was dropped.

– Value counts on ZIP CODE revealed an invalid zip code 99999. This was re-
placed with the highest count zip code per respective borough. Null zip code
rows were dropped as there were only nine records. Zip codes are in 5 digit
format.

– BOROUGH DESC was not altered and includes the five boroughs: 1 - Manhattan,
2 - Bronx, 3 - Staten Island, 4 - Brooklyn, 5 - Queens.

Once complete, the data was exported as a clean csv, fdip clean.csv and
loaded on the project site. The final dataset contains 2,348,330 records with no
null values and ten attributes. Final attributes and data types are:
– IM INCIDENT KEY: object
– INCIDENT DATE TIME: datetime64[ns]
– UNITS ONSCENE: object
– TOTAL INCIDENT DURATION: object
– ZIP CODE: object
– BOROUGH DESC: object
– INCIDENT CATEGORY: object
– LEVEL CATEGORY: object
– Day of week: object
– Hour of day: int64

## Data Validation

## Implementing ML Algorithms

## Results and Analysis

## Conclusion

- ### Limitations

- ### Future Work
Future work in this area that would add tremendous value would be incorpo-
ration of other predictive factors that for a comprehensive prediction, such as
crime, natural disaster, weather, and traffic data. It is also noted that more in-
formation is collected by NFIRS than what is represented in this dataset [7]. The
collection of a full dataset from NFIRS would allow for more thorough exami-
nation. Initially the property type was of interest but this field was often listed
as undetermined so it was not of use. Population is also relative to the data and
is a considering factor that could be added to future work for further analysis.

## References
[1] FDNY: Incidents responded to by fire companies,
https://data.cityofnewyork.us/Public-Safety/Incidents-Responded-to-by-Fire-Companies/tm6d-hbzd

[2] Kolesar, P., Walker, W.E.: An algorithm for the dynamic relocation of fire compa-
nies. Operations research 22(2), 249–274 (1974)

[3] Mukhopadhyay, A., Vorobeychik, Y.: Prioritized allocation of emergency responders
based on a continuous-time incident prediction model. In: International Conference
on Autonomous Agents and MultiAgent Systems (2017)
[4] Romero, T., Barnes, Z., Cipollone, F.: Predicting emergency incidents in san diego.
CS229. Stanford School of Engineering, Tech. Rep (2017)
[5] USFA: National fire incident reporting system complete reference guide,
https://www.usfa.fema.gov/downloads/pdf/nfirs/NFIRSC ompleteRef erenceGuide2015.pdf

[6] USFA: National fire incident reporting system,
https://www.usfa.fema.gov/nfirs/

[7] USFA: National fire incident reporting system complete reference guide,
https://www.usfa.fema.gov/downloads/pdf/nfirs/NFIRSCompleteReferenceGuide2015.pdf