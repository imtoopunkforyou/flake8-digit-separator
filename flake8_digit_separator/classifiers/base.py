from abc import ABC, abstractmethod


class BaseClassifier(ABC):
    @property
    @abstractmethod
    def token(self):
        ...

    @abstractmethod
    def classify(self):
        ...
