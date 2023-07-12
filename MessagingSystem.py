class MessagingService:  # Informal python interface
    def sendMessage(self):
        pass


class SMSMessagingService(MessagingService):
    def __init__(self, message, receiverNumber):
        self.message = message
        self.receiverNumber = receiverNumber

    def sendMessage(self):
        print("\"" + self.message + "\" is sent to the number - " + str(self.receiverNumber))


class EmailMessagingService(MessagingService):
    def __init__(self, message, receiverMail):
        self.message = message
        self.receiverMail = receiverMail

    def sendMessage(self):
        print("\"" + self.message + "\" is sent to the mail - " + self.receiverMail)


class WhatsAppMessagingService(MessagingService):
    def __init__(self, message, receiverNumber):
        self.message = message
        self.receiverNumber = receiverNumber

    def sendMessage(self):
        print("\"" + self.message + "\" is sent to the number - " + str(self.receiverNumber))


while True:
    try:
        messagingService = input("Press 'S' to send your message through SMS : \nPress 'E' to send your message through E-mail : \nPress 'W' to send your message through Whatsapp : \nPress '0' to exit the messaging service : ")
        if messagingService == '0':
            print("Session Ended.")
            break
        else:
            if messagingService == 'S':
                message = input("Enter the message to be sent : ")
                receiverNumber = int(input("Enter the recipient number : "))
                sms = SMSMessagingService(message, receiverNumber)
                sms.sendMessage()
            elif messagingService == 'E':
                message = input("Enter the message to be sent : ")
                receiverEmail = input("Enter the recipient mail : ")
                if len(receiverEmail.split('.')[-1]) >= 2 and '@' in receiverEmail and len(receiverEmail.split('@')[0]) > 0:
                    email = EmailMessagingService(message, receiverEmail)
                    email.sendMessage()
                else:
                    print("Invalid E-mail.")
            elif messagingService == 'W':
                message = input("Enter the message to be sent : ")
                receiverNumber = int(input("Enter the recipient number : "))
                whatsApp = WhatsAppMessagingService(message, receiverNumber)
                whatsApp.sendMessage()
            else:
                print("Invalid input.")
    except ValueError:
        print("This is not a number.")

