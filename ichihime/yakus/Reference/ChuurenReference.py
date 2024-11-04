from ichihime.enums import tile as _TL

MANZUREF = {
    (_TL.MAN1,): 3,
    (_TL.MAN2,): 1,
    (_TL.MAN3,): 1,
    (_TL.MAN4,): 1,
    (_TL.MAN5, _TL.MAN0): 1,
    (_TL.MAN6,): 1,
    (_TL.MAN7,): 1,
    (_TL.MAN8,): 1,
    (_TL.MAN9,): 3,
}

PINZUREF = {
    (_TL.PIN1,): 3,
    (_TL.PIN2,): 1,
    (_TL.PIN3,): 1,
    (_TL.PIN4,): 1,
    (_TL.PIN5, _TL.PIN0): 1,
    (_TL.PIN6,): 1,
    (_TL.PIN7,): 1,
    (_TL.PIN8,): 1,
    (_TL.PIN9,): 3,
}

SOUZUREF = {
    (_TL.SOU1,): 3,
    (_TL.SOU2,): 1,
    (_TL.SOU3,): 1,
    (_TL.SOU4,): 1,
    (_TL.SOU5, _TL.SOU0): 1,
    (_TL.SOU6,): 1,
    (_TL.SOU7,): 1,
    (_TL.SOU8,): 1,
    (_TL.SOU9,): 3,
}

CHUURENREF = MANZUREF, PINZUREF, SOUZUREF
