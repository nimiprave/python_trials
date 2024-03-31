#Implementing the iterators for an object. 

#Iterators on strings
name = "Nirmal Pothuraj"
for i in name:
    print(i)


#Using iterators
#stringIterator = iter(name)
#for i in range(55):
#    print(next(stringIterator))




 #Implementing Iterators in the class:

class MyNumbers:
    def __iter__(self):   
        self.a = 0
        return self
    
    def __next__(self):
        if self.a <= 20:
            self.a = self.a + 1
            return self.a
        else:
            raise StopIteration
iterator_object = iter(MyNumbers())
#print(next(iterator_object))

for x in iterator_object:
    print(x)