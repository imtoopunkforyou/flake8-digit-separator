from abc import ABC, abstractmethod


class NumberValidator(ABC):
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

    @property
    def re_expression(self):
        ...

        raise NotImplementedError

    @abstractmethod
    def validate(self):
        ...

    @property
    @abstractmethod
    def error_message(self):
        ...


class NumberValidatorsFactory(ABC):
    @property
    @abstractmethod
    def token(self):
        ...

    @abstractmethod
    def create_ordered_classifiers(self) -> tuple[NumberValidator, ...]:
        ...

