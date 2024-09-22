# Cyclopentane peptide nucleic acid in complex with DNA

from chimerax.core.commands import run
run(session, 'open 7KZL')
run(session, 'show c')
run(session, 'show a')
run(session, 'hide s')
run(session, 'style stick')
run(session, 'transparency 35 atoms')
run(session, 'color sequential palette Reds-5')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')
