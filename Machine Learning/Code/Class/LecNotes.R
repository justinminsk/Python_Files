babies <-read.csv("http://math.mercyhurst.edu/~sousley/STAT_139/data/babies.csv", header=T)
# data on babies with 999's as NAs
plot(babies$gestdays)
# scatter plot of gestration days
hist(babies$gestdays)
# histogram plot of ''
plot(density(babies$gestdays), main= "Density of birth weight")
# smooth histogram of ''
boxplot(babies$gestdays)
# boxplot of ''
UGsbyState<-read.csv("http://math.mercyhurst.edu/~sousley/STAT_139/data/UGsbyState.csv", header = T)
# second set of data on undergrads
boxplot(UGsbyState$UGs)
# boxplot of UGS
hist(UGsbyState$UGs)
# histogram of UGs
boxplot(UGsbyState$UGpT)
# boxplot of UGs by the thousand
hist(UGsbyState$UGpT)
# histogram by the thousand 
attach(faithful)
hist(waiting)
# generic, defaults
hist(waiting,main = 'truncated x range', xlab= 'seconds', ylab= 'count', xlim= c(60,90))
# truncated histogram 
hist(waiting, main = 'Histogram with cex= 1.5', cex.axis= 1.5 )
# cexmagnifies the text size, 1 = 100%, 1.5 = 150% of normal size
plot(babies$med)
# scatter plot of education codes
hist(babies$med)
# bad for this type of catagorical data
barplot(babies$med)
# better for this type of data
bcounts<-table(babies$med)
barplot(bcounts)
# need counts to make the bar plot work
pie(bcounts, main = "Mother's education")
# pie chart still has problems
boxplot(babies[which(babies$gestday < 999), 'gestdays'])
# box plot taking out values less than 999
