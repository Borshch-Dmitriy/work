class Pet:
    pets_list = []
    def __init__(self, name):
        self.name = name
        Pet.pets_list.append(self)


    @classmethod
    def first_pet(cls):
        if not cls.pets_list:
            return None
        return cls.pets_list[0]

    @classmethod
    def last_pet(cls):
        if not cls.pets_list:
            return None
        return cls.pets_list[-1]

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets_list)

    @classmethod
    def all_pets(cls):
        return [pet.name for pet in cls.pets_list]
