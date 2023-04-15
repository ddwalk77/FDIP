# 44688-Data Analytics Capstone Project
## 03/13/23 - 04/28/23

# ![Fire Dept logo](https://github.com/ddwalk77/FDIP/blob/main/FD_logo.png "FD_logo") FDIP (Fire Department Incident Prediction)

Debra D. "DeeDee" Walker

Northwest Missouri State University, Maryville MO 64468, USA

S554373@nwmissouri.edu

Report: https://www.overleaf.com/read/trcfgsnvjqds

- ### Abstract
Fire departments are considered first responders and respond
to a multitude of incidents at any given time. The potential to predict
incidents similar to how crime is currently predicted, could prove advantageous
for strategic planning. Utilizing the location, date, and time,
predictability of a broad incident type, duration, and units required, was
examined. New York City was selected due to the amount and availability
of information. Data from 2017 through 2021 was utilized, with sixteen
features. The total final dataset consists of 2,340,414 records. Independent
variables were narrowed between two and five features. Dependent
variables were narrowed between one and three features. The data was
analyzed to gain insights before implementing machine learning algorithms
to further determine predictability. Through data analysis and
further through algorithm implementation, it was discovered that location,
data, and time is not enough information to predict a broad incident
type, duration, and/or units required. The best result obtained from an
algorithm was the same information extracted from descriptive analytics.
We conclude that incidents are too random and further data would be
needed, or a more detailed objective, to determine better predictability.

- ### Keywords
fire department · 911 dispatching · emergency · machine learning

## Introduction
Fire departments are not only composed of fire fighters that fight fires, but EMT,
paramedic, and rescue. They respond to a variety of calls through 911 dispatching
They respond with the police department when needed, to vehicle accidents,
medical calls as the paramedics operating through the same facility who are also
fire fighters, and various rescue operations due to water, machinery, or chemical
incidents to name a few. Incidents can vary in number of people needed,
the type of services required, and necessary equipment. Because of the diversity 
in services required by fire departments due to incident and location types,
and additionally requiring the fastest response time, resources must be readily
available. Resources include human resources and equipment. All incidents are
logged through the National Fire Incident Reporting System [7] by responding
first responders within each fire company and some larger municipalities have
made this information readily available through their city website.

- ### Goals of this Research
The goal of this research is to use municipality incident history to predict future
incident type and required staffing for each area. This information can be useful
to fire departments for resource allocation allowing for proper staffing and equipment
availability. For each area, utilizing the historical incident date and time,
predictions on future incident requirements such as staff and equipment needs,
the type of incident, and duration, should be possible. This information can be
used to strategically place staff within the city in anticipation of an incident.

## Related Work
Like crime prediction, fire prediction has been evaluated in many municipalities
using several different algorithms for different purposes. FDNY has long been
in the practice, like many urban fire departments, of temporarily relocating
services between fire houses when they are overwhelmed by incidents to ensure
availability for future anticipated incidents[2]. This information was evaluated to
formulate dynamic staffing using algorithms. Data from the San Diego, CA area
was analyzed by a group at Stanford for predicting emergency incidents as a
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
the highest level of care provided, property use, the incident date, borough, and zip
code. The incident date needs further extraction to separate year, month and
hour of the day as the relevant areas to evaluate. The current format is YYYY
MMM DD HH:MM:SS XM.

## Data Cleaning
Initially the data was evaluated on the website from where it was obtained. The
initial review led to the decision to only keep the following features: 
IM INCIDENT KEY, INCIDENT TYPE DESC, INCIDENT DATE TIME, UNITS ONSCENE, 
HIGHEST LEVEL DESC, TOTAL INCIDENT DURATION, ACTION TAKEN1 DESC, PROPERTY USE DESC, 
ZIP CODE, BOROUGH DESC. The dataset was then loaded in to a Python pandas dataframe
and all except the above features were dropped. From there each feature was handled 
as follows:

– IM INCIDENT KEY is a unique value for each incident however duplicate records
were discovered and removed. This removed 7,915 records. This was complated
after filtering date by year.

– INCIDENT TYPE DESC value counts revealed that this field needed to be
categorized. This was completed using the NFIC Incident type cheat sheet [4]
where the series indicates the category. INCIDENT CATEGORY was created to
contain this value and INCIDENT TYPE DESC was dropped with a number
being assigned in a new feature, INCIDENT CATNUM.

Categories include:

    • FIRE
    • OVERPRESSURE RUPTURE, EXPLOSION, OVERHEAT-NO FIRE
    • RESCUE & EMS
    • HAZARDOUS CONDITION-NO FIRE
    • SERVICE CALL
    • CANCELED, GOOD INTENT
    • FALSE ALARM FALSE CALL
    • SEVERE WEATHER & NATURAL DISASTER

