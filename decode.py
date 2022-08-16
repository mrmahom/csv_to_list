def get_choices_list(df):
    return df.columns.values.tolist()


def text_file_generator(choice, df):
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d_%H-%M-%S")  # YYYY-mm-dd_HH-MM-SS
    lst = df[choice].values.tolist()
    with open(f"ID_list_{dt_string}", 'w', encoding='utf-8') as output:
        for item in lst:
            print(item, sep=',', file=output)
    return output
