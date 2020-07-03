class Doctor(object):
    def __init__(self, unique_id="ID", first_name='FIRST_NAME', last_name='LAST_NAME',
                 qualification="MD", specialization="SPECIALIZATION"):
        self.id_str = unique_id
        self.first_name_str = first_name
        self.last_name_str = last_name
        self.qualification_str = qualification
        self.specialization_str = specialization

    def __str__(self):
        return "{}| {}| {}| {}| {}| {}|".format(self.id_str, self.first_name_str, self.last_name_str,
                                                self.qualification_str, self.specialization_str)


class Patient(object):
    def __init__(self, unique_id="ID", first_name='FIRST_NAME', last_name='LAST_NAME',
                 gender="SEX", age='AGE'):
        self.__id_str = unique_id
        self.__first_name_str = first_name
        self.__last_name_str = last_name
        self.__gender_str = gender
        self.__age_str = age

    def set_id(self, ID):
        self.__id_str = ID

    def get_id(self):
        return self.__id_str

    def set_first_name(self, first_name):
        self.__first_name_str = first_name

    def get_first_name(self):
        return self.__first_name_str

    def set_last_name(self, last_name):
        self.__last_name_str = last_name

    def get_last_name(self):
        return self.__last_name_str

    def set_gender(self, gender):
        self.__gender_str = gender

    def get_gender(self):
        return self.__gender_str

    def set_age(self, age):
        self.__age_str = age

    def get_age(self):
        return self.__age_str

    def __str__(self):
        return "{}| {}| {}| {}| {}".format(self.__id_str, self.__first_name_str, self.__last_name_str, self.__gender_str, self.__age_str)

sample_patient = Patient()
print(sample_patient)
diabetes_patient = Patient()
diabetes_patient.set_first_name("Mumuni")
diabetes_patient.set_gender("M")
print(diabetes_patient)