rm(list = ls())

install.packages("rpart")
install.packages("rpart.plot")
install.packages("rattle")
install.packages("caret", dependencies = "TRUE")

library(caret)
library(rattle)
library(rpart)
library(rpart.plot)

ebay.df <- read.csv("eBayAuctions.csv")
ebay.df <- ebay.df[ , -c(18,21,22)]
#Exluded Categories: Music.Movie.Game + Currency.US + EndDay.Week
#partition

set.seed(1)
train.index <- sample(c(1:dim(ebay.df)[1]), dim(ebay.df)[1]*0.6)

train.df <- ebay.df[train.index, ]
valid.df <- ebay.df[-train.index, ]

default.ct <- rpart(Competitive ~ ., data=train.df,
                    control = rpart.control(maxdepth = 6), method = "class")

summary(default.ct)

#Plotting

prp(default.ct, type = 5, extra = 101, clip.right.lab = FALSE,
    box.palette = "GnYlRd", leaf.round = 5, 
    branch = .3, varlen = -10, space = 0)

fancyRpartPlot(default.ct, type=5, space = 0, palettes = "YlGn")

rpart.rules(default.ct, cover = TRUE)

default.ct.pred.train <- predict(default.ct, train.df, type ="class")
default.ct.pred.valid <- predict(default.ct, valid.df, type ="class")

confusionMatrix(default.ct.pred.valid, as.factor(valid.df$Competitive))
accuracy(default.ct.pred.valid, valid.df$Competitive)

caret::confusionMatrix(default.ct.pred.valid, as.factor(valid.df$Competitive))




#To be extracted in the next model
#1,2,5,20
rm(list = ls())

ebay.df <- read.csv("eBayAuctions.csv")

ebay.df <- ebay.df[ , -c(2,3,6,22,23)]
set.seed(1)
train.index <- sample(c(1:dim(ebay.df)[1]), dim(ebay.df)[1]*0.6)

train.df <- ebay.df[train.index, ]
valid.df <- ebay.df[-train.index, ]

default.ct <- rpart(Competitive ~ ., data=train.df,
                    control = rpart.control(maxdepth = 6), method = "class")

summary(default.ct)

#Plotting

prp(default.ct, type = 5, extra = 101, clip.right.lab = FALSE,
    box.palette = "GnYlRd", leaf.round = 5, 
    branch = .3, varlen = -10, space = 0)

fancyRpartPlot(default.ct, type=5, space = 0, palettes = "YlGn")

rpart.rules(default.ct, cover = TRUE)

default.ct.pred.train <- predict(default.ct, train.df, type ="class")
default.ct.pred.valid <- predict(default.ct, valid.df, type ="class")

caret::confusionMatrix(default.ct.pred.valid, as.factor(valid.df$Competitive))
accuracy(default.ct.pred.valid, valid.df$Competitive)


#Random Forest Model

install.packages("randomForest")
library(randomForest)

rf <- randomForest(as.factor(Competitive) ~ ., data = train.df, ntree = 500,
                   mtry = 4, nodesize = 5, importance = TRUE)

summary(rf)
head(rf$votes,10)
plot(rf)
legend("top", colnames(rf$err.rate), cex = 0.8, fill=1:3)

varImpPlot(rf, type = 1)
rf.pred <- predict(rf, valid.df)
caret::confusionMatrix(rf.pred, as.factor(valid.df$Competitive))
















