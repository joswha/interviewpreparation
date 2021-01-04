class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # sum = 0

        self.card_num = "".join(self.card_num.split())[::-1]

        try:
            vals = [int(i) for i in self.card_num]
        except:
            return False

        if len(vals) <= 1:
            return False
        

        for k, val in enumerate(vals):
            if k % 2 == 1:
                vals[k] *= 2
                if vals[k] > 9:
                    vals[k] -= 9

        return (sum(vals) % 10 == 0)