-INCIDENT DATE TIME was converted to datetime64[ns] and filtered for years
2017-2021. The format is YYYY MMM DD HH:MM:SS XM. The day of
the week and hour of the call were extracted and added as new features,
Day of week with a corresponding number value in DAY NUM, Month, and
Hour of day.

– Null values in UNITS ONSCENE were replaced by the mean and the feature
was converted to an integer. Value counts revealed the need for categorization
and seven categories were created and assigned ranging from one unit to
seven or more units. There were 70,433 replacements made, 3%, with the value
of 2. An additional categorical feature was created, UNITS CATEGORY.

– HIGHEST LEVEL DESC value counts also revealed the need to simplify and
clean redundant data. Based on counts, the data was placed in seven categories
with one being a lower level incident and seven being the highest.
LEVEL CATEGORY was created to contain this value. HIGHEST LEVEL DESC was
then dropped as the new category replaced this value. Records with null
values were removed. This was 106 records which was .005%.

– TOTAL INCIDENT DURATION is in seconds so this value was converted to hours
and rounded to two decimal places. From here, the data was categorized in
to seven categories: <=15min, 15min-30min, 30min-45min, 45min-1hr, 1-2hr,
2-3hr, and 3hr>. Records with null values were removed. This was 621
records which was .03%. The duration represents the time from the initial
incident date time to when the scene was cleared. The new feature is
INCIDENT LENGTH. The original feature was also kept in the converted float
format. Two outlier records were removed.

– ACTION TAKEN1 DESC value counts revealed that similar details that were
represented in INCIDENT TYPE DESC. Due to the complexity and the simplification
through categorization, this feature was dropped.

– Value counts on PROPERTY USE DESC revealed that the majority of values
are listed as undetermined so this feature was dropped.

– Value counts of ZIP CODE revealed an invalid zip code 99999. This was replaced
with the highest count zip code per respective borough. Null zip code rows
were dropped as there were only nine records. Zip codes are in five digit format.

– BOROUGH DESC was not altered and includes the five boroughs: 1 - Manhattan,
2 - Bronx, 3 - Staten Island, 4 - Brooklyn, 5 - Queens, however BOROUGH NUM
was added as a numerical feature.

Once complete, the data was exported as a clean csv, fdip clean.csv. The final
dataset contains 2,340,414 records with no null values and sixteen attributes.
Final attributes and data types are:

    – IM INCIDENT KEY: object
    – INCIDENT DATE TIME: datetime64[ns]
    – UNITS ONSCENE: int
    – UNITS CATEGORY: object
    – TOTAL INCIDENT DURATION: int
    - INCIDENT_LENGTH: object
    – ZIP CODE: object
    – BOROUGH DESC: object
    – BOROUGH NUM: int
    – INCIDENT CATEGORY: object
    – INCIDENT CATNUM: int
    – LEVEL CATEGORY: int
    – Day of week: object
    - DAY NUM: int
    - MONTH: int
    – Hour of day: int

Independent variables: 
ZIP CODE, BOROUGH DESC, BOROUGH NUM, Day of week, DAY NUM, Hour of day, Month

Dependent variables: 
UNITS ONSCENE, UNITS CATEGORY, TOTAL INCIDENT DURATION, INCIDENT LENGTH, 
INCIDENT CATEGORY, INCIDENT CATNUM, LEVEL CATEGORY

## Data Analysis
To evaluate the dataset, a univariate analysis was completed for each feature
followed by a bivariate or multivariate to determine relationships. Univariate
analysis consisted of value counts, bar charts of value counts, bar charts of 
relative frequency, and box plots. Bivariate and multivariate analysis consisted 
of scatterplots, crosstabs, lineplots, Pearson correlation, Chi-square, & 
Cramer’s V. The details can be viewed here on this Github within the Jupyter 
Notebooks.

– Analysis revealed that Brooklyn is the busiest BOROUGH DESC followed by
Manhattan. The ZIP CODE with the highest incident count is 10029, which
is in Manhattan [6]. The second largest incident count ZIP CODE is 10456,
which is in the Bronx [6]. The map demonstrates the incidents by
ZIP CODE.

– The highest LEVEL CATEGORY is one which accounts for 99.35% of the incidents.

– 49.69% of incidents occur between the 12:00 - 20:00 Hour of day which is
37.50% of the day, with the highest volume being between 17:00 - 18:00.
There is a gradual increase through the day that starts around the 05:00
hour and peaks between 17:00 - 18:00 then begins to decline, cycling back
through each day. When broken out per BOROUGH DESC, the peak time of
17:00 - 18:00 does not change.

