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
}
