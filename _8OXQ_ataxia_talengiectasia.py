from chimerax.core.commands import run
run(session, 'open 8OXQ')
run(session, 'show c')
run(session, 'show a')
run(session, 'show s')
run(session, 'color bychain')
run(session, 'cartoon style (#2 & coil) xsection oval')
run(session, 'cartoon style #2 xsection barbell modeHelix default')
run(session, 'color bychain')
run(session, 'lighting gentle')
run(session, 'sequence chain /A /B')
run(session, 'transparency 85 s')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')
