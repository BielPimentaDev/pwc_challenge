
def street_address_handler(street):
    street_name = []
    street_number = []
    index = 0

    for letter in street:
        if(letter.isnumeric()):
            index = street.index(letter)
            break

        street_name.append(letter)
    
    for letter in street[index:]:
        street_number.append(letter)
    
    street_name = "".join(street_name)
    street_number = "".join(street_number)

    street_name = street_name.strip()
    street_number = street_number.strip()


    return [street_name,street_number]



street_names = ["Miritiba 339", "Babaçu 500", "Cambuí 804B", "Rio Branco 23", "Quirino dos Santos 23 b"]

for street in street_names:
    print(street_address_handler(street))