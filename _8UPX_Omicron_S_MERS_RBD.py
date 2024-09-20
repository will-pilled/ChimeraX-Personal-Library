# Severe acute respiratory syndrome coronavirus 2

from chimerax.core.commands import run
run(session, 'open 8UPX')
run(session, 'show c')
run(session, 'show a')
run(session, 'show s')
run(session, 'color bychain')
run(session, 'style ball')
run(session, 'transparency 90 s')
run(session, 'sequence chain /A /B /C')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')
