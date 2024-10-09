from chimerax.core.commands import run
run(session, 'open 3ZUQ')
run(session, 'show c')
run(session, 'show a')
run(session, 'cartoon style coil xsection oval')
run(session, 'cartoon style xsection barbell modeHelix default')
run(session, 'lighting flat')
run(session, 'show s')
run(session, 'sequence chain all')
run(session, 'color sequential palette PuBu')
run(session, 'transparency 90 s')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')