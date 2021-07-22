EMPLOYEES = [
    {
        "id": 1,
        "name": "Jordan Rosas",
        "position": "Lead Engineer",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Jeffrey Weisel",
        "position": "Jr. Engineer",
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Zach Weisel",
        "position": "Buis Dev",
        "locationId": 3
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee