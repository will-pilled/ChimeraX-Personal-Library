# This is an activated Rubisco structure

from chimerax.core.commands import run
run(session, 'open 1IR2')
run(session, 'show c')
run(session, 'show a')
run(session, 'color sequential palette PuBu')
run(session, 'style ball')
run(session, 'transparency 75 c')
run(session, 'cartoon style modeHelix tube sides 20')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')
run(session, 'sequence chain /1 /2 /3 /4 /5 /6 /7 /8 /I /J /K /L /M /N /O /P')
#Sequences the smaller subunit
run(session, 'sequence chain /1 /2 /3 /4 /5 /6 /7 /8 /I /J /K /L /M /N /O /P')
#Sequences the larger subunit

