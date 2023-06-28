class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

def hash_password(password):
    return sum(map(ord, password))

def register(users):
    username = input("username: ")
    password = input("password: ")
    if username in users:
        print("please choose another name.")
    else:
        users[username] = hash_password(password)
        print("registration successful.")

def login(users):
    username = input("username: ")
    password = input("password: ")
    if (username in users) and (users[username] == hash_password(password)):
        print("login successful.")
    else:
        print("login failed.")

if __name__ == "__main__":
    users = {}
    while True:
        action = input("register or login? (R/L). 0 (zero) for exit: ")
        if action.lower() == 'r':
            register(users)
        elif action.lower() == 'l':
            login(users)
        elif str(action) == '0':
            break
        else:
            print("I said R or L xD. Or you can exit by 0 (zero)")
            continue
