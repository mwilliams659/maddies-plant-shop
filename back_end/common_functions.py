def update_field(table_name, field, column, value, value2):
	return f"UPDATE {table_name} SET {field} = {value} WHERE {column} = {value2};"

def create_table(table_name, columns, datatypes):
    return f"CREATE TABLE table_name ({columns[0]} {datatypes[0]},{columns[1]} {datatypes[1]});"