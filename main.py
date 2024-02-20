
def street_address_handler(street):
    street_address = street.split(" ")
    street_name = street_address[0]
    street_number = street_address[1]

    return [street_name, street_number]


street_names = ["Miritiba 339", "Babaçu 500", "Cambuí 804B"]

for street in street_names:
    print(street_address_handler(street))