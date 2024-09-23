# 26-mer stem-loop RNA

from chimerax.core.commands import run
run(session, 'open 6YMC')
run(session, 'hide s')
run(session, 'show a')
run(session, 'show c')
run(session, 'style stick')
run(session, 'color sequential palette PuBu')
run(session, 'nucleotides stubs')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')