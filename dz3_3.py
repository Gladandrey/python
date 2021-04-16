#3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
#>>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
#{
#    "И": ["Иван", "Илья"],
 #   "М": ["Мария"], "П": ["Петр"]

names = ["Иван", "Мария", "Петр", "Илья"]

names_dict_list = dict()

for name in names:
    first_letter = name[0].upper()
    names_dict_list[first_letter] = names_dict_list.setdefault(first_letter, []) + [name.capitalize()]

print(names_dict_list, sep='\n')
# {'И': ['Иван', 'Илья'], 'М': ['Мария'], 'П': ['Петр']}


def thesaurus(*names):
    set_names = {name.title() for name in names}
    first_letter = [name[0].upper() for name in set_names]
    result_dict = {k: list() for k in first_letter}

    for name in set_names:
        result_dict[name[0]].append(name)

    return result_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
# {'И': ['Иван', 'Илья'], 'П': ['Петр'], 'М': ['Мария']}

