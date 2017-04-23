label packed_a_snack(player):
    player.name "Ouch that last battle really tired me out. Good thing I packed a snack."
    $ player.heal(60)
    "[player.name] gained 60 hp."
    return
