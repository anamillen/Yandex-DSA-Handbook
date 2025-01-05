"""
Рассмотрим задачу менеджера рекламного агентства.

Есть n билбордов, на которых можно размещать рекламные объявления. Планирование размещения проводится на w недель вперед. 
Модель размещения рекламы разрешает сохранить одно и тоже объявление несколько недель на одном билборде, 
перенести объявление на следующей неделе на другой билборд. Размещать одно объявление на разных, 
не обязательно последовательных, неделях будущего периода. 
Однако на одной неделе не может быть рекламных объявлений от одного рекламодателя на разных билбордах.

k рекламодателей хотят разместить рекламу. Заявки подают рекламодатели в формате аукциона, но не знают заявок конкурентов. 
Известно, что i-й рекламодатель подал заявку на размещение своей рекламы максимум на wi​ недель с оплатой ci​ за каждую неделю размещения, 
т.е. рекламное объявление i-го рекламодателя может быть размещено от 0 до wi​ в течение периода 
(при размещении рекламы в течение m недель оплата за нее составит m⋅ci​).

Менеджеру нужно выбрать, в какие недели и на каких билбордах разместить рекламу рекламодателей.

Требуется максимизировать прибыль от размещения рекламы.
"""

def max_profit_billboards(n_boards, n_bids, max_weeks, bids, periods):
    """Returns the max profit from advertising placements"""
    total = 0
    i_week = 0
    offers = [[bids[i], periods[i]] for i in range(n_bids)]
    # we look into every week
    while len(bids)!=0 and i_week<max_weeks:     
        best_offers = sorted(offers, key=(lambda x: x[0]), reverse=True)
        # we consider every billboard
        i_board = 0
        while i_board<n_boards and i_board<len(best_offers):
            total += best_offers[i_board][0]
            best_offers[i_board][1] = best_offers[i_board][1] - 1      # we substract 1 week  
            # if the offer is no longer valid then
            if best_offers[i_board][1]==0:   
                offers.pop(offers.index(best_offers[i_board]))
            i_board+=1
            # from here on out we've either exhausted all the offers (i_board>=len(best_offers))
            # or we have no more empty billboards (i_board>=n_boards)
        i_week+=1
    # from here on out there are either no ad offers (len(bids)==0)
    # or the planning period has ended (i>=max_weeks)
    return total

# main program
n_billboards, n_offers, n_weeks = [int(x) for x in input().split()]
bids = []
periods = []
for _ in range(n_offers):
    bid, period = [int(x) for x in input().split()]
    bids.append(bid)
    periods.append(period)
print(max_profit_billboards(n_billboards, n_offers, n_weeks, bids, periods))



