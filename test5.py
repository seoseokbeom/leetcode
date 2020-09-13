def solution(cards):
    dealerMax = 0
    dealerLow = 0
    meMax = 0
    meLow = 0
    i = 0
    mf = 0
    df = 0
    showcard = 0
    result = 0
    while(i < len(cards)):
       if mf == 0 and cards[i] == 1:
            meLow += 1
            meMax += 11
        else:
            meLow += cards[i]
            meMax += cards[i]
        i += 1
        if df == 0 and cards[i] == 1:
            dealerMax = 11
            dealerLow = 1
        else:
            dealerMax += cards[i]
            dealerLow += cards[i]
        i += 1
        #
        if mf == 0 and cards[i] == 1:
            meLow += 1
            meMax += 11
        else:
            meLow += cards[i]
            meMax += cards[i]
        i += 1
        showcard = cards[i]
        if df == 0 and cards[i] == 1:
            dealerMax = 11
            dealerLow = 1
        else:
            dealerMax += cards[i]
            dealerLow += cards[i]
        i += 1
        if meMax > 21 and meLow > 21:
            result -= 2
        elif meMax == 21:
            if dealerMax != 21:
                result += 3
        while (showcard == 1 or showcard >= 7) and (meLow >= 17 or 21 >= meMax >= 17):
            meLow += cards[i]
            meMax += cards[i]
            i+=1
            if meLow >21:
                result -= 2
                break
        while 2 <=showcard<=3 and meLow<12 :
            meLow += cards[i]
            meMax += cards[i]
            i+=1

        # 6. 플레이어가 더이상 카드를 받지 않으면 딜러 앞의 뒤집어놓은 카드를 공개한 후, 딜러의 카드 합이 17 이상이 될 때까지 계속해서 딜러가 카드를 한 장씩 받는다.
        while dealerLow<17:
            if dealerMax==21 or dealerLow==21:
                result-=2
            dealerMax+=cards[i]
            dealerLow+=cards[i]
            i+=1
        # 7. 승패를 가린다. 카드 합이 21에 더 가까운 사람이 이기며, 카드 합이 서로 같으면 비긴다.
        if 
             
