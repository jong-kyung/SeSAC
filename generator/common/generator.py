'''
추상 메소드는 구현이 없이 선언만 되어있는 메서드로,
추상 메소드는 자식클래스에서 반드시 구현해야 하기 때문에 추상 클래스를 통해 추상 메소드를 정의한다.
'''

from abc import ABC, abstractmethod

class Generator(ABC):
    @abstractmethod
    def generator(self):
        pass