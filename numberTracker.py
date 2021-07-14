''''
import phonenumbers
from phonenumbers import geocoder
phone_numbers1 = phonenumbers.parse("+919336355716")
phone_numbers2 = phonenumbers.parse("+4930901820")
phone_numbers3 = phonenumbers.parse("+13478439904")
print(geocoder.description_for_number(phone_numbers1, "en"))
print(geocoder.description_for_number(phone_numbers2, "en"))
print(geocoder.description_for_number(phone_numbers3, "en"))
'''

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

user_input = input('Enter Phone Number : ')

phone_numbers = phonenumbers.parse(user_input, "CH")
print('Country Name : ', geocoder.description_for_number(phone_numbers, "en"))

service_provider = phonenumbers.parse(user_input, "RO")
print('Service Provider : ', carrier.name_for_number(service_provider, "en"))