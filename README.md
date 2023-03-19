# 44688-Data Analytics Capstone Project
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
for each fire company and some larger municipalities have made this information
readily available through their city website.

- ### Goals of this Research
The goal of this research is to use municipality incident history to predict future
incident locations including type of location, and incident type, and required
staffing. This information can be useful to departments for resource allocation
allowing for proper staffing, equipment availability, and potential training op-
portunities. Utilizing the historical incident date and time along with location
information, staff utilization, and actions taken, we should be able to make
predictions on future incident requirements. This information can be used to
strategically place staff. Knowing the type of location of the incident, high-rise
apartment, single family home, manufacturing facility, etc., and the type of inci-
dent, allows for planning of equipment allocation and staffing requirements. An
evaluation of the date and time patterns adds further value to staffing needs and
predictions.

## Related Work
Like crime prediction, fire prediction has been evaluated in many municipalities
using several different algorithms for different purposes. FDNY has long been
in the practice, like many urban fire departments, of temporarily relocating
services between fire houses when they are overwhelmed by incidents to ensure
availability for future anticipated incidents[2]. This information was evaluated to
formulate dynamic staffing using algorithms. Data from the San Diego, CA area
was analyzed by a group out of Stanford for predicting emergency incidents as a
project [4]. This work included detailed location information using latitude and
longitude, weather, and demographics of the area. A project out of Vanderbilt
evaluated data from Nashville, TN focusing on the incident severity as a main
factor to prioritize resources, traffic factors, and response times [3]. This an area
of interest that continues to develop.

## Data Collection
Data was obtained for this project through the City of New York open data site
[1] and is structured. It consists of seventeen categorical data types, fifteen of
which are nominal and two that are ordinal along with seven numerical data
types, three of which are continuous and four that are discrete. As of the time
of writing this, the data was last updated April 8, 2022, with the initial creation
on July 27, 2016, and is updated annually. It includes all incidents overseen by
the fire companies including fire, medical and non-fire emergencies. It contains
twenty-four columns and 4.16 million rows. The data is available for download
and is 1.02GB as a csv however it is available through an API endpoint. Data
to be used from this dataset includes the incident type, actions taken, highest
level of care provided, property use, incident date, borough, and zip code. The
incident date will need further extraction to separate year, month and hour of
the day as the relevant areas to evaluate. The current format is YYYY MMM
DD HH:MM:SS XM.

## Data Cleaning

## Data Validation

## Implementing ML Algorithms

## Results and Analysis

## Conclusion

- ### Limitations

- ### Future Work
Future work in this area that would add tremendous value would be incorpo-
ration of other predictive factors that for a comprehensive prediction, such as
crime, natural disaster, weather, and traffic data. It is also noted that more in-
formation is collected by NFIRS than what is represented in this dataset [5].
Collection of a full dataset from NFIRS would allow for more thorough exam-
ination. Population is also relative to the data and is a considering factor that
could be added to future work for further analysis.

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


