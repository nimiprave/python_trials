from abc import ABC, abstractmethod


class MyInterface(ABC):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class MyIntefaceImplementation(MyInterface):
    def method1(self):
        print("The First method is called")

    def method2(self, args):
        print(f"The Second is called with the arguments: {args}")


if __name__ == "__main__":
    impl = MyIntefaceImplementation()
    impl.method1()
    impl.method2("Hello World")
