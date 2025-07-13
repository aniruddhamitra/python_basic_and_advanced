# this program simply demonstetes the use of variables and operators in Python


income = 250_000

income_tax_rate = 0.05

gst_tax_rate = 0.43

savings = income - (income * income_tax_rate) - (income * gst_tax_rate)

print ('In India , a person with an income of', income, 'pays a tax of', income * income_tax_rate,
       'as income tax and', income * gst_tax_rate, 'as GST tax.and saves', savings, 'in total.')
