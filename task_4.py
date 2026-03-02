from typing import List, Dict, Tuple


def input_error(func: Callable) -> Callable:
    """
    Decorator to handle common user input errors (KeyError, ValueError, IndexError).
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact not found."
    return inner


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Parses user input into a command and its arguments.
    """
    if not user_input.strip():
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Adds a new contact to the dictionary."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Changes the phone number of an existing contact."""
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Shows the phone number of the specified contact."""
    name = args[0]
    return f"{name}: {contacts[name]}"


def main() -> None:
    """
    Main entry point for the CLI assistant bot.
    """
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            if not contacts:
                print("Contacts list is empty.")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()