import schemdraw
import schemdraw.elements as elmt


d = schemdraw.Drawing()

# Voltage source
d.add(elmt.SourceV().up().label('10V'))

# Resistor
d.add(elmt.Resistor().right().label('R'))

# Wire down
d.add(elmt.Line().down())

# Ground
d.add(elmt.Ground())
d.add(elmt.Line().left())

# Show drawing
d.draw()
print(d, type(d))

