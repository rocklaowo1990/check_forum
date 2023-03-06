import data


def check_proce(history: list[data.ResaultRow], url_name: str):

    is_proce = False
    for s in history:

        list_url = [s.resault_1.name, s.resault_2.name, s.resault_3.name]
        is_proce = url_name != '' and url_name in list_url

        if is_proce:
            break

    return is_proce


def check_in(history: list[data.ResaultRow], row: data.Row):
    is_in = False

    for s in history:
        is_url_1 = row.url_1 == s.resault_1.url
        is_url_2 = row.url_2 == s.resault_2.url
        is_url_3 = row.url_3 == s.resault_3.url
        is_title = row.title == s.title
        is_nick = row.nick_name = s.nick_name

        if is_url_1 and is_url_2 and is_url_3 and is_title and is_nick:
            is_in = True
            break
    return is_in
