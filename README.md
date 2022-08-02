class CardValidation:

    def __init__(self):
        self.card_number = input("Enter card number: ")
        self.result = False
        self.start_digit = ['4', '5', '6']
        self.count = 0

    def is_valid(self):

        if (len(self.card_number) == 16 or
        (len(self.card_number) == 19 and
        self.card_number[4] == '-' and
        self.card_number[9] == '-' and
        self.card_number[14] == '-')):
            self.card_number = self.card_number.replace('-', "")

        
        
        if (len(self.card_number) == 16 and 
        self.card_number.isdigit() and 
        self.card_number[0] in self.start_digit):
            for i in range(len(self.card_number) - 1, 0, -1):
                j = i-1
                k = j-1
                m = k-1
                if (self.card_number[i] == self.card_number[j] and 
                self.card_number[j] == self.card_number[k] and 
                self.card_number[k] == self.card_number[m]):
                    self.count = 1
            
            if self.count == 0:
                self.result = True

        return self.result

card = CardValidation()
valid = card.is_valid()

if valid:
    print("Valid")
else:
    print("Invalid")
