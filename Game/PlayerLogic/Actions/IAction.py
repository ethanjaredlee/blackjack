from abc import ABCMeta, abstractmethod

class IAction:
    __metaclass__ = ABCMeta

    @abstractmethod
    def legal(self, player, admin): pass

    @abstractmethod
    def effect(self, player, admin): pass

    @abstractmethod
    def actionName(self): pass