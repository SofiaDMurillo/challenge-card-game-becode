# Create a class called SYMBOL (2 attributes: Color and Icon)
            # Icons: [♥, ♦, ♣, ♠] 

class Symbol:

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon


# Create a class called CARD that will inherit from Symbol and add attribute value
            # Values: ['A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K']

class Card(Symbol):
  
    def __init__(self, icon, value):          # This will initialize the Card class, with parameters from parent Symbol, plus value
        if icon in ["♥", "♦"]:
            color = "RED"
        else:
            color = "BLACK" 
        super().__init__(color, icon)                
        self.value = value                          

# test= Card("red", "♥", 5)
# print(test.color)
# print(test.icon)
# print(test.value)


