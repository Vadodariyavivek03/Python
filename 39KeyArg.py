# Function with keyword arguments
def greet_person(name, greeting="Hello", punctuation="!"):
    
    """
    Greet a person using the specified greeting and add punctuation.

    Parameters:
    - name: The name of the person.
    - greeting: The greeting message (default is "Hello").
    - punctuation: The punctuation to add at the end of the greeting (default is "!").

    Returns:
    - The formatted greeting.
    """
    return f"{greeting}, {name}{punctuation}"

# Example usage with keyword arguments
person_name = "Vivek"

# Using keyword arguments in any order, and omitting defaults
greeting_message = greet_person(name=person_name, punctuation="!!!")

# Display the result
print(greeting_message)
