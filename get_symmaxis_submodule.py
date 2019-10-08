import stored
python
def get_symmaxis(chainlist=['A','B']):
    chainstring='' # Just making a string out of the selected chains, that is item+item+item ... to use pymol synmtax later.
    for item in chainlist:
        chainstring=chainstring+'+'+str(item)
    stored.ca=[]
    cmd.iterate('name ca and chain %s' %(chainlist[0]),'stored.ca.append(resi)') # Goes through all amino acids in chain A and stores their resi numbers in a list.
    for residue in stored.ca: # This loops through all amino acids in the list and uses their resi numbers, to make a selection of all ca atoms in all resis in all chains selected at the begining..
       cmd.pseudoatom('symmaxis','resi %s and name ca and chain %s' %(residue,chainstring)) # makes a pseudoatom at the center of each selection.
print 'Imported get_symmaxis submodule from JE. Use with:'
print '> get_symmaxis()'
print 'to get a symmetry axis for chains A and B (default behaviour).'
print 'Or use with > get_symmaxis(['A','B','C','D','E'])'
print ' to get a symmaxis between the chains defined in the list.'
python end
