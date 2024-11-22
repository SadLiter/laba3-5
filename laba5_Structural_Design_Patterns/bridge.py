# Абстракция
class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return self.implementation.implementation_method()

# Реализация
class Implementation:
    def implementation_method(self):
        pass

class ConcreteImplementationA(Implementation):
    def implementation_method(self):
        return "Implementation A"

class ConcreteImplementationB(Implementation):
    def implementation_method(self):
        return "Implementation B"

# Пример использования
implementation_a = ConcreteImplementationA()
abstraction_a = Abstraction(implementation_a)
print(abstraction_a.operation())  # Implementation A

implementation_b = ConcreteImplementationB()
abstraction_b = Abstraction(implementation_b)
print(abstraction_b.operation())  # Implementation B
