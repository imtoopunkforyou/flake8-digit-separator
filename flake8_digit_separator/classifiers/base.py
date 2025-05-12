from abc import ABC, abstractmethod


class NumberClassifier(ABC):
    @property
    @abstractmethod
    def type_name(self) -> str:
        ...

    @property
    @abstractmethod
    def token(self):
        ...

    @abstractmethod
    def check(self) -> bool:
        ...


class NumberClassifiersFactory(ABC):
    @property
    @abstractmethod
    def token(self):
        ...

    @abstractmethod
    def create_ordered_classifiers(self) -> tuple[NumberClassifier, ...]:
        ...
