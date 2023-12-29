def format_name(first_name, last_name):
    """This is an example function for the documentation"""
    return str(first_name).title() + ' ' + str(last_name).title()


print(format_name('adam', 'lipok'))


def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"


print(my_function(25))
