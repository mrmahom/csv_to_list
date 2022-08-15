def file_parser(uploaded_file):
    if uploaded_file is not None:
        with open(uploaded_file, 'r', encoding='utf-8') as file:
            lst = []
            for i, lines in enumerate(file):
                line = lines.split(',')
                for item in line:
                    lst[i].append(item)
    return lst


def get_choices_list(lst):
    return lst[0]


def list_creator(choice, lst):
    choices_list = get_choices_list(lst)
    result = []
    for sub_lst in lst:
        result.append(sub_lst[choices_list.index(choice)])
    return result
