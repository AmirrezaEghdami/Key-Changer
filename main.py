CHANGEABLE_KEYS = []
REPLACED_KEYS = []

# inputs
while True:
    changeable_key_ = input("Enter key you want to change: ")
    if changeable_key_ == "DONE":
        break
    replaced_key_ = input("Enter the key you want to replace with: ")

    CHANGEABLE_KEYS.append(changeable_key_)
    REPLACED_KEYS.append(replaced_key_)
