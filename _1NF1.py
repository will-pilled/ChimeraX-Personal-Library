from chimerax.core.commands import run
run(session, 'open 1NF1')
run(session, 'show c')
run(session, 'show a')
run(session, 'style stick')
run(session, 'color sequential palette Reds-5')
run(session, 'hide s')
run(session, 'cartoon style (#1 & coil) xsection oval')
run(session, 'cartoon style #1 xsection barbell modeHelix default')
run(session, 'transparency 50 atoms')
run(session, 'lighting flat')
run(session, 'sequence chain all')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')