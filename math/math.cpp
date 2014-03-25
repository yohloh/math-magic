#include <vector>
using namespace std;
class Math{
  template <typename t> add(t a, t b){
    return a + b;
  }
  
  template <typename t> subract(t a, t b){
    return a - b;
  }
  
  template <typename t> divide(t a, t b){
    return a / b;
  }
  
  template <typename t> multiply(t a, t b){
    return a * b;
  }
  
  template <typename t> exponent(t a, t n){
    t value = 0;
    for(int i = 0; i < n; i++){
      value *= a;
    }
  }
 
 /*
 Takes in a vector of numbers and finds the mean.
 
 Input: A vector of numbers
 
 Returns: The mean of the numbers (no decimals if not floating point)
 */
 template<typename t>
 double getMean(vector <t>numbers){
	t sum = 0;
	vector<t>::iterator numberIterator
	for(vector<t>::iterator numberIterator = numbers.begin(); numberIterator < numbers.end(); numberIterator++){
	 sum += *numberIterator
	}
	return sum/numbers.size();
  }
}
