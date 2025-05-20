class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(user):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()  # Composition

# Create instance and use the privileges object
admin_user = Admin("John", "Smith", 40, "Chicago", "john@example.com")
admin_user.describe_user()
admin_user.privileges.show_privileges()
