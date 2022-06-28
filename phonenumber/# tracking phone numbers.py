# tracking phone numbers
import phonenumbers

from phonenumbers import carrier, geocoder, timezone
from phonenumbers.phonenumberutil import number_type

# mobileNo = phonenumbers.parse(input("Enter the phone number with country code"))
num = input("Enter the number you want to track: ")
phone = phonenumbers.parse(num)
time = timezone.time_zones_for_number(phone)
service = carrier.name_for_number(phone, "en")
registration = geocoder.description_for_number(phone, "en")

print(phone)
print(time)
print("Service Provider: ", service)  # doesn't work
print("Country is ", registration)
# print(timezone.time_zones_for_number(mobileNo))
# print(carrier.name_for_number(mobileNo, "en"))
# print(geocoder.description_for_number(mobileNo, "en"))
# print("valid mobile no: ", phonenumbers.is_valid_number(mobileNo))
# print("checking possibility of number: ", phonenumbers.is_possible_number(mobileNo))
