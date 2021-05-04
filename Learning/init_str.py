class Developer:
    def __init__(self, name, city, skill, rate, phone):
        self.name = name
        self.city = city
        self.skill = skill
        self.rate = rate
        self.phone = phone

    def __str__(self):
        return f"{self.name} {self.city} {self.skill} {self.rate} {self.phone}"


user = Developer('Vlad', 'Kyiv', 'Python', 1300, '+380631234570')
print(user)
