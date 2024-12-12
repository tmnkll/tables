from Tables.load_and_save import load_table, save_table
from Tables.other_functions import save_table_text, save_table_pickle, get_rows_by_number, get_rows_by_index, get_column_types, set_column_types, _cast_value, detect_column_types, detect_type

# Загрузка данных
table = load_table('file1.csv', 'file2.csv')
print("Loaded table:", table)

# Сохранение данных
save_table(table, max_rows=2, base_file_name='output')
save_table_text(table, 'output.txt')
save_table_pickle(table, 'output.pkl')

# Извлечение строк
rows = get_rows_by_number(table, 1, 3)
print("Rows by number:", rows)

rows = get_rows_by_index(table, 'Alice')
print("Rows by index:", rows)

# Определение и изменение типов столбцов
types = get_column_types(table)
print("Column types:", types)

set_column_types(table, {1: 'int'}, by_number=True)
print("Updated table:", table)

# Автоматическое определение типов
detect_column_types(table)
