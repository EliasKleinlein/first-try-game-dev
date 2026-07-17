from terminal_ui import (
    show_research_menu,
    ask_research_choice,
    show_placeholder,
    show_invalid_input,
)


def open_research_menu():
    while True:
        show_research_menu()
        research_choice = ask_research_choice()

        if research_choice == "0":
            return

        if research_choice in ["1", "2", "3", "4", "5"]:
            show_placeholder("Dieser Forschungsbereich ist noch nicht implementiert.")
            continue

        show_invalid_input()