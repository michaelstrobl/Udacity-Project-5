Project 5: Data Visualization with D3.js
==============
Survivors of the Titanic
==============
by: Michael Strobl, Nanodegree Data Analyst November Cohort
--------------

1. Dataset
--------------

The used Dataset: http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls

Description of the Dataset: http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3info.txt

First, the Dataset is converted to a CSV file with Excel. Second, the Dataset is converted to a new one with only the relevant Variables.

Used Python Code for Conversion: “Datasets/titanic_csv_changer.py”

Now the Dataset ("titanic1.csv") is reduced to:


Total Data Points: 1309

Variables:
- Passenger Class: Class of the Titanic Passengers. Possible Classes: 1,2,3. 1 is the most expensive, 3 is the cheapest.
- Status: Status of the Passenger: Survived or Perished
- Sex: female or male
- Age: <14, 14-30, 31-50, >51
- Embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)


2. Summary
--------------
Used Code: 'index_final.html'

The Titanic was the biggest passenger liner in the world and it sunk during its first ride where 1500 of 2200 passengers died. In the Data Visualization, you can see that certain parameters gave the passengers better chances of survival.
More People in Class 1 or Class 2 have survived than in Class 3 and people who embarked in Southampton than in the other two ports. Additionally, women and children (below age of 14) survived rather than men and older people.

3. Design
--------------
Used Code: 'index_final.html'

I used stacked Bar Charts for this Data Visualization. It allows to represent different groups on top of each other and it’s good for comparison. Additionally, I added the Data Labels inside each of the stacked bars. For example, the values of 123 and 200 inside the first bar of Chart 1: It means that 123 people of Class 1 survived while 200 people of Class 1 died.

Like the following plot, I use percentage-stacked bars for comparison and the absolute values are inside the Data Labels for an overview. If you want to know the percentage value, you can hover over the stacked bar. 

Plot: http://dimplejs.org/advanced_examples_viewer.html?id=advanced_bar_labels

Survivors are shown in a light blue, while perished people get a light red color. With two different colors, the stacked bars are easier to perceive, differ and understand. A low value of saturation is more natural and gentle for the human’s eye.

In the top right of each graph, you can see the legend which indicates the survival status of a group.

In plot 2, another dataset ("titanic_without_age.csv") is used where the Age "NA" values are removed.

In plot 3, another dataset ("titanic_without_embarked.csv") is used where the Embarked "NA" values are removed.

4. Feedback
--------------
The feedback is divided in R Plots and index1.html.

R Plots:
- Used Code: 'R Plots/plots.R'
- Visible in: 'R Plots/R Plots.pdf'

index1.html:
- Used Code: "index1.html"

Feedback 1:
R Plots:
- Colors are too bright
- No Title or Y-Axis labelled

index1.html:
- Embarked NA and Age NA values should be removed
- X-Axis in Plot 2 should be sorted
- Data Labels would be nice

Feedback 2:
R Plots:
- good plots for overview
- Colors should be changed

index1.html:
- please label the Axes
- without na values would be better

Feedback 3:
R Plots:
- no sharp resolution
- boring background of the plots

index1.html:
- i prefer the absolute plots
- colors make no sense when perished have the color blue (like hope) and survived ones have the color red (like death or danger)



5. Resources
--------------

http://www.perceptualedge.com/articles/visual_business_intelligence/rules_for_using_color.pdf

http://www.encyclopedia-titanica.org/children-on-titanic/

http://dimplejs.org/advanced_examples_viewer.html?id=advanced_bar_labels

http://stackoverflow.com/questions/18558045/dimple-js-add-data-labels-to-each-bar-of-the-bar-chart

https://en.wikipedia.org/wiki/Bar_chart

https://en.wikipedia.org/wiki/RMS_Titanic
