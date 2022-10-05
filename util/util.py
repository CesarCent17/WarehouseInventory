def validate_positive_number(number):
    response = ["", False]
    if number > 0:
        response = ["Ok", True]
    else:
        response = ["Debe ingresar un numero positivo", False]
    return response
