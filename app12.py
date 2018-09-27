class CocaCola:
    formula = ['coffee', 'sugar', 'water', 'soda']

    def drink(self, how_much):
        if how_much == 'a sip':
            print('Cool-')
        elif how_much == 'whole bottle':
            print('Headache')


coke = CocaCola()
coke.drink('whole bottle')
