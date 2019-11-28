library(ggplot2)
library(readr)
t_test <- read_csv("~/neu/courses/cs7290/likert-project/t-test.csv")

sample_size = 30
ggplot(data=t_test[t_test$sample_size==30,], aes(x=median,y=p_value, color=treatment)) + geom_point() + geom_line() +
  geom_errorbar(aes(ymin=lower,ymax=upper,color=treatment,width=0.1)) + 
  ggtitle(expression("P-values from Student's T test "~H["0"]~": "~eta~" = 4 with sample size of 30")) + 
  theme(plot.title = element_text(hjust = 0.5)) + ylim(0,1) + geom_abline(intercept=0.05,slope=0,linetype="dashed") +
  scale_color_discrete(name="Treatment",labels=c("Control","Errors not centered at 0", "Non-constant variance in errors",
                                       "Errors from logistic distribution","Dependent observations","Discretized data"))

ggplot(data=t_test[t_test$sample_size==100,], aes(x=median,y=p_value, color=treatment)) + geom_point() + geom_line() +
  geom_errorbar(aes(ymin=lower,ymax=upper,color=treatment,width=0.1)) + 
  ggtitle(expression("P-values from Student's T test ("~H["0"]~": "~eta~" = 4) with sample size of 30")) +
  theme(plot.title = element_text(hjust = 0.5)) + 
  ylim(0,1) + geom_abline(intercept=0.05,slope=0,linetype="dashed")+
  scale_color_discrete(name="Treatment",labels=c("Control","Errors not centered at 0", "Non-constant variance in errors",
                                                 "Errors from logistic distribution","Dependent observations","Discretized data"))

ggplot(data=t_test[t_test$sample_size==500,], aes(x=median,y=p_value, color=treatment)) + geom_point() + geom_line() +
  geom_errorbar(aes(ymin=lower,ymax=upper,color=treatment,width=0.1)) + 
  ggtitle(expression("P-values from Student's T test ("~H["0"]~": "~eta~" = 4) with sample size of 30")) +
  theme(plot.title = element_text(hjust = 0.5)) + 
  ylim(0,1) + geom_abline(intercept=0.05,slope=0,linetype="dashed")+
  scale_color_discrete(name="Treatment",labels=c("Control","Errors not centered at 0", "Non-constant variance in errors",
                                                 "Errors from logistic distribution","Dependent observations","Discretized data"))
