import os
import math

counter = 1044283

def path():
    global skript_dir
    skript_dir = os.path.dirname(os.path.abspath(__file__))
    print("Folder path:", skript_dir)

def is_prime(num):
    for x in range(2,counter):
        if(num%x) == 0:
            return False
    return True

def is_prime_efficient(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for x in range(5, int(math.sqrt(num)) + 1, 2):
        if num % x == 0:
            return False
    return True

def start():
    global counter
    path()
    with open (skript_dir + "/all_primes.csv", "wt") as file:
        file.write("All Primes\n")
        with open(skript_dir + "/all_primes.csv", "a") as file:
            while True:
                if is_prime_efficient(counter) == True:
                    file.write(f"{counter}\n")
                    print(counter)
                counter += 1

if __name__ == '__main__':
    start()
