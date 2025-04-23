import schemdraw
import schemdraw.elements as elm

def draw_diff_amp(params):
    R1_val, R2_val = params  # Example: Replace with actual circuit parameters if needed

    with schemdraw.Drawing() as d:
        # Power rail
        d.add(elm.SourceV(label='VDD').up().label('VDD', loc='top'))

        # PMOS current mirror
        d.add(elm.Line().down().length(0.5))
        M3 = d.add(elm.PMos(label='M3', anchor='source').right())
        M4 = d.add(elm.PMos(label='M4', anchor='source').right())

        # Gates tied together
        d.add(elm.Line().left().at(M4.gate).tox(M3.gate))
        d.add(elm.Line().down().at(M3.gate).length(0.5))

        # Load resistors
        last_resistor = d.add(elm.Resistor(label=f'R1\n{R1_val:.1f}Ω').down())
        d.add(elm.Dot())
        d.push()
        d.add(elm.Resistor(label=f'R2\n{R2_val:.1f}Ω').down().at(last_resistor.end).right())
        d.add(elm.Dot())
        d.add(elm.Ground())

        # Differential pair
        d.add(elm.Line().at(last_resistor.start).down().length(0.5))
        M1 = d.add(elm.NMos(label='M1').left())
        M2 = d.add(elm.NMos(label='M2').right().at(last_resistor.end))

        # Connect sources together and to tail current source
        d.add(elm.Line().down().at(M1.source).length(0.5))
        d.add(elm.Dot())
        d.add(elm.SourceI(label='I_bias').down())
        d.add(elm.Ground())

        # Output nodes
        d.add(elm.Line().left().at(M1.drain).length(0.5).dot(open=True).label('OUT1', loc='left'))
        d.add(elm.Line().right().at(M2.drain).length(0.5).dot(open=True).label('OUT2', loc='right'))

        # Input gates
        d.add(elm.Line().left().at(M1.gate).length(0.5).dot(open=True).label('IN1', loc='left'))
        d.add(elm.Line().right().at(M2.gate).length(0.5).dot(open=True).label('IN2', loc='right'))

def draw_layout():
    with schemdraw.Drawing() as d:
        # Place components in a grid layout
        d.add(elm.Resistor().at((0, 0)))
        d.add(elm.Capacitor().at((2, 0)))
        d.add(elm.Ground().at((4, 0)))

