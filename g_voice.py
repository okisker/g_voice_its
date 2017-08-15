from googlevoice import Voice
from googlevoice.util import input
import sys

username, password = "gvoiceits@gmail.com", "$Yracus3"
voice = Voice()
voice.login(username, password)

phoneNumber = input('Number to send message to: ')
text = input('Message text: ')

voice.send_sms(phoneNumber, text)