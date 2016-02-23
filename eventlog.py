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
        diff_sq[i] = (loc_2[i] - loc_1[i])**2

    distance = n.sqrt(n.sum(diff_sq))
    
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

    for i in range(j):
        vector[i] = (location_2[i] - location_1[i])
        diff_sqr[i] = vector[i]**2

    magnitude = n.sqrt(n.sum(diff_sqr))


    unit_vector = range(len(vector))
    for i in range(len(unit_vector)):
        unit_vector[i] = float(vector[i])/float(magnitude)

    return unit_vector
unit_vec = part_unit_vec(prev_loc,event_loc)
print("\nThe unit vector of particle 43 is " + str(unit_vec))

#==========================================================================================

# Function to calculate energy of particle in eV from MeV

def MeV_to_eV(energy):
    eV = energy*10**6
    return eV

print("\nThe energy of particle 43 is " + str(MeV_to_eV(part_energy)) + " eV")


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

def three_copies(part_number, event_pos, part_direc, type_atom, type_rxn):

    events_log = {1:0, 2:0, 3:0}

    for l in [1,2,3]:
        events_log.update({l:{"particle number":part_number, "event position":event_pos, "particle direction":part_direc, "atom type":type_atom, "rxn number":type_rxn}})
    
    # This returns just the dictionary of the last "event" to show the loop worked
    return events_log[2]

# Printing the whole dictionary is very cumbersome and hard to read so just the third event is printed
print("\nThe dictionary of event 3 is " + str(three_copies(particle_ID, event_loc, unit_vec, atom_type, rxn_type)))





#
#===============================================================================================


