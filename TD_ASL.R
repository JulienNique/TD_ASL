## Exercise 1 ####
x <- seq(1,7,by = 1)
y <- c(6,4,2,1,3,6,10)
model <- lm(y ~ x)
coeff <- model$coefficients
d <- function(x){
  coeff[1] + x*coeff[2]
}
plot(x,y)
lines(x,d(x),col="green")