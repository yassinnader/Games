import tkinter as tk
from tkinter import simpledialog, messagebox

class Post:
    def __init__(self, content):
        self.content = content


class User:
    def __init__(self, username):
        self.username = username
        self.friends = []
        self.posts = []

    def add_friend(self, user):
        if user not in self.friends:
            self.friends.append(user)
            user.friends.append(self)

    def add_post(self, content):
        post = Post(content)
        self.posts.append(post)


# Static methods and shared data
users = []


def find_user(username):
    for user in users:
        if user.username == username:
            return user
    return None


class MiniSocialNetworkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Social Network")
        self.current_user = None

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.show_welcome_screen()

    def show_welcome_screen(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Welcome to Mini Social Network!", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.main_frame, text="Register", command=self.register).pack(pady=5)
        tk.Button(self.main_frame, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.main_frame, text="Exit", command=self.root.quit).pack(pady=5)

    def register(self):
        username = simpledialog.askstring("Register", "Enter a username:")
        if username:
            if find_user(username):
                messagebox.showerror("Error", "Username already exists!")
            else:
                new_user = User(username)
                users.append(new_user)
                messagebox.showinfo("Success", f"User {username} registered successfully!")

    def login(self):
        username = simpledialog.askstring("Login", "Enter your username:")
        if username:
            user = find_user(username)
            if user:
                self.current_user = user
                messagebox.showinfo("Welcome", f"Welcome back, {username}!")
                self.show_main_menu()
            else:
                messagebox.showerror("Error", "User not found.")

    def show_main_menu(self):
        self.clear_frame()

        tk.Label(self.main_frame, text=f"Welcome, {self.current_user.username}!", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.main_frame, text="Add Friend", command=self.add_friend).pack(pady=5)
        tk.Button(self.main_frame, text="Add Post", command=self.add_post).pack(pady=5)
        tk.Button(self.main_frame, text="Show My Posts", command=self.show_posts).pack(pady=5)
        tk.Button(self.main_frame, text="Show My Friends", command=self.show_friends).pack(pady=5)
        tk.Button(self.main_frame, text="Find Mutual Friends", command=self.find_mutual_friends).pack(pady=5)
        tk.Button(self.main_frame, text="Logout", command=self.logout).pack(pady=5)

    def add_friend(self):
        friend_username = simpledialog.askstring("Add Friend", "Enter friend's username:")
        if friend_username:
            friend = find_user(friend_username)
            if friend:
                self.current_user.add_friend(friend)
                messagebox.showinfo("Success", f"{friend_username} added as a friend!")
            else:
                messagebox.showerror("Error", "User not found.")

    def add_post(self):
        content = simpledialog.askstring("Add Post", "Enter your post:")
        if content:
            self.current_user.add_post(content)
            messagebox.showinfo("Success", "Post added!")

    def show_posts(self):
        posts = "\n".join([post.content for post in self.current_user.posts])
        if posts:
            messagebox.showinfo("My Posts", posts)
        else:
            messagebox.showinfo("My Posts", "No posts yet.")

    def show_friends(self):
        friends = "\n".join([friend.username for friend in self.current_user.friends])
        if friends:
            messagebox.showinfo("My Friends", friends)
        else:
            messagebox.showinfo("My Friends", "No friends yet.")

    def find_mutual_friends(self):
        friend_username = simpledialog.askstring("Find Mutual Friends", "Enter friend's username:")
        if friend_username:
            friend = find_user(friend_username)
            if friend:
                mutual = set(self.current_user.friends) & set(friend.friends)
                if mutual:
                    mutual_friends = "\n".join([u.username for u in mutual])
                    messagebox.showinfo("Mutual Friends", mutual_friends)
                else:
                    messagebox.showinfo("Mutual Friends", "No mutual friends found.")
            else:
                messagebox.showerror("Error", "User not found.")

    def logout(self):
        self.current_user = None
        self.show_welcome_screen()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniSocialNetworkApp(root)
    root.mainloop()