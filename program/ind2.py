from package_ind2 import *
import bisect
import re
import sys


display_routes = display.display_routes
get_route = get.get_route
select_routes = select.select_routes


def main():
    """
    Главная функция программы.
    """
    routes = []
    while True:
        command = input(">>> ").lower()

        match command:
            case 'exit':
                break

            case 'add':
                route = get_route()
                if route not in routes:
                    bisect.insort(
                        routes, route, key=lambda item: item.get(
                            'номер маршрута'
                        )
                    )
                else:
                    print("Данный маршрут уже добавлен.")

            case 'list':
                display_routes(routes)

            case _ if (m := re.match(r'select (.+)', command)):
                name_punct = m.group(1)
                selected = select_routes(routes, name_punct)
                display_routes(selected)

            case 'help':
                print("Список команд:\n")
                print("add - добавить маршрут;")
                print("list - вывести список маршрутов;")
                print(
                    "select <название пункта> - запросить маршруты, которые начинаются\n"
                    "или заканчиваются в данном пункте;"
                )
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
