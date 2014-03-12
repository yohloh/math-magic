class calculus:
        """
        Input:  1.A function that we want to find the deriviative from (calls from function)
                2.Starting interval on the x axis, and ending interval on the x axis where 
                where we want to integrate.
                3.Accuracy point denote how small we want rectangles to be
        Returns: Area of interval for a given function 'f'
        
        Assumes that the funtion is a valid function, and returns a number value when called
        , which is presumably the y value, where we input the x value.
        Start interval and end intervals are any real numbers.
        Accuracy point is a number > 0
        
        Integration works by taking the interval dividing it evenly by the amount
        rectangles we want. Then we do a simple loop and each 'step', will be
        the width of each rectangle, the height of each rectangle for a given
        'step' is calculated by calling the passed in function 'f'.
        """
        def integrate(f, startInterval = 0, endInterval=0, accuracyPoint = 1):
            steps = accuracyPoint * 100000
            graphIntervalDistance = abs(startInterval - endInterval)
            rectangleInterval = graphIntervalDistance / steps
            
            xAxisTracker = startInterval
            area = 0
            for i in range(steps):
                height = f(xAxisTracker)
                #rectangle widths are evenly divided by intervalDistance
                area += height * rectangleInterval
                xAxisTracker += rectangleInterval
                
            return area
            
        def limit(f, close=100):
            
        def derivative(f, x=0, y=0):
            
        def slopeOf(f):
            
        def checkSolution(functioin, x, y):
            
        
            
            
                