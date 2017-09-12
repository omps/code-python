#!/usr/bin/python
ctr=1
while ctr < 1000:
    ctr += 1
## PDB
# commands: you can give commands to run in script. Usage is commands 1
# at the prompt (com) p ctr
# (com) c
# (pdb)

# conditions: the conditions are use to check if there are errors between the iteration. For eg. in the code above when iterating though line 1000, we think there are error at line 500 to 524 we can set condition at that break point.
# for eg.
# inside pdb
# (pdb) b 3 # will set the break point at line 3 which is our while loop start.
# (pdb) condition 1 ctr > 500 and ctr < 524
# (pdb) p ctr
# (pdb) c
# (pdb) s # to step into again
# Noww this all can be automated using commands.
# so this whole thing will be exectued using the command from line no. 500 till line no 524. and thow us out of the PDB once completed.
