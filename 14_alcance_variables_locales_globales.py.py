def funcion():
    variable_local= 10
    print(variable_local)

variable_global= 20
def funcion2():
    print(variable_global)


funcion()
funcion2()
print(variable_global)
print(variable_local)
