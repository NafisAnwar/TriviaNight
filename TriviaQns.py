#Name: Nafis Anwar
#U-Number: U2092-0991
#Description: This is the second module of a trivia program that creates a list of trivia question objects

from Question import Question

def questionlist():

    question_prompts = [
    
        Question("How many days are in a lunar year?", "354", "365", "243", "379", 1),
        Question("What is the largest planet?", "Mars", "Jupiter", "Earth", "Pluto", 2),
        Question("What is the largest kind of whale?", "Orca whale", "Humpback whale", "Beluga whale", "Blue whale", 4),
        Question("Which dinosaur could fly?", "Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus", 3),
        Question("Which of these Winnie the Pooh characters is a donkey?", "Pooh", "Eeyore", "Piglet", "Kanga", 2),
        Question("What is the hottest planet?", "Mars", "Pluto", "Earth", "Venus", 4),
        Question("Which dinosaur had the largest brain compared to body size?", "Troodon", "Stegosaurus", "Ichthyosaurus", "Gigantoraptor", 1),
        Question("What is the largest type of penguins?", "Chinstrap penguins", "Macaroni penguins", "Emperor penguins", "White-flippered penguins", 3),
        Question("Which children's story character is a monkey?", "Winnie the Pooh", "Curious George", "Horton", "Goofy", 2),
        Question("How long is a year on Mars?", "550 Earth days", "498 Earth days", "126 Earth days", "687 Earth days", 4)
    
    ]

    return question_prompts

