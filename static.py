class Shopping:
    cart =[] #class attribute #static attribute
    origin = 'cinna'

    def __init__(self,name,location) -> None:
        self.name = 'Jamu na city '
        self.location = 'Jam er maj kane'

    def purchase(self,item,price,amount):
        remaining = amount- price
        print(f'buying: {item} for price:{price} ad remaining :{remaining}')
    @classmethod
    def hudai_dekhi(self,item):
        print('Hudai dekhi kintu just ac er hawa khaute asche',item)

basundara = Shopping('Basu en dhara', 'not pppular location')
Shopping.hudai_dekhi("Jeans kinbo")