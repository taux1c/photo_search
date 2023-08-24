import shutil
from pathlib import Path
from os import system, name
from hashlib import sha512 as ha

names_file = "./names.txt"
results_location = "."

def read_names():
    names = []
    file = Path(names_file)
    if file.exists():
        names = [x.strip() for x in file.open().readlines()]
    else:
        names = [x.strip() for x in input("Enter a comma separated list of names to search for: ").split(',')]
    return names

def find(name):
    name_location = Path(results_location,name)
    name_location.mkdir(exist_ok=True,parents=True)
    name_results_location = Path(name_location,'results.txt')
    first_name = name.split(' ')[0].strip()
    last_name = name.split(' ')[-1].strip()
    if name == "nt":
        print("This program doesn't work with windows!")
        quit()
    else:
        search = "locate -i {} | grep -i {} > \"{}\"".format(first_name,last_name,name_results_location)
    system(search)
    return name_location

def copy_files(location):
    files = []
    hashes = []
    target_location = Path(location,'files')
    target_location.mkdir(exist_ok=True,parents=True)
    files = [x.strip() for x in Path(location,'results.txt').open().readlines()]
    for file in files:
        f = Path(file)
        try:
            print("Hashing {}".format(f))
            if f.is_file():
                file_hash = ha(f.read_bytes()).hexdigest()
                if not file_hash in hashes:
                    print("Moving {}".format(f))
                    shutil.copy(f,target_location)
                    hashes.append(file_hash)
        except:
            raise

def main():
    names = read_names()
    for name in names:
        location = find(name)
        copy_files(location)



main()
