# A strain of the Cucumber Mosaic Virus that commonly infects wetland/marsh plants through primarily aphids.
# Plants with CMV typically show symptoms of mosaic-like patterns on leaves, poor overall vigor, and yellowing.

from chimerax.core.commands import run
run(session, 'open 1f15')
run(session, 'show c')
run(session, 'show a')
run(session, 'style ball')
run(session, 'sym #1 assembly 1 copies true')
run(session, 'cartoon style (#2 & coil) xsection oval')
run(session, 'cartoon style #2 xsection barbell modeHelix default')
run(session, 'transparency 25 c')
run(session, 'rainbow palette purples-5')
# Alternately, replace the rainbow command with 'color bychain'
run(session, 'sequence chain /A /B /C')
run(session, 'ui tool show "Side View"')
run(session, 'view orient')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')