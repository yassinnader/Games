class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}"
    
class UserMangment:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        if user.email in self.users:
            print(f"User with email {user.email} already exists.")
        else:
            self.users[user.email] = user
            print(f"User {user.name} added.")

    def search_user(self, email):
        return self.users.get(email, "User not found")
    
    def delete_user(self, email):
        if email in self.users:
            del self.users[email]
            print(f"User with email {email} delete.")
        else:
            print("User not found.")
        
    def display_users(self):
        if not self.users:
            print("No users available.")
        else:
            for user in  self.users.values():
                print(user)

if __name__  == "__main__":
    user_manger =    UserMangment()
    user1 =  User("Nero", "nero@example.com", "password123")
    user2 =  User("Kodo", "kodo@example.com", "password456")

    user_manger.add_user(user1)
    user_manger.add_user(user2)

    print(user_manger.search_user("nero@example.com"))

    user_manger.display_users()
    user_manger.delete_user("nero@example.com")

