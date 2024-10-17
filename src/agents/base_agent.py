from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    def process(self, input_data):
        """
        Process the input data and return the result.
        """
        pass

    @abstractmethod
    def get_status(self):
        """
        Return the current status of the agent.
        """
        pass