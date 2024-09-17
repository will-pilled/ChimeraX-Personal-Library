# This is the acetylcholine binding protein from Lymnaea stagnalis

from chimerax.core.commands import run
run(session, 'open 3U8M')
run(session, 'show c')
run(session, 'show a')
run(session, 'cartoon style modeHelix tube sides 20')
run(session, 'color sequential palette Reds-5')
run(session, 'style ball')
run(session, 'transparency 50 c')
run(session, 'sequence chain /A /B /C /D /E /F /G /H /I /J /K /L /M /N /O /P /Q /R /S /T')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')
