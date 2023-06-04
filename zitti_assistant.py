import datetime

class ZittiAssistant:
    def __init__(self):
        self.last_cleaned_time = None
        self.last_fetched_time = None
        self.shopping_list = []

    def process_input(self, user_input):
        if user_input.startswith("Hey."):
            return "Hello, I am doing great."

        if user_input == "How's the weather outside?":
            return "It's pleasant outside. You should take a walk."

        if user_input.startswith("Clean my room"):
            return self.clean_room()

        if user_input == "Fetch the newspaper":
            return self.fetch_newspaper()

        if user_input.startswith("Add"):
            item = user_input.split("Add ", 1)[1].split(" to my shopping list")[0]
            return self.add_to_shopping_list(item)

        if user_input == "Read my shopping list":
            return self.read_shopping_list()

        return "Hmm.. I don't know that"

    def clean_room(self):
        current_time = datetime.datetime.now()
        if self.last_cleaned_time is not None and (current_time - self.last_cleaned_time).total_seconds() < 600:
            minutes_since_cleaned = (current_time - self.last_cleaned_time).total_seconds() // 60
            return f"The room was just cleaned {int(minutes_since_cleaned)} minute(s) ago. I hope it's not dirty"

        self.last_cleaned_time = current_time
        return f"Room is cleaned. It looks tidy now. Job completed at {current_time}"

    def fetch_newspaper(self):
        current_date = datetime.datetime.now().date()
        if self.last_fetched_time is not None and self.last_fetched_time.date() == current_date:
            return "I think you don't get another newspaper the same day"

        self.last_fetched_time = datetime.datetime.now()
        return "Here is your newspaper."

    def add_to_shopping_list(self, item):
        if item in self.shopping_list:
            return f"You already have {item} in your shopping list"

        self.shopping_list.append(item)
        return f"{item} added to your shopping list"

    def read_shopping_list(self):
        if not self.shopping_list:
            return "You have no items in your shopping list"

        return "Here is your shopping list. " + ", ".join(self.shopping_list)

def process_commands_from_file(file_path):
    assistant = ZittiAssistant()

    with open(file_path, 'r') as file:
        commands = file.readlines()

    for command in commands:
        command = command.strip()
        response = assistant.process_input(command)
        print(response)

def main():
    print("Welcome to Zitti - Your Personal Robotic Assistant!")
    print("Enter your instructions or questions (or 'exit' to quit):")

    assistant = ZittiAssistant()

    while True:
        user_input = input("> ")

        if user_input == "exit":
            break

        response = assistant.process_input(user_input)
        print(response)

if __name__ == "__main__":
    main()