– The two busiest Month are July & August. This is consistent across the
BOROUGH DESC. There is variation of order from there depending on the
BOROUGH DESC, but April & February are consistently the slowest Month.

– The busiest Day of week is Friday and the slowest is Sunday. This is consistent
across the BOROUGH DESC, but it does vary in between.

– One unit responding is the highest count for UNITS ONSCENE, which 61.63%
of incidents. It is consistent across the BOROUGH DESC, followed by two and
three UNITS ONSCENE, then varies from there. Manhattan has the largest
count of UNITS ONSCENE in a singular incident.

– Incidents are resolved in less than 30 minutes 80.23% of the time. The largest
TOTAL INCIDENT DURATION for singular incidents were in Brooklyn and the
Bronx.

– The most common INCIDENT CATEGORY is RESCUE & EMS followed by
FALSE ALARM FALSE CALL. This is consistent across BOROUGH DESC.

– Pearson correlation on numerical data indicates a correlation between the
LEVEL CATEGORY and UNITS ONSCENE. Since the counts for both the UNITS ONSCENE
and LEVEL CATEGORY were highest at one, this is not too insightful. There is
also a correlation between ZIP CODE and BOROUGH DESC which is a given.
There are also some other minor correlations between UNITS ONSCENE and
TOTAL INCIDENT DURATION which is further demonstrated in pair plots, scatter
plots, and crosstabs. LEVEL CATEGORY and TOTAL INCIDENT DURATION
also show a minor correlation. Since the LEVEL CATEGORY for level one was
99.35%, this is not too insightful either.

-Crosstabs of each bivariate combination possible did not reveal anything
that it not indicated above.

– Chi-square & Cramer’s V on categorical data revealed a moderate relationship
between INCIDENT CATEGORY and UNITS CATEGORY. Cramer’s V was .32.

In summary, lots of descriptive information was extracted, however there is only 
a weak or non existent relationship between the independent and dependent variables. 

## Implementing ML Algorithms
Algorithms were selected based on their usability and performance with categorical
and uncorrelated data. Random Forest, MLPClassifier (Multi-layer Perceptron
classifier), and SGDClassifier (Stochastic Gradient Descent) algorithms
were implemented to determine if there were any hidden relationships and to predict
INCIDENT CATEGORY, INCIDENT LENGTH, & UNITS CATEGORY using ZIP CODE, BOROUGH NUM, 
MONTH, Hour of day, & DAY NUM. The data was split into an 80:20, train:test split, 
making the training set 1,872,331 rows and the test set 468,083 rows. Initially, a 
MultiOutputClassifier was implemented on each algorithm since the goal was to predict 
three labels. This information can be viewed in ML Alg MultiOut.ipynb. The accuracy of 
each algorithm on multi output was very low so each algorithm was evaluated further for 
single output to examine the possibilities, if any.

Random Forest was evaluated for a single label first due to its ability to
extract feature importance. From this information, algorithms were further tailored to 
the top two target features, ZIP CODE and Hour of day. Each algorithm was implemented 
for each label individually, utilizing the top two target features. The same random 
state of 50 was used in each implementation. Accuracy, F1, precision, and recall were 
collected on the training set and summarized for evaluation. Since this is categorical 
data, certain other metrics are not available. The data is skewed for certain categories 
leading to the selection of the macro average for F1, precision, and recall vs weighted 
or micro. A display of the confusion matrix for each algorithm is available in addition 
to a classification report within the links provided below.

Details on the hyperparameters used for each algorithm are:

- Random Forest multi was implemented with a max depth of 6, otherwise
defaults were in place. Random Forest on a single label was further refined
to a max depth of 10 and n estimators of 150. Random Forest details
can be viewed in RandomForest.ipynb. Random Forest multi was revisited with max depth 
of 20 and n estimators of 200.

- MLP multi was implemented with default settings. MLP on a single label
was further refined to activation ’tanh’, solver ’adam’, alpha .05, and
early stopping equal to True. MLP details can be viewed here inMLPClassifier.ipynb.

- SGD multi was implemented with early stopping equal to True and loss
’modified huber’, otherwise defaults were in place. SGD on a single label was
further refined to loss ’log loss’, and early stopping equal to True. SGD details
can be viewed in SGDClassifier.ipynb.

The preliminary indication from implementations on the test data as outlined
above was that Random Forest was the best performer. Because of this, Random
Forest with multi-output was revisited with the two target features only
and refined hyperparameters as outlined above, with the intention of finding a
good fit. This is available in RandomForestMulti.ipynb. The increase in performance 
was negligible.

