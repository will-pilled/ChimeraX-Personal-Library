# Structure and Biochemistry of a Promiscuous Thermophilic Polyhydroxybutyrate Depolymerase from Lihuaxuella thermophilia

from chimerax.core.commands import run
run(session, 'open 8DAJ')
run(session, 'show c')
run(session, 'show a')
run(session, 'show s')
run(session, 'color sequential palette Purples-5')
run(session, 'style stick')
run(session, 'transparency 80 s')
run(session, 'cartoon style modeHelix tube sides 20')
run(session, 'sequence chain /A')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')