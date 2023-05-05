# Guest List

# Part 1 - Make a list that includes at least 3 people

guest_list = []

guest_list.append('Jim')
guest_list.append('Ralph')
guest_list.append('Mike')

print(guest_list)


# Little bit of cheating on this task, but i think i have learnt in my days of powershell if you know of a shorter way of doing this, DO IT!

for guest in guest_list:
    print(f"I would like to formally invite {guest} to my dinner party")


# One of your guests can't make it, so you need to amend your guest list

party_poopers = guest_list.pop(2)

for guest in guest_list:
    print(f"\nI would like to update the invite to new people {guest}, this is due to {party_poopers} not wanting to come")
    
    
# You found a bigger table, let's invite 3 more people

print("\n We found a bigger table!!!")

guest_list.insert(0, 'Bob')
guest_list.insert(2, 'Lisa')
guest_list.append('Rachel')

for guest in guest_list:
    print(f"We found a bigger table, so i would like to send a new invitation. {guest}")
    
################## Time for ChatGPT To Attempt the above, only going to use GPT 4  #####################################

# Guest List

# Part 1 - Make a list that includes at least 3 people

# Instead of appending each name individually, create the list with initial names
guest_list = ['Jim', 'Ralph', 'Mike']

print(guest_list)

# Use a function to handle sending invitations
def send_invitations(guests):
    for guest in guests:
        print(f"I would like to formally invite {guest} to my dinner party")

send_invitations(guest_list)

# One of your guests can't make it, so you need to amend your guest list

# Instead of using two separate loops, create a single function to handle guest changes
def update_guest_list(guests, party_pooper_index):
    party_pooper = guests.pop(party_pooper_index)
    print(f"\nI would like to update the invite due to {party_pooper} not wanting to come")
    send_invitations(guests)

update_guest_list(guest_list, 2)

# You found a bigger table, let's invite 3 more people

print("\nWe found a bigger table!!!")

# Instead of inserting/appending one by one, use a list of new_guests and extend the guest_list
new_guests = ['Bob', 'Lisa', 'Rachel']
guest_list = guest_list[:1] + [new_guests[0]] + guest_list[1:] + new_guests[1:]

send_invitations(guest_list)


"""
Here are the improvements I made:

Created the initial guest list in a single line.
Created a function send_invitations() to handle sending invitations, reducing code repetition.
Created a function update_guest_list() to handle guest updates, reducing code repetition.
Instead of inserting/appending one by one for new guests, used a list and combined it with the existing guest list in a single line.
"""