## Analysis of Results
In summary, as expected from the data analysis and exploration, no further
insights were gained and accuracy is low. Results are no better than a guess of
the top value counts, which is demonstrated in the confusion matrix for Random
Forest predicting UNITS CATEGORY using the top two features. The confusion
matrix demonstrates that the algorithm is ignoring all categories except the
top value count category of one. As revealed in the data analysis section, this
accounts for 61.63% of the information. This algorithm has an accuracy of 61.64%. 
It is simply matching by default. Since a good fit could not be found due to the 
skew of the categories, lack of correlation, and randomness of the data, test data 
implementation was abandoned, as a good fit could not be found on the training set. 

A summary of the results from all of the algorithms implemented
is provided in Results.ipynb. Precision is the percentage of predicted labels that 
matched to the true labels then divided by true and false positives. False positives 
and false negatives are not so clear in a multi classification problem. Values of the
precision to be used are diagonal across the matrix matching 0 to 0, 1 to 1, and
so on, then divided along the row which is true positives and the false positives.
The row percentages from this are 61.64%, 0%, 0%, 0%, 0%, 100.00%, and 0%.
Divided by the seven categories is the 23.09% indicated for precision. This is
the macro average. Macro averaging is the choice due to the skewed categories
and the decision to treat all categories the same vs weighting one higher than
another. Recall is the percentage of predicted labels that matched to the true
labels but instead of dividing along the row, it divides the column total, which
is inclusive of true positives and false negatives. The column percentages are
100.00%, 0%, 0%, 0%, 0%, 0%, and 0%. Divided by the seven categories is the
14.29% indicated for recall. F1 combines precision and recall to provide a better
metric than either alone. F1 scores per category are 76.27%, 0%, 0%, 0%, 0%,
0%, and 0%. Divided by the seven categories is the 10.89% indicated for F1.
Again, the best is a default match. This is evident in the results for other 
algorithms with other settings.

## Conclusion
After collecting, cleaning, and analyzing New York City Fire Department incident
information, three machine learning algorithms were used to predict future
incident types, duration, and units needed on scene. Feature importance was
extracted and hyperparameter tuning was applied in an effort to obtain a good
fit. Unfortunately, a good fit could not be found. The final determination is
that incidents at the fire department are too random to predict utilizing only
location, date, and time. Descriptive analytics outlined in the data analysis section
demonstrated basic patterns that can be used for staffing and equipment
needs, but further details such as the specific type and duration of an incident, or
the specific number of units needed, cannot be determined. Without additional
information, the incidents appear as random as a roll of dice.

- ### Future Work and Limitations
Future work in this area that would add value is the incorporation of outside
predictive factors for a more comprehensive prediction. Datasets that could potentially
add value pertain to crime, natural disaster, weather, census and traffic 
data. It is also noted that more information is collected by NFIRS than what
is represented in this dataset [8], which presents a limitation. The collection of
a full dataset from NFIRS would allow for more thorough examination. For example,
initially the property type was of interest but this field was often listed
as undetermined, so it was not of use and had to be dropped. Other potentially
useful information not always available was the presence of certain monitors and
equipment within a building. The available data was also broadly simplified for
project use and potentially could be predicted if detailed incident types were
examined individually and outside data was added. For example, if only vehicle
accidents were evaluated, and traffic data was added, the predictability is
likely to increase. However, evaluating incidents at that level of specificity is
time consuming which was also a limitation of this project as there is a wide
array of specific incident types to examine. It is also noted that the initial level
of specificity was not intended to be to that level of detail.

## References
[1] FDNY: Incidents responded to by fire companies, https://data.cityofnewyork.us/
Public-Safety/Incidents-Responded-to-by-Fire-Companies/tm6d-hbzd

[2] Kolesar, P., Walker, W.E.: An algorithm for the dynamic relocation of fire companies.
Operations research 22(2), 249–274 (1974)

[3] Mukhopadhyay, A., Vorobeychik, Y.: Prioritized allocation of emergency responders
based on a continuous-time incident prediction model. In: International Conference
on Autonomous Agents and MultiAgent Systems (2017)

[4] NFIC: National fire information council incident type cheat sheet, https://www.
nfic.org/docs/IncidentTypeCheatSheet.pdf

[5] Romero, T., Barnes, Z., Cipollone, F.: Predicting emergency incidents in san diego.
CS229. Stanford School of Engineering, Tech. Rep (2017)

[6] UnitedStatesZipCodes.org: Unitedstateszipcodes.org, https://www.
unitedstateszipcodes.org

[7] USFA: National fire incident reporting system, https://www.usfa.fema.gov/nfirs/

[8] USFA: National fire incident reporting system complete reference guide, https://
www.usfa.fema.gov/downloads/pdf/nfirs/NFIRS Complete Reference Guide 2015.
pdf