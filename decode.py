def get_choices_list(df):
    return df.columns.values.tolist()


def get_file_name():
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")  # YYYY-mm-dd_HH-MM-SS
    return f"ID_list_{dt_string}"


def get_id_list(choice, df):
    lst = df[choice].values.tolist()
    string = ''
    for i, item in enumerate(lst):
        string += f", {item}" if i else f"{item}"
    return string


def number_of_items(choice, df):
    return len(df[choice].values.tolist())
