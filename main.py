import keyboard

CHANGEABLE_KEYS = []
REPLACED_KEYS = []

# inputs
while True:
    changeable_key_ = input("Enter key you want to change(Enter DONE to done): ")
    if changeable_key_ == "DONE":
        break
    replaced_key_ = input("Enter the key you want to replace with: ")

    CHANGEABLE_KEYS.append(changeable_key_)
    REPLACED_KEYS.append(replaced_key_)

# keyboard event when key is pressed
while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name in REPLACED_KEYS:
        keyboard.send(CHANGEABLE_KEYS[REPLACED_KEYS.index(event.name)])
