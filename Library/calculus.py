class calculus:
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
            
        
            
            
                