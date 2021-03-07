# Stats Calculator

### Team Members
* Jay Lakhani 
* Austin Lee 
* Sidharth Vemuri 
* Franklin Tan

### Outline
* Stats Calculator
    * Properties
    * Operations
        * Addition
        * Subtraction
        * Multiplication
        * Division
        * Square
        * Square Root
    * Random Generator Function
    * Population Sampling Functions
    * Descriptive Statistics Functions

### Breakdown of Tasks
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
    * Description: Computing statistical functions using numpy
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

### Resources
* https://pynative.com/python-random-sample/
