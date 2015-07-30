getwd()
setwd("/Users/Michael/Udacity/Project 5/Data Visualization/Final Project/R Sketches")

#Import GGPlot Libray
library(ggplot2)


#Read Data
titanic <- read.csv('titanic1.csv')

summary(titanic)

#Bar Chart Age
ggplot(aes(x=Age, fill = Status), data = titanic) + geom_bar() + 
  ggsave('Age.png')

#Bar Chart Passenger Class
ggplot(aes(x=Passenger.Class, fill = Status), data = titanic) + geom_bar() + 
  ggsave('Class.png')

#Bar Chart Sex
ggplot(aes(x=Sex, fill = Status), data = titanic) + geom_bar() + 
  ggsave('Sex.png')

#Bar Chart Embarked
ggplot(aes(x=Embarked, fill = Status), data = titanic) + geom_bar() +
  ggsave('Embarked.png')


