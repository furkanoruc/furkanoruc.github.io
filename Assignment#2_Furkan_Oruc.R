rm(list = ls())
library(forecast)

souvenir.data <- read.csv("SouvenirSales.csv")
#monthly sales

souvenir.ts <- ts(souvenir.data$Sales, 
                   start = c(1995, 1), end = c(2001, 12), freq = 12)

plot(souvenir.ts, xlab = "Time", ylab = "Sales (in 000s)")

#souvenir.lm <- tslm(souvenir.ts ~ trend + I(trend^2))

#partition data
train.ts <- window(souvenir.ts, start = c(1995, 1), end = c(2000, 12))
valid.ts <- window(souvenir.ts, start = c(2001, 1), 
                   end = c(2001, 12))
#lm-season
train.lm.season <- tslm(train.ts ~ trend + I(trend^2) + season)
summary(train.lm.season)

train.lm.season.trend.pred <- forecast(train.lm.season, h = 12, level = 0)
accuracy(train.lm.season.trend.pred, valid.ts)

#exponential + season
train.expo.season <- tslm(train.ts ~ trend + I(trend^2) + season, lambda = 0)
summary(train.expo.season)
train.expo.pred <- forecast(train.expo.season, h = 12, level = 0)
accuracy(train.expo.pred, valid.ts)

rainseriesforecasts2 <- forecast.HoltWinters(train.expo.season, h=8)

#hwin
nValid = 12
hwin <- ets(train.ts, model = "MAA")
summary(hwin)

hwin.pred <- forecast(hwin, h = nValid, level = 0)
accuracy(hwin.pred, valid.ts)











