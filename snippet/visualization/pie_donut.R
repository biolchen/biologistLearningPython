# Original post: https://stackoverflow.com/questions/26748069/ggplot2-pie-and-donut-chart-on-same-plot/37015211

browsers <- structure(list(browser = structure(c(3L, 3L, 3L, 3L, 2L, 2L, 2L, 1L, 5L, 5L, 4L), 
  .Label = c("Chrome", "Firefox", "MSIE",
  "Opera", "Safari"), class = "factor"), version = structure(c(5L, 
  6L, 7L, 8L, 2L, 3L, 4L, 1L, 10L, 11L, 9L), .Label = c("Chrome 10.0", 
  "Firefox 3.5", "Firefox 3.6", "Firefox 4.0", "MSIE 6.0", "MSIE 7.0", 
  "MSIE 8.0", "MSIE 9.0", "Opera 11.x", "Safari 4.0", "Safari 5.0"), 
  class = "factor"), share = c(10.85, 7.35, 33.06, 2.81, 1.58, 
  13.12, 5.43, 9.91, 1.42, 4.55, 1.65), ymax = c(10.85, 18.2, 51.26, 
  54.07, 55.65, 68.77, 74.2, 84.11, 85.53, 90.08, 91.73), ymin = c(0, 
  10.85, 18.2, 51.26, 54.07, 55.65, 68.77, 74.2, 84.11, 85.53, 
  90.08)), .Names = c("browser", "version", "share", "ymax", "ymin"),
  row.names = c(NA, -11L), class = "data.frame")

browsers$total <- with(browsers, ave(share, browser, FUN = sum))

tbl <- with(browsers, table(browser)[order(unique(browser))])

cols <- c('cyan2','red','orange','green','dodgerblue2')
cols <- unlist(Map(rep, cols, tbl))

givemedonutsorgivemedeath <- function(file, width = 15, height = 11) {
  ## house keeping 
  if (missing(file)) file <- getwd()
  plot.new(); op <- par(no.readonly = TRUE); on.exit(par(op))
  pdf(file, width = width, height = height, bg = 'snow')
  ## useful values and colors to work with
  ## each group will have a specific color
  ## each subgroup will have a specific shade of that color
  nr <- nrow(browsers)
  width <- max(sqrt(browsers$share)) / 0.8
  tbl <- with(browsers, table(browser)[order(unique(browser))])
  cols <- c('cyan2','red','orange','green','dodgerblue2')
  cols <- unlist(Map(rep, cols, tbl))
  ## loop creates pie slices
  plot.new()
  par(omi = c(0.5,0.5,0.75,0.5), mai = c(0.1,0.1,0.1,0.1), las = 1)
  for (i in 1:nr) {
    par(new = TRUE)

    ## create color/shades
    rgb <- col2rgb(cols[i])
    f0 <- rep(NA, nr)
    f0[i] <- rgb(rgb[1], rgb[2], rgb[3], 190 / sequence(tbl)[i], maxColorValue = 255)

    ## stick labels on the outermost section
    lab <- with(browsers, sprintf('%s: %s', version, share))
    if (with(browsers, share[i] == max(share))) {
      lab0 <- lab
    } else lab0 <- NA

    ## plot the outside pie and shades of subgroups
    pie(browsers$share, border = NA, radius = 5 / width, col = f0, 
        labels = lab0, cex = 1.8)

    ## repeat above for the main groups
    par(new = TRUE)
    rgb <- col2rgb(cols[i])
    f0[i] <- rgb(rgb[1], rgb[2], rgb[3], maxColorValue = 255)

    pie(browsers$share, border = NA, radius = 4 / width, col = f0, labels = NA)
  }

  ## extra labels on graph

  ## center labels, guess and check?
  text(x = c(-.05, -.05, 0.15, .25, .3), y = c(.08, -.12, -.15, -.08, -.02), 
       labels = unique(browsers$browser), col = 'white', cex = 1.2)

  mtext('Browser market share, April 2011', side = 3, line = -1, adj = 0, 
        cex = 3.5, outer = TRUE)
  mtext('stackoverflow.com:::maryam', side = 3, line = -3.6, adj = 0,
        cex = 1.75, outer = TRUE, font = 3)
  mtext('/questions/26748069/ggplot2-pie-and-donut-chart-on-same-plot',
        side = 1, line = 0, adj = 1.0, cex = 1.2, outer = TRUE, font = 3)
  dev.off()
}

givemedonutsorgivemedeath('~/Downloads/donuts.pdf')