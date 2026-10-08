from shlex import split


challenge = ['Thirty', 'Days', 'Of', 'Python']
result = ' ' .join(challenge)
print(result)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding = ['Coding', 'For', 'All']
result2 = ' ' .join(coding)
print(result2)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'  
print(company)
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:14])
print(company.index('Coding'))
print(company.replace('Coding', 'Python'))
print(split(company, ', '))
