import os

def path():
    global skript_dir
    skript_dir = os.path.dirname(os.path.abspath(__file__))
    print("Folder path:", skript_dir)

def has_more_than_16349_lines(file_path):
    with open(file_path, "r") as file:
        for i, _ in enumerate(file, start=1):
            if i > 16349:
                return True
    return False

def rename_files():
    i = 1000000
    max_index = 700
    for i in range(max_index, 0, -1):
        try:
            os.rename(skript_dir + f"/all_primes.{i}.csv", skript_dir + f"/all_primes.{i+1}.csv")
        except: pass

def split_file():
    with open(skript_dir + "/all_primes.1.csv", "wt") as file3: file3.write("All Primes\n")
    with open(skript_dir + "/all_primes.csv", "r") as file:
        with open(skript_dir + "/all_primes.1.csv", "a") as file2:
            for i, line in enumerate(file, start=1):
                if 2 <= i <= 16345:
                    file2.write(str(line))
        with open(skript_dir + "/all_primes.csv", "r") as src, open(skript_dir + "/all_primes.csv" + ".tmp", "w") as dst:
            dst.write(src.read())
        with open(skript_dir + "/all_primes.csv.tmp", "r") as src, open(skript_dir + "/all_primes.csv", "w") as dst:
            dst.write("All primes\n")
            for i, line in enumerate(src, start=1):
                if 16346 <= i:
                    dst.write(str(line))

def open_csv():
    while True:
        if has_more_than_16349_lines(skript_dir + "/all_primes.csv"):
            rename_files()
            split_file()
        else:
            print("File has not more 16348 lines!")
            print("finish!")
            break
        print("again")

if __name__ == '__main__':
    path()
    open_csv()
    input()