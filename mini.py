
class Post:
    def __init__(self, content):
        self.content = content


class User:
    def __init__(self, username):
        self.username = username
        self.friends = []
        self.posts = []

    def add_friend(self, user):  # Corrected method name to singular ("add_friend")
        if user not in self.friends:
            self.friends.append(user)
            user.friends.append(self)

    def add_post(self, content):  # Fixed the typo "contenet" -> "content"
        post = Post(content)
        self.posts.append(post)

    def show_posts(self):
        for post in self.posts:
            print(f"{self.username} posted: {post.content}")

    def show_friends(self):
        for friend in self.friends:
            print(friend.username)


# Static methods and shared data
users = []  # Moved `users` outside the class to avoid scope issues


def find_user(username):  # Defined it as a standalone function
    for user in users:
        if user.username == username:
            return user
    return None  # Fixed indentation and logic


def find_mutual_friends(user):
    print("--- Mutual Friends ---")
    if not user.friends:
        print("You have no friends.")
        return

    for friend in user.friends:
        mutual_friends = [mutual for mutual in friend.friends if mutual in user.friends]
        if mutual_friends:
            print(f"Mutual friends with {friend.username}: {', '.join([mf.username for mf in mutual_friends])}")
        else:
            print(f"No mutual friends with {friend.username}.")


def register():
    username = input("Enter a username: ")
    if find_user(username):
        print("Username already exists!")
    else:
        new_user = User(username)
        users.append(new_user)
        print(f"User {username} registered successfully!")


def login():
    username = input("Enter your username: ")
    user = find_user(username)
    if user:
        print(f"Welcome back, {username}!")
        return user
    else:
        print("User not found.")
        return None


def main_menu(user):
    while True:
        print("\n--- Main Menu ---")
        print("1. Add Friend")
        print("2. Add Post")
        print("3. Show My Posts")
        print("4. Show My Friends")
        print("5. Find Mutual Friends")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            friends_username = input("Enter friend's username: ")
            friend = find_user(friends_username)
            if friend:
                user.add_friend(friend)
                print(f"{friends_username} added as a friend!")
            else:
                print("User not found.")
        elif choice == "2":
            content = input("Enter your post: ")
            user.add_post(content)
            print("Post added!")
        elif choice == "3":
            user.show_posts()
        elif choice == "4":
            user.show_friends()
        elif choice == "5":
            find_mutual_friends(user)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def find_mutual_friends(user):
    friend_username = input("Enter friend's username to find mutual friends: ")
    friend = find_user(friend_username)
    if friend:
        mutual = set(user.friends) & set(friend.friends)
        if mutual:
            print("Mutual Friends:")
            for u in mutual:
                print(u.username)
        else:
            print("No mutual friends found.")
    else:
        print("User not found.")

def run():
    while True:
        print("\n--- Welcome to Mini Social Network ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                main_menu(user)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
run()