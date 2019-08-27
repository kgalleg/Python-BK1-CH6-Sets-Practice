# Python Sets -A set is a collection of things, like a list, but the collection is both unordered, and contains no duplicate elements. Developers use sets to easily filter down other collections to unique elements, and to see if two, or more, collections share any similar items.



# Practice: Showroom & Junkyard
# Create an empty set named showroom.

#this is my set of car models
# Add four of your favorite car model names to the set.
showroom = {'Pilot', 'Charger', 'Civic', 'Altima'}

# Print the length of your set.
print(len(showroom))

# Pick one of the items in your show room and add it to the set again.

# showroom.add('something')
# print(showroom)

#adding a second 'Charger' wont add it to the list twice.  Takes care of multiples
showroom.add('Charger')
print(showroom)

# Print your showroom. Notice how there's still only one instance of that model in there.
#see above... this is done!


# Using update(), add two more car models to your showroom with another set.

add_to_showroom = {'Cooper', 'Xterra'}

showroom.update(add_to_showroom)
print("new showroom", showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard("Cooper")
print("sold cooper", showroom)

