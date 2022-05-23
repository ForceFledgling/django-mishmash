import json

from django.utils.safestring import mark_safe

from .models import Category, Page


def get_wiki_categories_menu():
    """Получаем левый блок с категориями статей, для страницы со списком статей"""

    pages = Page.objects.all()
    categories = Category.objects.all()

    result = ''
    for category in categories:
        pages_by_category_count = pages.filter(category=category.id).count()
        action = "searchSocket.send(JSON.stringify({'message': ['filter_category', '" + str(category.id) + "']}));"
        result += f'<a type="submit" onclick="{action}">{category.name} ({pages_by_category_count})</a><br>'
    return result


def _get_all_pages_sorted_by_categories():
    '''
        Выводит страницы конкретной категории.
        На входе id катергрии (int).
        На выходе HTML-код со всеми записями в категории.
    '''
    categories = Category.objects.all()
    result = ''
    for category in categories:
        pages = Page.objects.filter(category=category.id)

        result += f'<h2>{category.name}</h2>'
        if len(pages) == 0:
            result += 'There are no entries in this category.<hr>'
        else:
            for page in pages:
                result += f'<a href="/wiki/{page.id}">{page.name}</a><br>'
            result += '<hr>'
    return result


def _get_pages_by_category(category_id: str) -> str:
    category_name = Category.objects.get(id=category_id).name
    pages = Page.objects.filter(category=category_id)
    result = f'<h2>{category_name}</h2>'
    if len(pages) == 0:
        result += 'There are no entries in this category.<hr>'
    else:
        for page in pages:
            result += f'<a href="/wiki/{page.id}">{page.name}</a><br>'
        result += '<hr>'
    return result


def _get_page_view_data(page_id: str) -> dict:
    page = Page.objects.get(id=page_id)
    content = page.content
    page_name = page.name

    data = {
        'app': f'{mark_safe(json.dumps("wiki"))}',
        'page': page,
        'page_id': page_id,
        'page_name': page_name,
        'content': content,
        }
    return data
