# 6SCL: Barley Yellow Dwarf Virus Cryo-EM Structure
# Commonly infects grass species such as cordgrass
# Spreads via aphids

from chimerax.core.commands import run
run(session, 'open 6SCL')
run(session, 'show a')
run(session, 'hide c')
run(session, 'color bychain')
run(session, 'style ball')
run(session, 'sym #1 assembly 1 copies true')
run(session, 'sequence chain /A /B /C')
run(session, 'ui tool show "Side View"')
run(session, 'view orient')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')