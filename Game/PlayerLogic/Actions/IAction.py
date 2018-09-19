from abc import ABCMeta, abstractmethod

class IAction:
    __metaclass__ = ABCMeta

    @abstractmethod
    def legal(self, player, dealer): pass

    @abstractmethod
    def effect(self, player, dealer): pass