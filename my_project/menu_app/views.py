from django.shortcuts import render

from my_project.menu_app.templatetags.menu_tags import draw_menu


def my_view(request):
    menu = draw_menu('main_menu') # здесь main_menu - название меню, которое вы хотите отрисовать
    context = {'menu': menu}
    return render(request, 'my_template.html', context)