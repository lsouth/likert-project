library(ggplot2)
library(readr)
library(latex2exp)

t_test <- read_csv("~/neu/courses/cs7290/likert-project/t-test.csv")

treatment_labels_students <- c("Control","Errors not centered at 0", "Non-constant variance in errors",
                               "Errors from logistic distribution","Dependent observations",
                               "Discretized data")

test_name = "Student T test"

make_plot <- function(test_data, test_name, labels, sample_size){
  ggplot(data=test_data[test_data$sample_size==sample_size,], aes(x=median,y=p_value, color=treatment)) + 
    geom_point() + geom_line() + geom_errorbar(aes(ymin=lower,ymax=upper,color=treatment,width=0.1)) + 
    ggtitle(TeX(paste("P-values from ", test_name, " (H_0: eta = 4) with sample size of ", sample_size))) +
    theme(plot.title = element_text(hjust = 0.5)) + geom_abline(intercept=0.05,slope=0,linetype="dashed")+
    scale_color_discrete(name="Treatment",labels=labels) +
    scale_y_continuous(name="P-value",limits = c(0,1)) + 
    scale_x_continuous(name=expression(eta))
}

make_treatment_plot <- function(test_data, test_name, sample_size, treatment){
  ggplot(data=test_data[test_data$sample_size==sample_size & test_data$treatment == treatment,], aes(x=median,y=p_value, color=treatment)) + 
    geom_point() + geom_line() + geom_errorbar(aes(ymin=lower,ymax=upper,color=treatment,width=0.1)) + 
    ggtitle(TeX(paste("P-values from ", test_name, " (H_0: eta = 4) with sample size of ", sample_size, " - ", treatment))) +
    theme(plot.title = element_text(hjust = 0.5)) + geom_abline(intercept=0.05,slope=0,linetype="dashed")+
    scale_color_discrete(name="Treatment",labels=labels) +
    scale_y_continuous(name="P-value",limits = c(0,1)) + 
    scale_x_continuous(name=expression(eta))
}

make_plot(t_test, test_name, treatment_labels_students, 30)
make_plot(t_test, test_name, treatment_labels_students, 100)
make_plot(t_test, test_name, treatment_labels_students, 500)

