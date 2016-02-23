##=========================================================================================
#
#           Homework 2 |  Riley Benson | EP 476 | Prof. Paul Wilson
#
#==========================================================================================
#
# Initializing descriptions of event described in problem statement
particle_ID = 43
event_loc = [3,4,5]
prev_loc = [8,1,12]
part_energy = 2.3 # [MeV]
atom_type = 1002  # Where the last three numbers are atomic mass,
		  # the first 1-3 are atomic number
rxn_type = 102    # Code pertaining to specific reaction that occurs

#==========================================================================================

# Function to find distance between two collision sites
def collision_dist(loc_1,loc_2):
    import numpy as n

# Defensive programming, make sure locations have equal dimensions
    if len(loc_1) != len(loc_2):
        return "Coordinates do not have same number of dimensions"
        sys.exit()


    j = len(loc_1)
    diff_sq = n.zeros(j)
    for i in range(j):
        diff_sq[i] = (loc_2[i] - loc_1[i])**2  # square of the difference x,y,z cordinates 

    distance = n.sqrt(n.sum(diff_sq)) # square root of the sum of the differences is the 
                                      # distance forumula
    
    return "The distance between collisions for this is event is " + str(distance)

print(collision_dist(prev_loc,event_loc))



#=============================================================================================

# Function to calculate unit vector of particle path between two collisions

def part_unit_vec(location_1,location_2):

    import numpy as n

# Defensive Programming, make sure locations have equal dimensions
    if len(location_1) != len(location_2):
        return "Coordinates do not have same number of dimensions"
        sys.exit()

# Loop through locations to get motion vector, then find magnitude, divide vector by magnitude   
    j = len(location_1)
    diff_sqr = range(j)
    vector = range(j)
#  Loop through locations and make direction vector
    for i in range(j):
        vector[i] = (location_2[i] - location_1[i])
        diff_sqr[i] = vector[i]**2

    magnitude = n.sqrt(n.sum(diff_sqr)) # distance formula


    unit_vector = range(len(vector)) # initialize unit vector variable
    for i in range(len(unit_vector)): # loop thru vector and divide each value by the magnitude
        unit_vector[i] = float(vector[i])/float(magnitude)

    return unit_vector
unit_vec = part_unit_vec(prev_loc,event_loc)
print("\nThe unit vector of particle 43 is " + str(unit_vec))

#==========================================================================================

# Function to calculate energy of particle in eV from MeV

def MeV_to_eV(energy):
    eV = energy*10**6
    return eV

part43_energy = MeV_to_eV(part_energy)
print("\nThe energy of particle 43 is " + str(part43_energy) + " eV")


#==============================================================================================

# ii.
#
# I think the best way for storing all the information about an event would be a dictionary.
# The dictionary would allow the coder to label all of the values that are listed in the dictionary.
#
# Comparatively, a list could work if the user knew what values corresponded to what physical meaning.
# Same goes for a tuple. A set wouldn't make any sense as there would be no way to know which values
# correspond to which physical meaning. 
#
#
#==============================================================================================
#
# iii.
#
# I think the best way to store many events together in a 'log' would be in a list, if you could count
# on the fact that the physical events would happen chronologically, as in event 1 happened first, event
# 2 happened second, etc. If this were the case, then the location of the dictionary in the list could 
# used as the event number identifier and each location would hold a dictionary containing all the 
# pertinent information. 
#
# If this were not the case, then I think the best container for this log would be another dictionary.
# This way, regardless of the order the events are taking place, a label of the event number can be
# tracked. The label of each entry in log dictionary would correspond to another dictionary containing
# the information about that event. Using this system, the user/coder can call upon any event in the 
# dictionary utilizing the label of that event. Since I do not know which is the case, I will use 
# dictionaries in a dictionary. 
#
#
# Function to store three copies of described event in above described structure

def three_copies(part_number, event_pos, part_direc, type_atom, type_rxn, particle_energy):

    events_log = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0} # initialize events log dictionary

    for l in [1,2,3,4,5,6,7,8,9]: # loop thru dict and update each key
        events_log.update({l:{"particle number":part_number,"particle energy":particle_energy, "event position":event_pos, "particle direction":part_direc, "atom type":type_atom, "rxn number":type_rxn}})
    
    # This returns the whole dict
    return events_log

events_log = three_copies(particle_ID, event_loc, unit_vec, atom_type, rxn_type, part43_energy)

# Printing the whole dictionary is very cumbersome and hard to read so just the third event is printed
print("\nThe dictionary of event 3 is " + str(events_log[2]))


#===============================================================================================

# iv. 

# a. This is a function and accompanying code to determine change in energy between 5th and 6th event
#
# An assumption is made that the expectation is not to create arbitrary events to analyze. This code 
# will reference the 5th and 6th events in above events_log. This then applies for the following b, 
# and c where they will refer to events in the log above. As a result of all the events being the same,
# all of the values should be zero. This will be the confirmation that the code is working. 
#
#

def energy_change(rxn_log):
    
    energy_change = (rxn_log[6]["particle energy"] - rxn_log[5]["particle energy"])
    
    return energy_change


energy_chng = energy_change(events_log)

print("\nThe change in energy between the 5th and 6th event is " + str(energy_chng) + " eV")


#=================================================================================================

# b. This function and accompanying code will calculate the distance between the 7th and 8th event
#    It will accomplish this by calling a previous function that calculates distance between two
#    points.


def position_change(rxn_log):
    # call collision dist function for events 7 and 8
    pos_change = collision_dist(rxn_log[7]["event position"], rxn_log[8]["event position"])

    return pos_change

loc_change = position_change(events_log)

print("\nThe distance between event 7 and event 8 is " + str(loc_change))


#==================================================================================================

# c. This function and accompanying code will calculate whether the 4th event was more aligned with
#    the z-axis than the 9th event. 
#
# In order to actually see a value for this event, an update will be made to the direction of event 4
# so an actual comparison can be made. This is the following code:


unit_vec_4 = part_unit_vec([1,2,3], [6,2,12]) # create arbitrary unit vector for event 4

# Update event 4 in the events_log 
events_log.update({4:{"particle number":particle_ID,"particle energy":part_energy, "event position":event_loc, "particle direction":unit_vec_4, "atom type":atom_type, "rxn number":rxn_type}})

# From here the code will compute which event is more aligned with the z-axis.


def direction_z(rxn_log):

    import numpy as n
    
    event9_z = 0 # initialize variable
    event4_z = 0 # initialize variable

    z_axis = [0, 0, 1]
    event9_z = n.dot(rxn_log[9]["particle direction"], z_axis)  # Finds portion of direction of event 9 in z direction
    event4_Z = n.dot(rxn_log[4]["particle direction"], z_axis)  # Finds portion of direction of event 4 in z direction


# If statement checks to see which event has a larger dot product with the unit vector alont the z-axis
    if event9_z > event4_z:
        return ["9th event","4th event"]

    else: 
        return ["4th event", "9th event"]

z_event = direction_z(events_log)

print("\nThe " + z_event[0] + " was more aligned with the z-axis than the " + z_event[1] + " was.")
