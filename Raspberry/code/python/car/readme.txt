1.py 


13,19号端口是所谓是使能端，21,22端口是in1,in2。
13和19端口必须是GPIO.OUT && GPIO.HIGH。这样电机才能工作。
21,22端口也就是in1,in2也必须是GPIO.OUT，in1为GPIO.HIGH时正转，in2为GPIO.HIGH时反转'


