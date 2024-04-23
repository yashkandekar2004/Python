city_pincode_mapping = {
    'Nashik': 422611,
    'Pune': 422622,
    'Mumbai': 422633,
}

user_data = []

users = int(input("Enter the number of users: "))

for i in range(users):
    print(f"\nUser {i + 1}:")
    
    name = input("Enter user name: ")
    
    print("Choose the Cities:")
    for city in city_pincode_mapping:
        print(city)
    
    selected_city = input("Enter the user's city: ")
    
    pincode = city_pincode_mapping.get(selected_city, "DefaultPincode")

    user_data.append({
        'Name': name,
        'City': selected_city,
        'Pincode': pincode
    })

print("\nUser Information:")
for user in user_data:
    print(f"Name: {user['Name']}, City: {user['City']}, Pincode: {user['Pincode']}")
