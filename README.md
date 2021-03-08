# Stats Calculator

## Contributors
* [Jay Lakhani](https://github.com/jaylakhani14) 
* [Austin Lee](https://github.com/lustinaee) 
* Sidharth Vemuri 
* [Franklin Tan](https://github.com/fjt7)

## Outline
* Stats Calculator
    1. Properties
    2. Math Operations
        * Addition - Calls addition static method
        * Subtraction - Calls subtraction static method
        * Multiplication - Calls multiplication static method
        * Division - Calls division static method
        * Square - Calls square static method
        * Square Root - Calls square root static method
    3. Random Generator
        * listPick Methods
            * return random choice
            * use seed
            * use RandomGenerator.randNum to generate list
    4. Population Sampling Functions
        * randomSampling
        * confidenceInterval
        * marginOfError
        * cochranFormula
        * sampleSize
    5. Descriptive Statistics Functions
        

## Breakdown of Tasks
* Random Generator Function
    * Description: The random module uses the seed value as a base to generate a random number. if seed value is not present it takes system current time.
    * Tasks 
        * [x] without a seed between a range of two numbers 
        * [x] with a seed between a range of two numbers(integer and decimal
        * [x] generate a list of n random numbers
        * [x] selecting random item from list 
        * [x] setting a seed and randomly select 
        * [x] selecting n number of items from a list without a seed 
        * [x] selecting n number of items from a list with a seed
    * Use Functions (make sure to import the random module)
        * <code>.seed()</code>used to initialize the random number generator.
        * <code>.random()</code> for generating random floats
        * <code>.randint()</code> for generating random integers
        * <code>.randrange()</code> for generating random numbers within a range
        * <code>.choice()</code> for randomly selected element 
          
* Populating Sampling Functions
    * Description: Computing statistical functions using statistics module
    * Tasks 
        * [x] Simple random sampling
        * [x] Confidence Interval For a Sample 
        * [x] Margin of Error 
        * [x] Cochran’s Sample Size Formula 
        * [x] How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
    * Use functions
        * <code>.sample()</code> to choose sample/multiple items from a Python list, set, and dictionary.
        * <code>scipy.stats.t.interval()</code> to find the confidence interval of a sample statistic
                
* Descriptive Statistics Functions
    * Description: Creating functions for basic stats operations
        * [x] Mean
        * [x] Median
        * [x] Mode
        * [x] Variance
        * [x] Standard Deviation
        * [x] Z-Score
    * Use functions:
        * Use <code>import numpy</code> See example
            * <code>np.mean()</code>
            * <code>np.median()</code>
            * <code>np.mode()</code>
            * <code>np.var()</code>
            * <code>np.std()</code>
            * <code>.stats.zscore</code> Make sure to <code>from scipy import stats</code>
    

| To do | In progress |  Review  | Done | 
| ---  | ----------- |  ------- | ---- |
| example | example | example |  example | 
|  |  |  |  |
|  |  |  |  | 
|  |  |  |  |

<!-- Undordered List -->

## Resources
* https://pynative.com/python-random-sample/
* https://www.kite.com/python/answers/how-to-compute-the-confidence-interval-of-a-sample-statistic-in-python  
* https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html
* https://numpy.org/doc/stable/reference/generated/numpy.std.html
* https://numpy.org/doc/stable/reference/generated/numpy.var.html
