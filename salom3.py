class Person:
    name='Ivan'
    age=42
    def set(self,name, age):
        self.name=name
        self.age=age
operation =input()
if operation== '+':
    vlad=Person()
    vlad.set('Vlad',25)
    print(vlad.name+' ' + str(vlad.age))
elif operation == '*':

    ivan=Person()
    ivan.set(input(),int(input()))
    print(ivan.name, ivan.age )
print()
