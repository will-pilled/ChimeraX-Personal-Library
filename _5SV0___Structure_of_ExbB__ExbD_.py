# This is a biopolymer transport protein

from chimerax.core.commands import run
run(session, 'open 5SV0')
run(session, 'show c')
run(session, 'show a')
run(session, 'rainbow palette pastel1-7')
run(session, 'style ball')
run(session, 'transparency 50 c')
run(session, 'sequence chain /B /C /D /E /F /G /H /I /J /A')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')