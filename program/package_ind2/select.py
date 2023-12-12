def select_routes(routes, name_punct):
    """
    Выбрать маршруты с заданным пунктом отправления или прибытия.
    """
    selected = []
    for route in routes:
        if route['начальный пункт'].lower() == name_punct \
                or route['конечный пункт'].lower() == name_punct:
            selected.append(route)

    return selected