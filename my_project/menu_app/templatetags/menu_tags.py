from django import template

from my_project.menu_app.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    active_url = request.path_info

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    menu_tree = build_menu_tree(menu_items)

    for node in menu_tree:
        set_active_node(node, active_url)

    return {'menu_tree': menu_tree}