from menus.common.menu import ListThreads, ask_question

exit_code = ask_question(
    """Welcome to the Threads menu.
    What would you like to do with the Threads menu?""",
    [
        ListThreads(),
    ],
    can_exit=False
)
