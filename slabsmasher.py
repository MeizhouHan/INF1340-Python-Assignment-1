VHS_GRACE_DAYS = 7
DVD_GRACE_DAYS = 5
GAME_GRACE_DAYS = 2
VHS_FINE = 0.99
VHS_REWIND_FEE = 1.99
DVD_FINE = 2.99
GAME_FINE = 5.99
VHS_COST = 11.99
DVD_COST = 14.99
GAME_COST = 23.99




def get_late_days(total_days:int,grace_period:int)->int:
    """Return the number of days the item is late, given total_days an item has 
    been checked out and the grace_period. Return 0 if the item is not late.
    >>>get_late_days(9,7)
    2
    >>>get_late_days(3,5)
    0
    """
    if total_days>grace_period:
        return total_days-grace_period
    else:
        return 0
    




def get_total_fine(daily_fine:float, days_late:int,replacement_cost:float,
                   rewind_fee:bool)->float:
    """Return the total fine for the item, given the daily_fine and days_late, 
    including a rewind_fee if necessary. If the replacement_cost is lower than 
    the total lateness fee, it is returned instead, and the rewind fee does not apply.
    >>> get_total_fine(0.99, 0, 11.99, False)
    0.0
    >>> get_total_fine(0.99, 4, 11.99, True)
    5.95
    >>> get_total_fine(0.99, 12, 11.99, True)
    13.87
    >>> get_total_fine(5.99, 20, 23.99, False)
    23.99
    """
    fine=daily_fine * days_late
    if fine <= replacement_cost and rewind_fee==True:
        return round((fine + VHS_REWIND_FEE),2)
    elif fine<=replacement_cost and rewind_fee == False:
        return round(fine,2)
    else:
        return replacement_cost
   




def show_item_name(item_code:str)->str:
    """Return the item type, according to the item_code.
    >>>show_item_name('v')
    'VHS tape'
    >>>show_item_name('d')
    'DVD'
    """
    if item_code=='v':
        return'VHS tape'
    elif item_code=='d':
        return'DVD'
    elif item_code=='g':
        return'Video game'    




def show_late_status(item_code:str,days_late:int,rewind_fee:bool)->str:
    """ Returns lateness status and whether it needs rewinding, given the 
    item_code, days_late and whether it needs a rewind_fee.
    >>> show_late_status('v', 3, True)
    'VHS tape returned 3 days late, needs rewind!'
    >>> show_late_status('v', 0, True)
    VHS tape returned on time, needs rewind!
    >>> show_late_status('g', 0, False)
    Video game returned on time!
    >>> show_late_status('d', 1, False)
    DVD returned 1 day late!
    """
    if item_code=='v':
        if days_late>1:
            return show_item_name(item_code) + ' returned '+ str(days_late)  + ' days late, needs rewind!'
        if days_late==1:
            return show_item_name(item_code) + ' returned '+ str(days_late)  + ' day late, needs rewind!'
        if days_late==0:
            return show_item_name(item_code) + ' returned on time, needs rewind!'      
    elif  rewind_fee==False:
        if days_late>1:
            return show_item_name(item_code) + ' returned '+ str(days_late)  + ' days late!'
        if days_late==1:
            return show_item_name(item_code) + ' returned '+ str(days_late)  + ' day late!'
        if days_late==0:
            return show_item_name(item_code) + ' returned on time!'              



def show_fine(total_fine:float)->str:
    """Return a human-readable string indicating the total_fine. If no fine 
    is owed, it returns "".
    >>> show_fine(23.99)
    'TOTAL FINE: $23.99'
    >>> show_fine(12.45633)
    'TOTAL FINE: $12.46'
    >>> show_fine(0)
    ''
    >>> show_fine(10)
    'TOTAL FINE: $10'    
    """
    if total_fine>0:
        return 'TOTAL FINE: $' + str(round(total_fine,2))
    else:
        return ''




def fee_assessment(item_code: str, total_days: int, rewind_fee: bool) -> str:
    """Precondition: 
    item_code is 'v', 'd', or 'g', total_days is a positive integer.
    
    Given an item of type item_code that's been out for total_days and 
    whether it's been assessed a rewind_fee, return a human-readable string 
    describing the item's lateness status and what fines, if any, it has
    incurred.
    
    >>> fee_assessment('v', 12, True)
    'VHS tape returned 5 days late, needs rewind!\nTOTAL FINE: $6.94'
    >>> fee_assessment('g', 2, False)
    'Video game returned on time!\n'
    """
    if item_code=="v":
        grace_period=VHS_GRACE_DAYS
    elif item_code=="d":
        grace_period=DVD_GRACE_DAYS
    elif item_code=="g":
        grace_period=GAME_GRACE_DAYS    
    days_late=get_late_days(total_days,grace_period)
    
    
    if item_code=="v":
        daily_fine=VHS_FINE
        replacement_cost=VHS_COST
    elif item_code=="d":
        daily_fine=DVD_FINE
        replacement_cost=DVD_COST
    elif item_code=="g":
        daily_fine=GAME_FINE
        replacement_cost=GAME_COST        
    total_fine=get_total_fine(daily_fine, days_late,replacement_cost,rewind_fee)
    return show_late_status(item_code, days_late, rewind_fee) + \
           "\n" + show_fine(total_fine)