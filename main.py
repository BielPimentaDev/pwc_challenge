class StreetAddressGenerator:
    def __init__(self, street):
        self.street = street
        self.street_name = []
        self.street_number = []
        self.start()

    def start(self):
        if(self.is_street_name_exception()):
            self.handle_exception_case() 

        elif(self.street[0].isalpha()):
            self.start_with_letter_case()

        elif(self.street[0].isnumeric()):
            self.start_with_number_case()

        print(self.return_address())

    def start_with_number_case(self):
        for letter in self.street:
            if(letter.isalpha()):
                index = self.street.index(letter)
                break
            self.street_number.append(letter)
        
        for letter in self.street[index:]:
            self.street_name.append(letter)
  
    def start_with_letter_case(self):
        for letter in self.street:
            if(letter.isnumeric()):
                index = self.street.index(letter)
                break
            self.street_name.append(letter)        
        for letter in self.street[index:]:
            self.street_number.append(letter)

    def handle_exception_case(self):        
        splited_street = self.street.split()
        for split in splited_street:
            if (split.lower() == "no"):
                    street_No_index = splited_street.index(split)                
                    for item in splited_street[street_No_index:]:                    
                        self.street_number.append(item)
                        self.street_number.append(" ")
                    break
            self.street_name.append(split)
            self.street_name.append(" ")               

    def is_street_name_exception(self):
        splited_street = self.street.split()
        flag_calle = False
        flag_no = False

        for splited_word in splited_street:
            if 'no' == splited_word.lower():
                flag_no = True

            if 'calle' == splited_word.lower():
                flag_calle = True

        return flag_calle and flag_no

    def return_address(self):
        self.street_name = "".join(self.street_name)
        self.street_number = "".join(self.street_number)        
        return([self.street_name.strip().replace(",",""),self.street_number.strip().replace(",","")])
        
    

street_names = [
    "Miritiba 339",
    "Babaçu 500",
    "Cambuí 804B",
    "Rio Branco 23",
    "Quirino dos Santos 23 b",
    "4, Rue de la République",
    "100 Broadway Av",
    "Calle Sagasta, 26",
    "Calle 44 No 1991"
]

for street in street_names:
    StreetAddressGenerator(street)
