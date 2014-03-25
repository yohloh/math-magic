class Math{
  template <typename t> add(a, b){
    return a + b;
  }
  
  template <typename t> subract(a, b){
    return a - b;
  }
  
  template <typename t> divide(a, b){
    return a / b;
  }
  
  template <typename t> multiply(a, b){
    return a * b;
  }
  
  template <typename t> exponent(a, n){
    t value = 0;
    for(int i = 0; i < n; i++){
      value *= a;
    }
  }
  
  template<typename t>
 double GetMean(vector <t>numbers){
	t sum = 0;
	for(int i = 0; i<numbers.size(); i++){
	 sum += numbers[i];
	}
	return sum/numbers.size();
  }
}
