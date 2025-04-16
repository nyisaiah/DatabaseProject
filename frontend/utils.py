
def format_phone(raw_phone: int):
    return f"({raw_phone[:3]}) - {raw_phone[3:6]} - {raw_phone[6:]}"

def format_license_plate(licence_plate: str):
    return licence_plate.upper()

def format_name(name: str):
    return name.title()

def format_customer(customer : dict):
    return f'{customer["custfname"]} {customer["custlname"]}'

def format_car(car : dict):
    return f'{car['licenseplate']}, {car['makename']} {car['modelname']}'