import abc


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def list(self):
        raise NotImplementedError

    # @abc.abstractmethod
    # def add(self, entity):
    #     raise NotImplementedError

    # @abc.abstractmethod
    # def get(self, identifier):
    #     raise NotImplementedError
    