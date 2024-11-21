import csv
def read_csv(file_name):
    mortalkombat = {}
    
    with open(file_name, mode = 'r', newline = '') as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            year = row[0]
            fatalities = row[1]
            injuries = row[2]
            crashes = row[3]
            fatal_crashes = row [4]
            distraction_affected_fatal_crashes = row[5]
            fatal_crashes_involving_cell_phone_use = row [6]
            fatal_crashes_involving_excessive_speed = row[7]
            fatal_Crashes_while_driving_under_the_influence = row[8]
            fatal_Crashes_involving_fatigue_or_illness = row[9]
            mortalkombat[year] = [fatalities, injuries, crashes, fatal_crashes, distraction_affected_fatal_crashes, fatal_crashes_involving_cell_phone_use, fatal_crashes_involving_excessive_speed, fatal_Crashes_while_driving_under_the_influence, fatal_Crashes_involving_fatigue_or_illness]
        return mortalkombat

def display_info(year_info):
        if year_info:
            print("Menu:")
            print("1. Fatalities")
            print("2. Injuries")
            print("3. Crashes")
            print('4. Fatal Crashes')
            print("5. Distraction affected fatal crashes")
            print("6. Fatal crashes involving cell phone use")
            print('7. Fatal crashes involving excessive speed')
            print('8. Fatal Crashes while driving under the influence')
            print('9. Fatal Crashes involving fatigue or illness:')
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                print(f'Fatalities: {year_info[0]}')
            elif choice == '2':
                print(f'Injuries: {year_info[1]}')
            elif choice == '3':
                print(f'Crashes: {year_info[2]}')
            elif choice == '4':            
                print(f'Fatal crashes: {year_info[3]}')
            elif choice == '5':  
                print(f'Distraction affected fatal crashes: {year_info[4]}')
            elif choice =='6':           
                print(f'Fatal crashes involving cell phone use: {year_info [5]}')
            elif choice == '7':
                print(f'Fatal crashes involving excessive speed: {year_info[6]}')
            elif choice == '8':
                print(f'Fatal Crashes while driving under the influence: {year_info[7]}')
            elif choice =='9':
                print(f'Fatal Crashes involving fatigue or illness: {year_info[8]}')
            else:
                print('Invalid choice')
        else:
            print('Year not found')
def main():
    file_name = r'C:\Users\Labinfo10\Documents\Quebec Martinez\archivos de chamba\accidents.csv'
    
    crashes = read_csv(file_name) 
    year = input('Write the year: ')
    year_info = crashes.get(year)
    
    display_info(year_info)
        
main()