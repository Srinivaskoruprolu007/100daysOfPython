class User:
    # Initialize the User class with user_id, username, and set followers/following to 0
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Method to follow another user
    def follow(self, user):
        user.followers += 1  # Increment the followers count of the other user
        self.following += 1  # Increment the following count of the current user


# Create two user instances
user_1 = User("001", 'srinivas')
user_2 = User("002", "vasu")

# User 2 follows User 1
user_2.follow(user_1)

# Print the following count of User 2
print(user_2.following)  # Output: 1

# Print the username of User 1
print(user_1.username)  # Output: srinivas
