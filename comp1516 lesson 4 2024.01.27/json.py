# author: jason wilder

fname = "tiger"
lname = "woods"
years_xp = 20
hourly_wage_cad = 50000

json = ('[\n\t{\n\t\t"first_name": "%s",\n\t\t"last_name": "%s",\n\t\t"experience": %d,\n\t\t"hourly_wage_cad": '
        '%.2f\n\t}\n]') % (fname,lname,years_xp,hourly_wage_cad)

print(json)
