# NMR Structure of stereo-array isotope labelled (SAIL) maltodextrin-binding protein (MBP)

from chimerax.core.commands import run
run(session, 'open 2D21')
run(session, 'show c')
run(session, 'show a')
run(session, 'transparency 70 atoms')
run(session, 'style stick')
run(session, 'color sequential palette Reds-5')
run(session, 'cartoon style #2-21#!1 modeHelix tube sides 20')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')