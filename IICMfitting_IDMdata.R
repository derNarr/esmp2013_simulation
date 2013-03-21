setwd("/Users/jwdegee/Desktop/ESMP2013/simulation/esmp2013_simulation/")
SJ3data <- read.csv("data.csv", header = F)

#SOA <- seq(-350,350,50) #15 valori di auditory delay
#length(SOA)

SJ3data <- rbind(seq(-350,350,700/(dim(SJ3data)[2]-1)),SJ3data)
SJ3data <- as.matrix(SJ3data)


#SJ3data <- rbind(seq(-350, 350, 50), 
#           c(98,82,73,76,80,48,20,12, 6, 1, 1, 0, 0, 2, 0),
#           c( 0, 1, 2, 4, 7,35,69,73,91,79,59,21, 7, 6, 5),
#           c(12, 7, 5,10,13, 7, 1, 5, 3,10,50,89,93,72,85))

package(FitTimingJudgments)

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
fit_SJ3(SJ3data, LamBounds=LamBounds, TauBounds=TauBounds, DeltaBounds=DeltaBounds,
        LamTStart=LamTStart, LamRStart=LamRStart, TauStart=TauStart, 
	  DeltaStart=DeltaStart, ErrStart=ErrStart, BiasStart=BiasStart,
        Model, Plot, Disp)


	