class User:
    first_name: str
    last_name: str
    age: int
    hobbies: [str]
    followers: int
    following: int

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobbies = []
        self.followers = 0
        self.following = 0

    def add_hobby(self, hobby: str):
        self.hobbies.append(hobby)

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User('John', 'Smith', 34)
user1.add_hobby('playing video games')

user2 = User('Susan', 'Smith', 25)
user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
