library(FitTimingJudgments)

setwd("/Users/jwdegee/Desktop/ESMP2013/simulation/esmp2013_simulation/")

SJ3data <- read.csv("sub3_data.csv", header = F)
pdf("sub3_fitted_model.pdf")

SJ3data <- rbind(seq(-350,350,700/(dim(SJ3data)[2]-1)),SJ3data)
SJ3data <- as.matrix(SJ3data)

#Paramter space settings
LamBounds <- c(1/200, 1/3) #da modificare c(1/200, 1/5)
TauBounds <- c(-Inf, Inf) 
DeltaBounds <- c(0, Inf) 
LamTStart <- c(1/70, 1/10) #da definire	2/3 valori evenly spaced
LamRStart <- c(1/70, 1/10) #			2/3 valori evenly spaced
TauStart <- c(-70, 70)
DeltaStart <- c(20, 150)
ErrStart <- c(0.05)
BiasStart <- c(0.5)

Model <- 1;
Plot <- TRUE
Disp <- TRUE
a <- fit_SJ3(SJ3data, LamBounds=LamBounds, TauBounds=TauBounds, DeltaBounds=DeltaBounds,
        LamTStart=LamTStart, LamRStart=LamRStart, TauStart=TauStart, 
	  DeltaStart=DeltaStart, ErrStart=ErrStart, BiasStart=BiasStart,
        Model, Plot, Disp)
        
dev.off()