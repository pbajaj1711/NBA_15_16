dat_teams = read.csv("teams.csv", header=TRUE, sep=",")
num_teams = dim(dat_teams)[1]

c1 <- rainbow(10)
c2 <- rainbow(10, alpha=0.2)
c3 <- rainbow(10, v=0.7)

for(i in 1:num_teams){
  team = as.character(dat_teams[i,1])
  file_name = paste(team,"_15_16.csv", sep="")
  dat_team = read.csv(file_name, header = TRUE, sep=",")
  pdf(paste("../ExploratoryAnalysis/BoxPlots/",team,"_15_16.pdf", sep=""))
  print (boxplot(dat_team[,2:5], col=c2, medcol=c3, whiskcol=c1, staplecol=c3, boxcol=c3, outcol=c3))
  dev.off()
}