import math

#Normal approximation is useful for determining confidence interval where  probability of event is not close to 0 or 1
# events = number of successes or failures in trials
# num_trials = total number of trials performed
# probit = probability unit function. For confidence interval of 95% allowable error rate is 5%, probit (z) = 1.96
    #other values: 90%=1.645, 98%=2.327, 99%=2.576
# Returns: high and low failure/success rate that 95% of trials should be bounded by (or alternative confidence interval) when ran in the same manner 
def normal_approximation(events, num_trials, probit=1.96):
    events = int(events)
    num_trials = int(num_trials)
    sample_statistic = events/num_trials
    standard_error=  math.sqrt((sample_statistic*(1-sample_statistic))/num_trials)
    probability_upper = sample_statistic + probit * standard_error
    probability_lower = sample_statistic - probit * standard_error
    print(str(probability_upper))
    print(str(probability_lower))

    return probability_upper, probability_lower


#Wilson approximation is useful for values close to 0 or 1, as you might see with radiation testing (handful of events for 1e11 trials)
# This uses a wilson approximation to give an upper and lower bound for a cross section range one can expect to see
# events = number upsets/ events observed over total fluence
# fluence = total particles seen per cm^2 (protons/ions per unit area)
# Returns: Upset cross section upper and lower bounds that 95%( or alt. conf. interval) of samples should fall between
    #Cross section is a measure of the probability that photons interact with matter by a particular process [errors/ion_fluence]
        #e.g. if a device has a 8.34e-11 cross section, and the device sees 1e11 fluence [particles/cm^2], the device will exhibit 8.34 events over that fluence
def wilson_appoximation(events, fluence, confidence = 0.95):
    z = get_probit(confidence)
    p = events/fluence
    nom=1/(1+z*z/fluence)*(p+z*z/(2*fluence))
    diff=z/(1+z*z/fluence)*math.sqrt((p*(1-p))/fluence+z*z/(4*fluence*fluence))
    lower=nom-diff
    upper=nom+diff

    print(str(upper))
    print(str(lower))
    return upper, lower

def get_probit(x):
    z = 0
    a = 0.147
    the_sign_of_x = 0

    if(0==x):
        the_sign_of_x = 0
    elif(x>0):
        the_sign_of_x = 1
    else:
        the_sign_of_x = -1

    if  x != 0: 
        ln_1minus_x_sqrd = math.log(1-x*x)
        ln_1minusxx_by_a = ln_1minus_x_sqrd / a
        ln_1minusxx_by_2 = ln_1minus_x_sqrd / 2
        ln_etc_by2_plus2 = ln_1minusxx_by_2 + (2/(math.pi* a))
        first_sqrt = math.sqrt((ln_etc_by2_plus2*ln_etc_by2_plus2)-ln_1minusxx_by_a)
        second_sqrt = math.sqrt(first_sqrt - ln_etc_by2_plus2)
        z = second_sqrt * the_sign_of_x
    else: #// x is zero
        z = 0
    z = math.sqrt(2)*z
    return z


if __name__ == '__main__':
    #failures = input("Num Events:")
    #trials = input ("Trials:")
    #normal_approximation(failures, trials)
    wilson_appoximation(14,1e11)