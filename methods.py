def call():
    print('Calling someone i dont know')
    return 'call done'

class Phone:
    price: 12000
    color ="Blue"
    brand ="samsung"
    features= ['camera', 'speaker', 'hammer']

    def call():
        print("Calling one person")
    def call(self):
        print("Calling one person")

    def send_sms(phone,sms):
        text = f'sending SMS to: {phone} and message: {sms}' 
        return text
my_phone = Phone()
print(my_phone.features)
my_phone.call()
my_phone.send_sms(41423, 'I missed to')