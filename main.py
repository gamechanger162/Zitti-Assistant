from zitti_assistant import ZittiAssistant

# Example usage
assistant = ZittiAssistant()

inputs = [
    "Hey. How are you?",
    "Clean my room.",
    "Fetch the newspaper.",
    "Clean my room.",
    "Read my shopping list.",
    "Fetch the newspaper.",
    "Add Bread to my shopping list.",
    "Add Eggs to my shopping list.",
    "Add Bread to my shopping list.",
    "Read my shopping list.",
    "How much is 5 + 2?",
    "How's the weather outside?"
]

for user_input in inputs:
    response = assistant.process_input(user_input)
    print(response)
