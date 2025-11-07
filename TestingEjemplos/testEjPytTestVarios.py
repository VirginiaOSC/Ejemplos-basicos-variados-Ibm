from types import *
import pandas as pd
import numpy as np
from collections.abc import Iterable


assert 5 == 5
#assert 5 == 3

assert type(5) is int
#assert type(5) is not int

type(object).__name__
df = pd.DataFrame()
print(type(df) is pd.DataFrame)

type(df).__name__ == 'DataFRame'        #True Boolean 
type(df).__name__ is type([]).__name__  #False Boolean

assert(type(df).__name__ == 'DataFrame') # Success Example
#assert(type(df).__name__ is type([]).__name__) # Fail Example

iterable_item = [3,6,4,2,1]
isinstance(iterable_item, Iterable)
isinstance(5, Iterable)

assert isinstance(iterable_item, Iterable) # Success Example
#assert isinstance(3, Iterable) # Fail Example

class Test(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def test_all_class_arguments(self):
        print('Testing both of the class variables to see whether they are both strings!')
        for _ in [self.first_name, self.last_name]:
            assert isinstance(_, str)
            print('Passed all the tests!')
print('Primer yay ID previo a crear el objeto', id(object))
yay = Test('John', 'Doe') #success expample
print('Primer yay ID', id(yay))
yay.test_all_class_arguments()

'''Testing both of the class variables to
see whether they are both strings!'''
#yay = Test(5, 'Doe') #fail example
print('Segundo yay ID', id(yay))
yay.test_all_class_arguments()


#Ejemplo escribiendo declaraciones de afirmación
class Example():
    def __init__(self, id_, name):
        self._id = id_
        self.name = name

    def subtract(self):
        answer = 5 + 5
        return answer
    
    def test_lambda_function(self):
        assert(lambda x: x is LambdaType)

    def test_subtract_function(self):
        assert(self.subtract is LambdaType)

example_class = Example("123", 'James Phoenix')

example_class.test_lambda_function() #Success Example
example_class.test_subtract_function() #Fail Example