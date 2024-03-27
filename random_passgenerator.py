import itertools
import random
import string
def genarate_pass(lenght,start,used_passwords = []):
    
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"

    combination = itertools.product(uppercase_letters+lowercase_letters+digits, repeat=lenght)
    for i in list(combination)[start:]:
        pass_random = "".join(i)
        if pass_random not in used_passwords:
            used_passwords.append(pass_random)
            print(used_passwords)
            return pass_random
        else:
            continue

        

def random_passwords(length=10, pass_given = []):
    charcater = string.ascii_letters + string.digits
    
    print(pass_given)
    while True:
        random_s = "".join(random.choices(charcater, k=length))
        if random_s not in pass_given:
            pass_given.append(random_s)
            return random_s
        else:
            continue


print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())
print(random_passwords())






