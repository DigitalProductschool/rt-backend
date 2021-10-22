
def config_scholarship(location, country):
        oecd_country = ["Australia", "Austria", "Belgium", "Canada", "Chile", "Colombia", "Costa Rica", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Israel", "Italy",
                       "Japan", "Korea", "Latvia", "Lithuania", "Luxembourg", "Mexico", "Netherlands", "New Zealand", "Norway", "Poland", "Portugal", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom", "United Stated"]

        if location == "Munich":
            scholarship_option = "You will also receive a monthly scholarship of 750€."
        elif country in oecd_country and location != "Munich":
            scholarship_option = "You will also receive a monthly scholarship of 500€."
        else:
            scholarship_option = "You will also receive a monthly scholarship of 300.00€  (incl. 50.00€ internet grant)."
        return scholarship_option
