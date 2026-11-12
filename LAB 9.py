#task 2
class VacuumEnvironment:
    def __init__(self):
        self.rooms = {
            "A": "Dirty",
            "B": "Dirty"
        }
     
    def get_percept(self, location):
        return location, self.rooms[location]
     
    def execute_action(self, location, action):
        if action == "Suck":
            self.rooms[location] = "Clean"
        elif action == "Move Right":
            location = "B"
        elif action == "Move Left":
            location = "A"
        return location
     
    def display_environment(self):
        print("Environment State:", self.rooms)

    def count_dirty_rooms(self):
        """Returns the number of rooms that are currently Dirty."""
        return sum(1 for status in self.rooms.values() if status == "Dirty")

class SimpleReflexAgent:
    def __init__(self, location="A"):
        self.location = location
     
    def select_action(self, percept):
        location, status = percept
        if status == "Dirty":
            return "Suck"
        elif location == "A":
            return "Move Right"
        else:
            return "Move Left"

# Create objects
environment = VacuumEnvironment()
agent = SimpleReflexAgent("A")

# Run the agent with dirty room tracking
for step in range(6):
    percept = environment.get_percept(agent.location)
    action = agent.select_action(percept)
    
    print(f"\nStep {step + 1}")
    print("Percept:", percept)
    print("Selected Action:", action)
    
    agent.location = environment.execute_action(agent.location, action)
    
    environment.display_environment()
    print("Agent Location:", agent.location)
    print("Dirty Rooms Count:", environment.count_dirty_rooms())

   
   
 #task 3

class VacuumEnvironment:
    def __init__(self):
        self.rooms = {
            "A": "Dirty",
            "B": "Dirty"
        }
     
    def get_percept(self, location):
        return location, self.rooms[location]
     
    def execute_action(self, location, action):
        if action == "Suck":
            self.rooms[location] = "Clean"
        elif action == "Move Right":
            location = "B"
        elif action == "Move Left":
            location = "A"
        return location
     
    def display_environment(self):
        print("Environment State:", self.rooms)

    def count_dirty_rooms(self):
        return sum(1 for status in self.rooms.values() if status == "Dirty")

class SimpleReflexAgent:
    def __init__(self, location="A"):
        self.location = location
     
    def select_action(self, percept):
        location, status = percept
        if status == "Dirty":
            return "Suck"
        elif location == "A":
            return "Move Right"
        else:
            return "Move Left"

# Create objects
environment = VacuumEnvironment()
agent = SimpleReflexAgent("A")

step = 0
# Run the agent until all rooms are clean
while environment.count_dirty_rooms() > 0:
    step += 1
    percept = environment.get_percept(agent.location)
    action = agent.select_action(percept)
    
    print(f"\nStep {step}")
    print("Percept:", percept)
    print("Selected Action:", action)
    
    agent.location = environment.execute_action(agent.location, action)
    
    environment.display_environment()
    print("Agent Location:", agent.location)

print("\nAll rooms are clean! Agent has stopped.")