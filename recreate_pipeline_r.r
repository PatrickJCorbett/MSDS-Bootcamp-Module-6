#load in tidyverse
library(tidyverse)

#Part 1: read in csv to a dataframe
andre  <- read_csv('andre.csv')

#Part 1.5: quick EDA on dataframe
dim(andre)
table(andre$Year)
#Part 2: remove data from 1976 and after 1993
andre_subset  <- andre %>%
    filter(Year > 1976 & Year < 1993)
#Part 3: make a histogram
andre_subset %>%
    ggplot(aes(x = H)) +
    geom_histogram(bins = 100) +
    ggtitle("Hits Histogram") +
    ggsave("andre_hits_histogram_r.png")