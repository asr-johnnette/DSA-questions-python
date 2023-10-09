user_input = [] 

# Define the number of inputs you want to receive
num_inputs = int(input("Enter the number of elements: "))

for i in range(num_inputs):
    element = input(f"Enter element {i + 1}: ")  
    user_input.append(element)
print("Array:", user_input)
max_value=0
max_value = user_input[0]
for element in user_input:
    if element > max_value:
        max_value = element


print(max_value,"is greatest in the array list", user_input)