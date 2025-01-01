from embroidery_thread import emb_thread
from menus.utilities import user_input_options

QUIT_MENU_LETTER = 'Q'
QUIT_MENU_NAME = 'Back'
QUIT_MENU_CODE = -1000
UNCONFIRMED_MENU_CODE = -1001

def ask_question(introduction, choices, can_exit=True, confirm_action='', extra_options=None):
    print(introduction)

    if isinstance(choices, list):
        choices = {index + 1: value for index, value in enumerate(choices)}
    else:
        raise ValueError('choices must be a list or a dictionary')

    if extra_options:
        choices.update(extra_options)

    if can_exit:
        choices[QUIT_MENU_LETTER] = QUIT_MENU_NAME

    for key, value in choices.items():
        print(f'{key}. {value.title if isinstance(value, MenuAction) else value}')

    user_input = user_input_options(choices.keys())

    if user_input == 'Q':
        return QUIT_MENU_CODE

    if confirm_action:
        print(f'Are you sure you want to {confirm_action}? [Y/N]')
        user_confirmation = user_input_options(['Y', 'N'])

        if user_confirmation == 'N':
            return UNCONFIRMED_MENU_CODE

    return choices[user_input].action() if isinstance(choices[user_input], MenuAction) else user_input

class MenuAction:
    @property
    def title(self):
        return self._get_title()

    def _get_title(self):
        raise NotImplementedError

    def action(self):
        raise NotImplementedError

class ListThreads(MenuAction):
    def _get_title(self):
        return "List Threads"

    def action(self):
        brand_names = [brand['name'] for brand in emb_thread['brands']]
        brand_choice = ask_question(
            'What Thread list would you like to see?',
            brand_names,
        )

        # Variable is show_all-->it is assigned the value user_input == 'A' (boolean)
        show_all = brand_choice == 'A'
        if show_all:
            brand_listed = None
        else:
            brand_listed = emb_thread['brands'][brand_choice - 1]

        for thread in emb_thread['threads']:
            if show_all or thread['brand'] == brand_listed['id']:
                print(thread['name'])
