import user_class as u

my_user = u.User("callum", "cally", "35", "UK")
sumny_user = u.User('sumny', 'soom sooms', '35', 'Cuba')

my_user.describe_user()
my_user.greet_user()

my_user.increment_login_attempts(10)
my_user.increment_login_attempts(20)
my_user.increment_login_attempts(30)
my_user.increment_login_attempts(40)

my_user.reset_login_attempts()

# sumny_user.describe_user()
# sumny_user.greet_user()

