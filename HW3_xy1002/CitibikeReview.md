# Citibike mini project review by fb55

## IDEA: the idea is fine

## Null and alternative hypotheses: 
are formulated fine and consistently with the idea. except for not clarifying the difinition of younger and older rider. At this stage things should be clear enough that I could run a similar experiment on my own.

## data wrangling:

very good! the data is rpocessed well and it supports the question.

add comments to the cells so one knows what they do: 

```
#converting trip duration to hours
df['tripduration'] = df['tripduration']/60
```

you are in a fine position for a test of proportions (chi sq)

