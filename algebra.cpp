/*
Takes in two points and finds the slope from the 
two points. In otherwords, it retunrs the slope of the interval between two points.

Returns the slope for a line based on the 2 points given.
*/
template <typename t> findSlope(t x1, t y1, t x1, t x2){
        t deltaY = y1 - y2;
        t deltaX = x1 - x2;
        
        return deltaX / deltaY
}
