# How to load the data into R from the csv file

fname <- "<Your Filename to the csv file here>"
d <- read.csv(fname, sep="\t")
colnames(d)
head(d)
nrow(d)