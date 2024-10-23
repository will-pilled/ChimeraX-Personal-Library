from chimerax.core.commands import run
run(session, 'open 1A7F')
run(session, 'show c')
run(session, 'show a')
run(session, 'style ball')
run(session, 'size ballscale 0.18')
run(session, 'color sequential palette PuBu')
run(session, 'show s')
run(session, 'lighting gentle')
run(session, 'transparency 90 s')
run(session, 'sequence chain all')
run(session, 'view orient')
run(session, 'ui tool show "Side View"')
run(session, 'graphics silhouettes true')
run(session, 'set bgColor #ffffff00')