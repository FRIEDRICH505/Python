from roles import Admin

my_user = Admin('john', 'doe', 'jdoe', 30, 'new york')
my_user.privileges.show_privileges()