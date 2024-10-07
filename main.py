def inverse_lettres():
    phrase= input('Ecris une phrase ! :')
    mots = phrase.split()
    mots_inverses=[mot[::-1] for mot in mots]
    phrase_inversee = ' '.join(mots_inverses)
    return phrase_inversee
print(inverse_lettres())
