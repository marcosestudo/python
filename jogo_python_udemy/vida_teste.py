vida_perdida = 0
vida = f"vida ]{'|' * (12 - vida_perdida)}{' ' * vida_perdida}["
print(vida)
while vida_perdida < 12:
    vida_perdida += 4
    vida = f"vida ]{'|' * (12 - vida_perdida)}{' ' * vida_perdida}["
    print(vida)
