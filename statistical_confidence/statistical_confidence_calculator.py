import math

#Normal approximation is useful for determining confidence interval where  probability of event is not close to 0 or 1
# events = number of successes or failures in trials
# num_trials = total number of trials performed
# probit = probability unit function. For confidence interval of 95% allowable error rate is 5%, probit (z) = 1.96
    #other values: 90%=1.645, 98%=2.327, 99%=2.576
# Returns: rate that should be representative of 95% (or alternative confidence interval) of trial population ran in the same manner 
    #e.g. returning '0.53' means that within 95% of samples, the failure (or success) rate will be 53%.
        #"There is a 95% chance that a sample will be representative of a 53% success rate"
def normal_approximation(events, num_trials, probit=1.96):
    events = int(events)
    num_trials = int(num_trials)
    sample_statistic = events/num_trials
    standard_error=  math.sqrt((sample_statistic*(1-sample_statistic))/num_trials)
    probability = sample_statistic + probit * standard_error
    print(probability)
    return probability


if __name__ == '__main__':
    failures = input("Num Events:")
    trials = input ("Trials:")
    normal_approximation(failures, trials)