from agents.base_agent import BaseAgent
from utils.message import Message

class Orchestrator:
    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent):
        if isinstance(agent, BaseAgent):
            self.agents[name] = agent
        else:
            raise TypeError("Agent must be an instance of BaseAgent")

    def process_request(self, request):
        # This is a placeholder for the main processing logic
        pass

def main():
    orchestrator = Orchestrator()
    # Here we will register our agents once they are implemented
    
    while True:
        user_input = input("Enter your request (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        result = orchestrator.process_request(user_input)
        print(result)

if __name__ == "__main__":
    main()