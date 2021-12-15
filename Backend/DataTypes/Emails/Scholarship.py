from Backend.DataTypes.Scholarship import Munich, OECD, NonOECD

def config_scholarship(location, country):
        oecd_country = ["Australia", "Austria", "Belgium", "Canada", "Chile", "Colombia", "Costa Rica", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Israel", "Italy",
                       "Japan", "Korea", "Latvia", "Lithuania", "Luxembourg", "Mexico", "Netherlands", "New Zealand", "Norway", "Poland", "Portugal", "Slovak Republic", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "United Kingdom", "United Stated"]

        if location == "Munich":
            return Munich
        elif country in oecd_country and location != "Munich":
            return OECD
        else:
            return NonOECD