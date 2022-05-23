from typing import Union

from .wiki_services import _get_all_pages_sorted_by_categories, _get_pages_by_category


def wiki_ws_action(message: Union[str, list]) -> str:
    if isinstance(message, list) is True:
        action = message[0]
        if action == 'filter_category':
            if message[1] != 'clear':
                category_id = message[1]
                return _get_pages_by_category(category_id)
            else:
                return _get_all_pages_sorted_by_categories()
    else:
        # иначе это что то ввели в строку поиска
        # result = search(username, app, message)
        pass
