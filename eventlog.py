# Initializing descriptions of event described in problem statement
particle_ID = 43
event_loc = (3,4,5)
prev_loc = (8,1,12)
part_energy = 2.3 # [MeV]
atom_type = 1002  # Where the last three numbers are atomic mass,
		  # the first 1-3 are atomic number
rxn_type = 102    # Code pertaining to specific reaction that occurs

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
    
    return("The distance between collisions for this event is " + str(distance))


print(collision_dist(prev_loc,event_loc))

