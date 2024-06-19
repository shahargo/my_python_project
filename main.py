import re
import random
import time

negation_pattern = re.compile(r"\b(no|not|never|don't)\b")
affirmation_pattern = re.compile(r"\b(yes|yeah|yep|sure)\b")
question_pattern = re.compile(r"^(What|When|Where|Why|Who|How|.*\?)")
repetition_pattern = re.compile(r"\b(yes it is|no it isn't)\b")
personal_statement_pattern = re.compile(r"\b(I am|I think|I'm)\b")
political_statement=re.compile(r"right|left|Bibi|Gantz")
keyword_patterns = {
    "never": re.compile(r"\bnever\b"),
    "impossible": re.compile(r"\bimpossible\b"),
    "always": re.compile(r"\balways\b")
}
responses = {
    "negation": [
        "Are you sure it's not just your perspective?",
        "What if the opposite is true?",
        "Maybe you should think about it in a different way?"]
    ,"affirmation": [
        "Is it really, or are we just agreeing to disagree?",
        "You seem quite certain. Why is that?",
        "Are you sure about that?"]
    ,"question": [
        "Good question, what do you think is the answer?",
        "Is understanding the same as agreeing?",
        "Why do you ask?",
        "Could you clarify your question?"]
    ,"repetition": [
        "No it isn't!",
        "Yes it is!",
        "This feels like déjà vu. Or is it just a spirited agreement?"]
    ,"personal_statement": [
        "What if it's just a different way of thinking?",
        "Why do you think that?",
        "Is that really your opinion?"]
    ,"political_statement":[
        "Politics is not good for your health!",
        "Only together will we win, don't you think"]
    ,"keyword": {
        "never": "Never say never!",
        "impossible": "Impossible? Isn't that a bit of an exaggeration?",
        "always": "Always? Isn't life full of exceptions?"
    }
}

def _user_input(user_input):
    if negation_pattern.search(user_input):
        return "negation"
    elif affirmation_pattern.search(user_input):
        return "affirmation"
    elif question_pattern.search(user_input):
        return "question"
    elif repetition_pattern.search(user_input):
        return "repetition"
    elif personal_statement_pattern.search(user_input):
        return "personal_statement"
    elif political_statement.search(user_input):
      return "political_statement"
    else:
        for keyword, pattern in keyword_patterns.items():
            if pattern.search(user_input):
                return "keyword", keyword
        return None


def generate_response(input_type, keyword=None):
    if input_type == "keyword" and keyword:
        return responses["keyword"][keyword]
    else:
        return random.choice(responses[input_type])

def sample_conversation():
    sample_inputs = [
        "I think this is silly.",
        "Yes, but it's still silly.",
        "Don't you understand?",
        "You always say that.",
        "No, that's wrong.",
        "Yes it is, yes it is!" ]

    for user_input in sample_inputs:
        print(f"User: {user_input}")
        input_type = _user_input(user_input)
        if isinstance(input_type, tuple):
            response = generate_response(input_type[0], input_type[1])
        elif input_type:
            response = generate_response(input_type)
        else:
            response = "I'm not sure how to respond to that."
        print(f"Clinic: {response}")


def argument_clinic():
    start_time = time.time()
    print("Welcome to the Python Argument Clinic!")
    duration = int(input("Enter the duration of the argument in seconds: "))
    print("\nHere is an example of conversation:")
    sample_conversation()
    print("\nYou can start the argument now. Type 'exit' to end the argument.")

    while (time.time() - start_time) < duration:
        user_input = input("User: ")

        if user_input.lower() == 'exit':
            print("Clinic: Ending the argument. Have a nice day!")
            break

        input_type = _user_input(user_input)
        if isinstance(input_type, tuple):
            response = generate_response(input_type[0], input_type[1])
        elif input_type:
            response = generate_response(input_type)
        else:
            response = "I'm not sure how to respond to that."

        print(f"Clinic: {response}")
    else:
        print("Clinic: Time's up! Thanks for the argument. Goodbye!")
argument_clinic()