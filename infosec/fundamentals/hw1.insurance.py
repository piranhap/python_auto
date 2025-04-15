"""
Create a python file that asks an insurance company the following inputs:



Insurance company name

Number of employees

location (city, OR country, OR state)

Lowest price for a policy

The highest price for a policy

The output will consist of a prompt almost like an ad. For example:

"We are Company LLC located in India. Our 55 employees can help you find the policy that is right for you with policies ranging from $15 to $300 per month!"
"""

ins_name = input('What is your company name? ')
emp = int(input('How many employees do you have? ')) 
loc = input('What is your location? City or country or state ')
low = input('What is the lowest pruce for a policy ')
high = input('What is the highest price for a policy ')


print(f"We are {ins_name} located in {loc}. Our {emp} can help you find the policy that is right for you with policies ranging from ${low} to ${high} per month!")
