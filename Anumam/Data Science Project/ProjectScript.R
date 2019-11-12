#Study of height versus weight
library(ggplot2)
library(reshape2)
library(plyr)


#First Load the data
ht_weight_df <- read.csv(file = "weight-height.csv")
# str is short for structure(). It reports what's in the data.frame
str(ht_weight_df)

#relation ship between height and weight
plot(x = ht_weight_df$Height, y = ht_weight_df$Weight)

#It really does look like there is a strong linear relationship. Execute an lm fit to see.

lm_ht_weight <- lm(Weight ~ Height, data = ht_weight_df)
summary(lm_ht_weight)

#How do height and weight depend on gender?

# Subset the full data.frame by genders
male_df <- subset(ht_weight_df, Gender == "Male")
female_df <- subset(ht_weight_df, Gender == "Female")
# Get the summary values of height

summary(male_df$Height)

summary(female_df$Height)

#Using plyr to do this all at once

ddply(ht_weight_df, .(Gender), function(df) summary(df$Height))

#Comparing the densities by gender
plot(density(male_df$Height))

plot(density(female_df$Height))


#Using ggplot2 to overlay plots

#The package ggplot2 has had a significant impact on visualization in statistics. It will change the way you work.

dens_by_gender <- ggplot(data = ht_weight_df, aes(x = Height, color = Gender)) + 
  geom_density()
dens_by_gender

#This makes it more clear. It looks like these are two normal distributions with different means. We can check a Q-Q plot.

qq_by_gender <- ggplot(data = ht_weight_df, aes(sample = Height)) + geom_point(stat = "qq") + 
  facet_wrap(~Gender)
qq_by_gender

#Relationship between height and weight by gender
ht_wt_pt_gender <- ggplot(data = ht_weight_df, aes(x = Height, y = Weight, color = Gender)) + 
  geom_point(alpha = 0.2)
ht_wt_pt_gender

#It looks like the lines should have the same slope. Let's turn back to statistics and compute the fits with a factor for gender.
lm_ht_wt_by_gender <- lm(Weight ~ Height * Gender, data = ht_weight_df)
summary(lm_ht_wt_by_gender)

data = ht_weight_df[sample(nrow(ht_weight_df)),]#reshufles the data
bound = floor(0.9 * nrow(data))
df_train = data[1:bound,]
df_test = data[(bound+1):nrow(data),]

regressor <- lm(Weight ~ Height, data = df_train)

#Predicting the test set results

y_pred = predict(regressor, newdata = df_test)


#Visualising the training set results
library(ggplot2)
ggplot() + 
  geom_point(aes(x = df_train$Height, y = df_train$Weight),
             colour = 'red') +
  geom_line(aes(x = df_test$Height, y = predict(regressor, newdata = df_test)),
            colour = 'blue') + 
  ggtitle('Height vs Weight(Training set)') +
  xlab('Height') +
  ylab('Weight')

#visualising the test set results

ggplot() + 
  geom_point(aes(x = df_train$Height, y = df_train$Weight),
             colour = 'red') +
  geom_line(aes(x = df_train$Height, y = predict(regressor, newdata = df_train)),
            colour = 'blue') + 
  ggtitle('Height vs Weight(Testing set)') +
  xlab('Height') +
  ylab('Weight')

ggplot() + 
  geom_point(aes(x = df_test$Height, y = df_test$Weight),
             colour = 'red') +
  geom_line(aes(x = df_test$Height, y = predict(regressor, newdata = df_test)),
            colour = 'blue') + 
  ggtitle('Height vs Weight(Testing set)') +
  xlab('Height') +
  ylab('Weight')

actuals_preds <- data.frame(cbind(actuals=df_train$Weight, predicteds=predict(regressor, newdata = df_test)))  
# make actuals_predicteds dataframe.
correlation_accuracy <- cor(actuals_preds)

head(actuals_preds)

# Min-Max Accuracy Calculation
min_max_accuracy <- mean(apply(actuals_preds, 1, min) / apply(actuals_preds, 1, max))  

# MAPE Calculation
mape <- mean(abs((actuals_preds$predicteds - actuals_preds$actuals))/actuals_preds$actuals)  

# install.packages('DMwR')

DMwR::regr.eval(actuals_preds$actuals, actuals_preds$predicteds)
