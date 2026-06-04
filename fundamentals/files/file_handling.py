import datetime
import fileinput
from pathlib import Path


def read_file()-> None:
    file = open("data_file.txt", 'r')
    print(file.read())
    file.close()

def write_file()-> None:
    file = open("data_file.txt", 'a')
    print(file.write('\nWelcome to Gen AI training'))
    file.close()

def write_with_date_time()-> None:
    f1 = open("data_file.txt", 'a')
    f1.write(f"\n{datetime.datetime.now()} - User logged in" )
    f1.write(f"\n{datetime.datetime.now()} - Perform some operation" )

    f1.write(f"\n{datetime.date.today()}- add changes")
    f1.close()

def write_file_with_use()-> None:
    print("=" * 20)
    with open("data_file.txt",'r') as infile:
        all_lines = infile.readlines()

    with open("data_file.txt",'w') as wfile:
            for line in all_lines:
                if line.find('Manoj') != -1:
                    print("line found! replacing....")
                    line = line.replace('Manoj', 'Manoj Kumar')
                wfile.write(line)


def update_file_in_place_with_best_approch() -> None:
    with fileinput.input("data_file.txt",inplace=True) as file3:
        for line in file3:
            if 'Manoj' in line:
                line = line.replace('Manoj','Manoj Kumar')
            print(line, end="")


def find_file(filename, search_path):
    results = list(Path(search_path).rglob(filename))

    if results:
        for file in results:
            print(f"File found: {file}")
    else:
        print(f"{filename} not found!")


if __name__=="__main__":
    read_file()
    write_file()
    write_with_date_time()
    write_file_with_use()
    update_file_in_place_with_best_approch()
    find_file('data_file.txt','/Users/manojkumar/Documents/repository/')