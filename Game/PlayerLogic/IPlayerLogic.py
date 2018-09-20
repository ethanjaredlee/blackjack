from abc import ABCMeta, abstractmethod

class IPlayer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def chooseAction(self, hand, others): pass
    
    @abstractmethod
    def makeWager(self, remaining): pass