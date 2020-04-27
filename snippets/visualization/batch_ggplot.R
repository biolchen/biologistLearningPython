# Original link: https://stackoverflow.com/questions/26034177/r-saving-multiple-ggplots-using-a-for-loop

# Plot separate ggplot figures in a loop.
library(ggplot2)

# Make list of variable names to loop over.
var_list = combn(names(iris)[1:3], 2, simplify=FALSE)
var_list
# Make plots.
plot_list = list()
for (i in 1:3) {
  p = ggplot(iris, aes_string(x=var_list[[i]][1], y=var_list[[i]][2])) +
    geom_point(size=3, aes(colour=Species))
  plot_list[[i]] = p
}

# Save plots to tiff. Makes a separate file for each plot.
for (i in 1:3) {
  file_name = paste("~/Downloads/iris_plot_", i, ".tiff", sep="")
  tiff(file_name)
  print(plot_list[[i]])
  dev.off()
}

# Another option: create pdf where each page is a separate plot.
pdf("~/Downloads/plots.pdf")
for (i in 1:3) {
  print(plot_list[[i]])
}
dev.off()
