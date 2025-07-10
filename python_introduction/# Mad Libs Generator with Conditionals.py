# Mad Libs Generator with Conditionals

print("Welcome to the Mad Libs Story Generator! 🎉")
print("Please answer the following prompts:\n")

# Collect user inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb ending in -ing: ")
object1 = input("Enter a random object: ")
weather = input("What's the weather like (sunny/rainy/snowy)? ")

# Conditional storyline branch
if weather.lower() == "sunny":
    weather_scene = "The sun was blazing, and everything shimmered with heat."
elif weather.lower() == "rainy":
    weather_scene = "Rain poured from the sky, turning the streets into rivers."
elif weather.lower() == "snowy":
    weather_scene = "Snow blanketed the ground, making everything look magical."
else:
    weather_scene = "The sky was strange, a mix of mystery and surprise."

# Build the story
story = f"""
One day, {name} was walking through the streets of {place} when suddenly, a wild {animal} appeared!
Feeling very {emotion}, {name} picked up a {object1} and started {verb}.

"{adjective.capitalize()} day, isn't it?" the {animal} said, surprisingly.

{weather_scene}
Despite it all, {name} couldn't stop smiling—it was one of those unforgettable days.
"""

# Print the final story
print("\n🌟 Your Mad Libs Story 🌟")
print(story)