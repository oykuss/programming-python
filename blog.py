class User:
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return f"şu anda aktif {cls.active_users} user var."

    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        User.active_users += 1
    
    def fullname(self):
        return f"{self.firstname} {self.lastname}"


class Moderator(User):
    active_moderators = 0

    @classmethod
    def display_active_moderators(cls):
        return f"şu anda aktif {cls.active_moderators} moderator var."

    def __init__(self,firstname,lastname,age,community):
        super().__init__(firstname,lastname,age)
        self.community = community
        Moderator.active_moderators += 1


def main():
    print(User.display_active_users())
    print(Moderator.display_active_moderators())
    u = User("Sıla","Şahin",30)
    m = Moderator("Öykü","Şahin",25,"software")  



