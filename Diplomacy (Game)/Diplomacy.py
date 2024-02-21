#!/usr/bin/env python3

# ---------------------------
# projects/diplomacy/Diplomacy.py
# Copyright (C)
# Glenn P. Downing
# ---------------------------

# ------------
# diplomacy_read
# ------------
def diplomacy_read(s):
    """
    read a list of string
    in a list
    return every input line has three elements separated by spaces: an army, a location, and an action. 
    return a list of all inputs, representing all of the inputs
    """
    s = s.read()
    a = s.split("\n")
    return a

# -----------------
# diplomacy_Battle
# -----------------
def city_with_armies(current_standing):
    """
    Current_standing is list of the curent army and it location
    Will find the cities with more than 2 armies and army battleing
    Return cities_with_armies & battling
    """      
    # Creating dictionary with cities and the number of armies in each
    city_army = {}
    for army_city in current_standing:
        # Read entry one at a time
        city = army_city[1:]
        city = "".join(city.split())
        # If city not found in dictonary, add it in and set number of armies to 0
        if city not in city_army:
            city_army[city] = 0
        # Update count of Army in City
        city_army[city] += 1
        
    # Finding cities with more than 2 armies
    cities_with_armies = []
    for city, army_count in city_army.items():
        if army_count >= 2:
            cities_with_armies.append(city)

    battling = []     
    for x in current_standing:
        city = x[1:]
        city = "".join(city.split())
        army = x[0:]
        if city in cities_with_armies:
            battling.append(army)   
    # Returning the cities with more than 2 armies and armies in that city
    return(cities_with_armies, battling)


# --------------------------
# diplomacy_surviving_armies
# --------------------------
def surviving_armies(outputs, total_of_support, loaded_city, fighting, current_support, max_support):  
    """
    total_of_support is a dict of all armies with support
    loaded_city is a list of city in which a battle will occur
    fighting is a list of army that will go into battle
    current_support is the army that are dealing with any support in certain city
    Outputs is the current list of oytptus that we are updating 
    Cheking If an army is battling and update all current location
    Updating and returning Outputs
    """  
    for x in range(len(loaded_city)):
        fighters = []
        # Getting all all cities fight to see how much support they hvae
        for move in fighting:
            army, city = move.split()
            if loaded_city[x] == city: # pragma: no cover
                fighters.append(army)
        # Checking who has the most support
        for x in range(len(fighters)):
            if fighters[x] in total_of_support.keys():
                # If less support than max, update Army loaction to dead
                if fighters[x] != max_support and total_of_support.get(fighters[x]) < total_of_support.get(max_support):
                    update_Loaction(fighters[x], outputs) # pragma: no cover
                # If equal support to max, update All Army loaction to dead
                elif fighters[x] != max_support and total_of_support.get(fighters[x]) == total_of_support.get(max_support):
                    update_Loaction(fighters[x], outputs) # pragma: no cover
                    update_Loaction(max_support, outputs) # pragma: no cover
            # If no support, update Army loaction to dead
            else:
                update_Loaction(fighters[x], outputs) # pragma: no cover
    # If an army who was supporting someone is dead, update other army to dead 
    update_Army_Loaction (current_support,outputs )
    return (outputs)


# --------------------------
# diplomacy_updating_armies
# --------------------------
def update_Army_Loaction (current_support,outputs ):
    """
    current_support is the army that are dealing with with any support
    Outputs is the current list of oytptus that we are updating 
    Cheking If an army is attacked while supporting another army,its support becomes invalid.
    Updating and returning Outputs
    """  
    look = ([army[0] for army in outputs])
    for key, value in current_support.items():
        Army, supporting = key, value
        for x in range(len(look)):
            if look[x] == supporting:
                if '[dead]' in outputs[x]:
                    for i in range(len(look)):# pragma: no cover
                        if look[i] == Army:
                            outputs[i] = Army + ' ' + '[dead]'
    return outputs

# ------------------------------------
# diplomacy_updating_armies_Dictionary
# ------------------------------------
def update_Loaction (Army, outputs):  
    """
    Army is the army that are dealing with
    Outputs is the current list of oytptus that we are updating 
    Cheking If an army is attacked durring battle
    Updating and returning Outputs
    """  
    look = ([army[0] for army in outputs])
    for y in range(len(look)):
        if look[y] == Army:
            outputs[y] = Army + ' ' + '[dead]'
    return outputs


# --------------
# diplomacy_eval
# --------------
def diplomacy_eval(i):
    """
    i a list of inputs
    return a list of the outputs with the given inputs
    """
    # Assert the input is a list of is not empty
    assert len(i) > 0
    
    outputs = []
    # Mapping each city to the city it currently supports
    current_support = {}
    total_of_support = {}
    for move in i:
        # Getting len for input
        find = move.split()
        # Extracting army, city, action from input
        if len(find) == 3:
            army, city, action = move.split()
        # Extracting army, city, action, target from input
        else:
            army, city, action, target = move.split()

        # When Army is in Holding, nothing changes
        if action == 'Hold':
            outputs.append(army + ' ' + city)

        # When action is Move, Update the output string to new loaction
        elif action == 'Move':            
            outputs.append(army + ' ' + target)

        # When action is Support, Update with Army  reciving support and from whom
        elif action == 'Support':
            # Army is in dictrion, increase the support number
            if target in total_of_support: # pragma: no cover
                total_of_support[target] += 1
            # Army is providing support to another army
            else:
                total_of_support[target] = 1
                
            current_support[target] = army
            # Update the output string
            outputs.append(army + ' ' + city )
    
    # Retrieving cities with more than 2 armies
    loaded_city, fighting  = city_with_armies(outputs)

    # Retrieving cities with the max support
    max_key,max_val = None , None
    for key, val in total_of_support.items(): # pragma: no cover
        if max_val is None or val > max_val:
            max_val,max_key = val, key
    max_support = max_key
    
    # Retrieving armies that survive the battle
    final_output = surviving_armies(outputs, total_of_support, loaded_city, fighting, current_support,max_support)
    final_output.sort()
    
    # Assert the output is a list of armies sorted alphabetically.
    assert final_output == sorted(final_output)
    assert len(final_output) > 0
    
    return final_output


# ---------------
# diplomacy_print
# ---------------
def diplomacy_print(w, v):
    """
    print a list of inputs
    w a writer
    v is the outcome
    """ 
    for x in range(len(v)):
        # Done need a newline after the last output
        if x == (len(v) -1):
            w.write(str(v[x]))
        else: 
            w.write(str(v[x]) + "\n")
        
        
# -------------
# diplomacy_solve
# -------------
def diplomacy_solve(r, w):
    """
    r a reader
    w a writer
    """
    i = diplomacy_read(r)
    v = diplomacy_eval(i)
    diplomacy_print(w, v)