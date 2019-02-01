import sys
import json

class Person(object):
    """Future Support for Class"""
    def __init__(self, attrs):
        self.attrs = attrs


class ObfuscationWorker(object):
    """Main worker that Obfuscation personal information. To"""
    def __init__(self):
        self.Obfuscation = dict()
        self.Obfuscation["Id"] = False
        self.Obfuscation["Name"] = True
        self.Obfuscation["Address"] = True
        self.Obfuscation["City"] = False
        self.Obfuscation["State"] = False
        self.Obfuscation["Zip"] = False
        self.Obfuscation["SSN"] = True
        self.Obfuscation["Location"] = True
        self.Obfuscation["Phone"] = True
        self.Obfuscation["Countrycode"] = False
        self.Obfuscation["DOB"] = True
        self.Obfuscation["Website"] = True
        self.Obfuscation["Company"] = True
        self.Obfuscation["Occupation"] = False
        self.Obfuscation["HeightCM"] = False
        self.Obfuscation["WeightKG"] = False
        self.Obfuscation["BloodType"] = False
        self.Obfuscation["Vehicle"] = False
        self.Obfuscation["Color"] = False

    def process(self, person):
        """Process all attributes defined in class. Should not be modify by inherit.""" 
        # for attr, value in person.attrs.items():
        for attr, value in person.items():
            # check method and value exist
            if self.Obfuscation.get(attr, False) and value:
                encoder = getattr(self, "do_"+attr)
                # person.attrs[attr] = encoder(value)
                person[attr] = encoder(value)

    def star_encoder(self, string, start, stop):
        """Encode string[start:stop] to ***""" 
        if stop > start:
            ret = string[:start] + '*' * (stop - start) + string[stop:]
            return ret
        else:
            return string
    
    def do_Name(self, string):
        sentiment = 2
        return self.star_encoder(string, sentiment+1, len(string)-sentiment)

    def do_Address(self, string):
        sentiment = 2
        return self.star_encoder(string, sentiment+1, len(string)-sentiment)

    
    def do_SSN(self, string):
        sentiment = 2
        return self.star_encoder(string, sentiment+1, len(string)-sentiment)

    def do_Location(self, string):
        splits = string.split(',')
        return len(splits[0]) * '*' + splits[1]

    def do_Phone(self, string):
        area_code_length = 3
        return self.star_encoder(string, area_code_length+1, len(string))
    
    def do_DOB(self, string):
        splits = string.split(',')
        return len(splits[0]) * '*' + splits[1]

    def do_Email(self, string):
        splits = string.split('@')
        return len(splits[0]) * '*' + splits[1]
        
    def do_Website(self, string):
        splits = string.split('.')
        return len(splits[0]) * '*' + splits[1]

    def do_Company(self, string):
        sentiment = 2
        return self.star_encoder(string, sentiment+1, len(string)-sentiment)

def load_data(path):
    # persons = []
    with open(path, encoding="utf-8") as f:
        datas = json.load(f)
    # for data in datas:
    #     persons.append(Person(data))
    # return persons
    return datas

def save_data(path, persons):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(persons, f)

if __name__ == "__main__":
    # Parse command line and detect errors
    try:
        _, source_path, dest_path = sys.argv
    except Exception as e:
        print("Error args", sys.argv)
        raise
    persons = load_data(source_path)
    worker = ObfuscationWorker()
    for person in persons:
        worker.process(person)
    save_data(dest_path, persons)