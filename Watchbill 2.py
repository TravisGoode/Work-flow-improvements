import random
import calendar
from datetime import datetime




#read the red text to help calibrate the generator
#After inputing the names when you run this program it'll make your watchbill accounting for the proper month/day
#however many months out you need and account for the current date
#look at your date and time bar on your computer and set to to the correct day/year now


 
#start of informative text
def generate_watchbill(nco_names, runner_names, num_months=1):

    if not nco_names or not runner_names:
        raise ValueError("Please enter names, the list is empty.")

    if not isinstance(num_months, int) or num_months <= 0:
        raise ValueError("Negitive values for the month(s) are not accepted.")

    
    watchbill = []

    #pulls the date and time to account for the current month and day. 
    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year
    current_day = current_date.day


    last_nco_day = {name: -2 for name in nco_names}
    last_runner_day = {name: -2 for name in runner_names}


    #creates random list pool for each day
    all_nco_names = nco_names[:]
    all_runner_names = runner_names[:]
    random.shuffle(all_runner_names)
    random.shuffle(all_nco_names)
    paired = set()
    
    # accounts for the months
    for month_offset in range(num_months):
        month = (current_month + month_offset - 1) % 12 + 1
        year = current_year + ((current_month + month_offset - 1) // 12)
        
        
        watchbill.append(f"Month {month}:")

        
        
        num_days = calendar.monthrange(year, month)[1]
        start_day = current_day if month == current_month else 1



        #assigns daily roles
        for day in range(start_day, num_days + 1):

            if not all_nco_names:
                all_nco_names = nco_names[:] #refill list with names
                random.shuffle(all_nco_names) #reshuffle list

            
            if not all_runner_names:
                all_runner_names = runner_names[:]
                random.shuffle(all_runner_names)


            #ensure no repeating pairs
            nco_role = None
            runner_role = None
            for i in range(len(all_nco_names)):
                for j in range(len(all_runner_names)):
                    pair = (all_nco_names[i], all_runner_names[j])
                    if pair not in paired:
                        nco_role = all_nco_names.pop(i)
                        runner_role = all_runner_names.pop(j)
                        paired.add(pair)
                        last_nco_day[nco_role] = day
                        last_runner_day[runner_role] = day
                        break
                if nco_role and runner_role:
                    break



            #restart if unable to make new pair
            if not nco_role or not runner_role[:]:
                all_runner_names = runner_names[:]
                random.shuffle(all_nco_names)
                random.shuffle(all_runner_names)

                nco_role = all_nco_names.pop()
                runner_role = all_runner_names.pop()

                last_nco_day[nco_role] = day
                last_runner_day[runner_role] = day

               
            
            
            watchbill.append(f"Day {day}: {nco_role} (NCO) | {runner_role} (Runner)")
            


            
        watchbill.append("")

        
#end of imformative text 
    return watchbill


#we can start changing things here 



#input names inside the [] with "", format
try:
    
    nco_names = ["N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8", "N9", "N10", "N11", "N12", "N13", "N14", "N15", "N16", "N17", "N18", "N19", "N20", "N21", "N22", "N23", "N24", "N25", "N26", "N27", "N28", "N29", "N30"] #example names put your own with "",

    runner_names = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13", "R14", "R15", "R16", "R17", "R18", "R19", "R20", "R21", "R22", "R23", "R24", "R25", "R26", "R27", "R28", "R29", "R30"] #same as above must be "", format


    #change the "=3" to one more than the number of months you want to generate. 
    watchbill = generate_watchbill(nco_names, runner_names, num_months=3) 


    print("\nGenerated Watchbill:")

    for line in watchbill:
        print(line)
except ValueError as e:
    print(f"Error: {e}")

