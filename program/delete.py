


def del_items(type_param='even' ):
    """
    Выбирается тип элементов для удаления.

    Можно выбрать 'even' - удалятся четные;
    иначе не четные. По умолчанию стоит 'even'.
    """
    def delete(list_items):
        """
        Функция удалет некоторые элементы массива в зависимости от type_param.

        Type_param задается во внешней функции.
        """
        match type_param:
            case 'even':
                return list(filter(lambda x: x % 2 != 0, list_items))
            case _:
                return list(filter(lambda x: x % 2 == 0, list_items))


    return delete