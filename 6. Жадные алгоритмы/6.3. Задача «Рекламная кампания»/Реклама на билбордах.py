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
    i_offer = 0
    disponibility = n_boards*max_weeks
    offers =sorted(
        [[bids[i], periods[i]] for i in range(n_bids)], 
        key = (lambda x: x[0]),
        reverse = True
    )
    while disponibility>0 and i_offer<n_bids:
        available_weeks = min(disponibility, offers[i_offer][1])
        disponibility -= available_weeks
        total += available_weeks*offers[i_offer][0]
        i_offer += 1
    # from here on out we either have already created a plan for the entire period (disponibility==0)
    # or we have no more offers from advertisers (i_offer==n_bids)
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



