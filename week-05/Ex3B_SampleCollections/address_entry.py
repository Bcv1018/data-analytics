# Working with Dictionaries
# Dictionary for Youngster Joey information
contact_info = {
    "name": "Joey",
    "Address": "123 Route30",
    "City": "CherryGrove City",
    "State": "Johto",
    "Zip": "30315"
}

# Print dictionary in proper format for mailing
print(f"""
{contact_info['name']}
{contact_info['Address']}
{contact_info['City']} {contact_info['State']} {contact_info["Zip"]}
""")

# Removing name key value
contact_info.pop("name")
# print(contact_info)

# New dictionary for Name
full_name = {
    "first name": "Joey",
    "last name": "Pokemon"
}
# Adding honorific to full name
full_name.update({
    "honorific": "Youngster"
})
#print(full_name)

# adding full_name to contact_info
contact_info.update({"full_name": full_name})
# print(contact_info)

# Updated address
print(f"""
{full_name['honorific']} {full_name["first name"]} {full_name['last name']}
{contact_info['Address']}
{contact_info['City']} {contact_info['State']} {contact_info["Zip"]}
""")