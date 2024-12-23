
install.packages('babynames')
install.packages('tidyverse')
library(mdsr)
library(tidyverse)
library(babynames)

BnDist <- make_babynames_dist()

BnDist2 <- BnDist %>% 
  filter(sex == "F") %>%
  mutate(numberofalive = count_thousands * alive_prob)

BnDist3 <- BnDist2 %>%
  group_by(name) %>%
  summarise(alivepeople = sum(numberofalive)) %>%
  arrange(desc(alivepeople)) %>%
  slice(1:25)
  
top25names <- as.vector(BnDist3$name)

BnDist4 <- BnDist2 %>% 
  filter(name %in% top25names) %>%
  group_by(name)
  

geom_

tapply(BnDist2$name, sum)
  
BnDist3 <- split(BnDist2, )
split(BnDist2$name)

