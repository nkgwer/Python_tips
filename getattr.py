class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


hoge_hogemi = Human('Hoge Hogemi', 16, 'F')

print(getattr(hoge_hogemi, 'name'))

setattr(hoge_hogemi, 'height', 200)

print(hoge_hogemi.height)