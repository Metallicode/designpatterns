#abstract component 
class TextComponent:
    def PrintText(self):pass


#concrete component 
class Text(TextComponent):
    def __init__(self, text):
        self._text = text
        
    def PrintText(self):
        return self._text



#decorators
#addes ++ to text
class TextDecoratorPlus(TextComponent):
    def __init__(self, textcomponent):
        self._textcomponent = textcomponent

    def PrintText(self):
        return f"++{self._textcomponent.PrintText()}++"


#Capital all the chars
class TextDecoratorCapital(TextComponent):
    def __init__(self, textcomponent):
        self._textcomponent = textcomponent

    def PrintText(self):
        return f"{self._textcomponent.PrintText().upper()}"


#reverse text direction
class TextDecoratorInvertor(TextComponent):
    def __init__(self, textcomponent):
        self._textcomponent = textcomponent

    def PrintText(self):
        return f"{self._textcomponent.PrintText()[::-1]}"


#XOR text
class TextDecoratorXOR(TextComponent):
    def __init__(self, textcomponent, key=3):
        self._textcomponent = textcomponent
        self._key = key

    def PrintText(self):
        text = self._textcomponent.PrintText()
        XORd = []
        for i in range(len(text)):
            XORd.append(chr(ord(text[i]) ^ self._key))
        return f"{''.join(XORd)}"





#Driver
if __name__ == "__main__":

    t = Text("hello this is text")
    print(t.PrintText())
    
    d01 = TextDecoratorPlus(t)
    d02 = TextDecoratorCapital(t)
    d03 = TextDecoratorInvertor(t)
    d04 = TextDecoratorXOR(t)
    
    print(d01.PrintText())
    print(d02.PrintText())
    print(d03.PrintText())
    print(d04.PrintText())

    
