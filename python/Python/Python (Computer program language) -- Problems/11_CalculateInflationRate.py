year2020 = int(input("Enter frist Price : "))
year2022 = int(input("Enter second Price : "))
swelling=(float)(year2022-year2020)/year2020*100
# year2024=year2022+(swelling/10)
# print('Extra=%:',swelling,'\t\if everything will be ok, Price year 2024 is about :',year2024 )
print("Swelling 2022 is : %",swelling)