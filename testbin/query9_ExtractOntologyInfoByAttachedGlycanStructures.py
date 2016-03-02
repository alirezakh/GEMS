### Sample usage from testbin directory: python query9.py &> [YOUR-OUTPU-FILE]
### This query searches Glycan structures based on the given sequence of Glycans side atom orientations and these Glycans would be attached to eachother. ExtractOntologyInfoByAttachedGlycanStructures(structures)

import sys
sys.path.insert(0, '../')
import gmml
temp = gmml.Assembly()

structure1 = gmml.string_vector()
structure1.push_back("P");
structure1.push_back("Up");
structure1.push_back("");
structure1.push_back("Down");
structure1.push_back("Up");
structure1.push_back("Down");
structure1.push_back("Up");

structure2 = gmml.string_vector()
structure2.push_back("P");
structure2.push_back("Up");
structure2.push_back("");
structure2.push_back("Down");
structure2.push_back("Up");
structure2.push_back("Down");
structure2.push_back("Up");

structures = gmml.dihedral_vector()
structures.push_back(structure1)
structures.push_back(structure2)

temp.ExtractOntologyInfoByAttachedGlycanStructures(structures)