# -*- coding: utf-8 -*-
#
# ------------------------------------------------------------
#  Copyright (c) 2019 Allrisk, a.s.
#  This software is the proprietary information of Allrisk, a.s.
#  All Right Reserved.
#  ------------------------------------------------------------
#

def checkValidRC(rc):
    '''
    Overi zda je plate RC
    Delka RC musi byt v <9, 10>
    Algoritmus:
    Vypocita se zbytek po deleni prvnich 9 cislic a cisla 11
     - je-li zbytek 10, musi byt posledni cislo 0
     - jinak musi byt posledni cislice rovna zbytku
    Pokud nesplnuje, neni validni RC
    :param rc: rodne cislo
    :type rc: string (int)
    :rtype: bool, str
    '''
    msg_no_valid = 'Zadane RC neni platne. Neodpovida algoritmu ministerstva vnitra'

    "Kontrola, zda se jedna o cislo a nejsou nepovolene znaky"
    try:
        int(rc)
    except:
        return False, 'Zadane RC neni platne. Nesmi se vyskytovat znaky jine nez 0-9'

    if len(str(rc)) > 10 or len(str(rc)) < 9:
        return False, 'Zadane RC neni platne. Pocet cislic musi byt 9 az 10'

    "Pokud jsou posledni 4 cisla 9999, 9998, ... tak nekontroluju na delitelnost 11. Jedna se pravd. o cizince"
    if len(str(rc)) == 10:
        if str(rc)[6:9] == '999':
            return True, None

    "Kontroluji algoritmem delitelnosti 11"
    last_digit = int(str(rc)[len(str(rc)) - 1:])
    if int(str(rc)[:9]) % 11 == 10:
        if last_digit == 0:
            return True, None
        else:
            return False, msg_no_valid
    else:
        if last_digit == (int(str(rc)[:9]) % 11):
            return True, None
        else:
            return False, msg_no_valid

    return False, msg_no_valid
