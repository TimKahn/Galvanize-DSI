#!/usr/bin/Rscript

data <- read.csv("snakes.csv",header=TRUE,sep=',')
attach(data)

## use factors where values are not quantitative
pop <- as.factor(pop)
region <- as.factor(region)
hab <- as.factor(hab)


print(summary(lm(formula = mass ~ svl)))