# Set working directory to desktop (Change to your own linking)
setwd("~/Desktop")

# Set Seed
seed <- 12345 
set.seed(seed)

### Scenario 1: Outlier is far from IQR ###

# Generate Random Star Values
cluster_0 <- rnorm(5, 15, 5)
cluster_1 <- rnorm(10, 50, 5)
cluster_2 <- rnorm(10, 60, 5)
cluster_3 <- rnorm(10, 70, 5)
cluster_4 <- rnorm(10, 75, 5)

x_values <- c(cluster_0, cluster_1, cluster_2, cluster_3, cluster_4)
y_values <- array(0, length(x_values))

simulated_data <- data.frame(
  x = x_values,
  y = y_values
)

# Remove Tukey Outliers
remove_tukey_outliers <- function(x, k) {
  q1 <- quantile(x, 0.25)
  q3 <- quantile(x, 0.75)
  iqr <- q3 - q1
  lower_bound <- q1 - k * iqr
  upper_bound <- q3 + k * iqr
  x <- x[x >= lower_bound & x <= upper_bound]
  return(x)
}

x_values_tukey <- remove_tukey_outliers(x_values, 1.5)
y_values_tukey <- array(0, length(x_values_tukey))

simulated_data_tukey <- data.frame(
  x = x_values_tukey,
  y = y_values_tukey
)

# Write data frame to CSV
write.csv(simulated_data, "simulated_data_far.csv", row.names = TRUE)
write.csv(simulated_data_tukey, "simulated_data_tukey_far.csv", row.names = TRUE)


### Scenario 2: Outlier is close to IQR ###
# Generate Random Star Values
cluster_0 <- rnorm(5, 30, 5)
cluster_1 <- rnorm(10, 50, 5)
cluster_2 <- rnorm(10, 60, 5)
cluster_3 <- rnorm(10, 70, 5)
cluster_4 <- rnorm(10, 75, 5)

x_values <- c(cluster_0, cluster_1, cluster_2, cluster_3, cluster_4)
y_values <- array(0, length(x_values))

simulated_data <- data.frame(
  x = x_values,
  y = y_values
)

# Remove Tukey Outliers
remove_tukey_outliers <- function(x, k) {
  q1 <- quantile(x, 0.25)
  q3 <- quantile(x, 0.75)
  iqr <- q3 - q1
  lower_bound <- q1 - k * iqr
  upper_bound <- q3 + k * iqr
  x <- x[x >= lower_bound & x <= upper_bound]
  return(x)
}

x_values_tukey <- remove_tukey_outliers(x_values, 1.5)
y_values_tukey <- array(0, length(x_values_tukey))

simulated_data_tukey <- data.frame(
  x = x_values_tukey,
  y = y_values_tukey
)

# Write data frame to CSV
write.csv(simulated_data, "simulated_data_close.csv", row.names = TRUE)
write.csv(simulated_data_tukey, "simulated_data_tukey_close.csv", row.names = TRUE)