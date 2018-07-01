float func(int n, float time, float delay) {
  /* 
   Turn divide function into a periodic function
   by mapping a sin function with divide 
   */
  return divide(n, 1, 1, map(sin(time+delay), -1, 1, 0, 1));
}

float divide(int n, float xRange, float yRange, float j) {

  /*
  This function was discovered while playing around with GLSL editor in the BookOfShaders. I was
   trying to create a variable multistep function that is also periodic, this is the first half of it.
   int n : number of steps
   float xRange: max X
   float yRange: max Y
   float j: moving parameter (time, a, etc...)
   */

  float outputVal = 0;
  for (int i=0; i<n; i++) {
    float a = float(n);
    outputVal += (yRange/(a-1.))*smoothstep(xRange*i/a, xRange*i/a-0.5, j);
  }
  return map(outputVal,0,yRange,0,1);
}

float smoothstep(float edge0, float edge1, float x) {
  x = constrain((x - edge0) / (edge1 - edge0), 0.0f, 1.0f); 
  return x * x * (3 - 2 * x);
}
