CUSTOMERS = [
    {
        "id": 1,
        "name": "Samantha Rosas",
        "phone": "360-489-9107"
    },
    {
        "id": 2,
        "name": "Baka Weisel",
        "phone": "123-123-1234",
    },
    {
        "id": 3,
        "name": "Zach Weisel",
        "phone": "321-321-3211",
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
            
    return requested_customer