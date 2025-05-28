import random

class Father:
    def __init__(self, blood_types):
        self.blood_types = self.validate_blood_types(blood_types)

    def validate_blood_types(self, blood_types):
        valid_blood_types = ["A", "B", "O", "AB"]
        if blood_types[0] not in valid_blood_types or blood_types[1] not in valid_blood_types:
            raise ValueError("Golongan darah tidak valid. Gunakan A, B, O, atau AB.")
        return blood_types

class Mother:
    def __init__(self, blood_types):
        self.blood_types = self.validate_blood_types(blood_types)

    def validate_blood_types(self, blood_types):
        valid_blood_types = ["A", "B", "O", "AB"]
        if blood_types[0] not in valid_blood_types or blood_types[1] not in valid_blood_types:
            raise ValueError("Golongan darah tidak valid. Gunakan A, B, O, atau AB.")
        return blood_types

class Child:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        father_allele = random.choice(self.father.blood_types)
        mother_allele = random.choice(self.mother.blood_types)
        return father_allele + mother_allele

def get_blood_types_input(prompt):
    while True:
        try:
            blood_types = input(prompt).upper()
            if len(blood_types) != 2:
                raise ValueError("Golongan darah harus terdiri dari 2 karakter.")
            return list(blood_types)
        except ValueError as e:
            print(f"Error: {e}")

father_blood_types = get_blood_types_input("Masukkan golongan darah ayah (contoh: ao): ")
mother_blood_types = get_blood_types_input("Masukkan golongan darah ibu (contoh: bo): ")

try:
    father = Father(father_blood_types)
    mother = Mother(mother_blood_types)
    child = Child(father, mother)
    print(f"Golongan darah anak: {child.blood_type}")
except ValueError as e:
    print(f"Error: {e}")
