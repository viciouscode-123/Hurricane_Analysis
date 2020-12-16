# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#%%
# write your update damages function here:

def convert_millions(millions):
    if '.' in millions:
        amount_in_millions = millions.replace('.', '') + '00000'
    else:
        amount_in_millions = millions + '000000'
    return amount_in_millions

def convert_billions(billions):
    if '.' in billions:
        amount_in_billions = billions.replace('.', '') + '00000000'
    else:
        amount_in_billions = billions + '000000000'      
    return amount_in_billions

def convert_unit_to_integer(damage_with_unit):
    if damage_with_unit.endswith('M'):
        damage_amount = convert_millions(damage_with_unit.rstrip('M'))
    else:
        damage_amount = convert_billions(damage_with_unit.rstrip('B'))   
    return damage_amount

def convert_damage_records(damages):
       
    converted_damage_records = []    
    for record in damages:
        if record == 'Damages not recorded':
            converted_damage_records.append(record)
        else:
            converted_damage_records.append(float(convert_unit_to_integer(record)))   
    return converted_damage_records

# print(convert_damage_records(damages))
#%%
# write your construct hurricane dictionary function here:
def update_details(hurricane, hurricanes_list):
    hurricanes_list.append({
        "Name": names[hurricane],
        "Month": months[hurricane],
        "Year": years[hurricane],
        "Max Sustained Wind": max_sustained_winds[hurricane],
        "Areas Affected": areas_affected[hurricane],
        "Damage": damages[hurricane],
        "Deaths": deaths[hurricane]
        })        

def store_each_hurricane_data():
    list_of_hurricanes = []
    for hurricane in range(len(names)):
        update_details(hurricane, list_of_hurricanes)
    return list_of_hurricanes

def create_hurricane_database(): 
    hurricane_database = {key:value for key, value in 
                          zip(names, store_each_hurricane_data())}    
    return hurricane_database

print(create_hurricane_database())
#%%
# write your construct hurricane by year dictionary function here:

def get_years(hurricanes):
    """Get a list of years when the hurricanes occured"""
    years = []
    for hurricane in hurricanes:        
        if hurricanes.get(hurricane).get('Year') not in years:
            years.append(hurricanes.get(hurricane).get('Year')) 
    return years
    
def hurricanes_by_year(hurricanes):
    """Arrange the input hurricane dictionary where the year of hurricane 
    is the key of returned dictionary.
    e.g. {2016: {'Cuba': ....}}"""
    hurricanes_by_year = {}
    for year in get_years(hurricanes):
        hurricanes_in_year = []
        for hurricane in hurricanes:
            if hurricanes.get(hurricane).get('Year') == year:
                 hurricanes_in_year.append(hurricanes.get(hurricane))                 
        hurricanes_by_year.update({year:hurricanes_in_year})        
    return hurricanes_by_year

#%%
# write your count affected areas function here:
def create_affected_areas_dict(hurricanes: dict):
    """ Takes in an input of hurricanes. It uses the key 'Affected areas' 
        of each hurricane and generates a new dict with unique key values 
        for each area found with a value of 0.
        The output dictionary will be a cummulation of all areas over all 
        hurricanes from the input.
        e.g.
                                 
        Output: {'Central America': 0, 'Mexico', 0 'Cuba': 0, ....}
    """
    new_dict={}
    for hurricane in hurricanes:
        for affected_area in hurricanes.get(hurricane).get('Areas Affected'):
            if affected_area not in new_dict.keys():
                new_dict.update({affected_area:0})
    return new_dict
         
def count_affected_areas(hurricanes: dict):
    counts_dict = create_affected_areas_dict(hurricanes)

    for hurricane in hurricanes:
        for affected_area in hurricanes.get(hurricane).get('Areas Affected'):
            counts_dict.update({affected_area: counts_dict.get(affected_area) + 1})
    return counts_dict

print(count_affected_areas(create_hurricane_database()))
#%%
# write your find most affected area function here:
def get_most_affected_area(hurricanes: dict):
    counts = count_affected_areas(hurricanes).items()
    most_affected = next(iter(counts))
    return most_affected

print(get_most_affected_area(create_hurricane_database()))
#%%
# write your greatest number of deaths function here:
def greatest_deaths(hurricanes: dict):
    max_deaths = 0
    deadliest_hurricane = {}
    for hurricane in hurricanes:
        if max_deaths < hurricanes.get(hurricane).get('Deaths'):
            max_deaths = hurricanes.get(hurricane).get('Deaths')          
            deadliest_hurricane = hurricanes.get(hurricane)
    return max_deaths, deadliest_hurricane

# greatest_deaths(create_hurricane_database())

#%%
# write your catgeorize by mortality function here:
def assign_mortality_rate(deaths):
    if deaths == 0:
        return 0
    elif deaths > 0 and deaths <= 100:
        return 1
    elif deaths > 100 and deaths <= 500:
        return 2
    elif deaths > 500 and deaths <= 1000:
        return 3
    else:
        return 4    

def mortality_rate(hurricanes: dict):
    hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[]}
    for hurricane in hurricanes:
        mortality_rate = assign_mortality_rate(hurricanes.get(hurricane).get('Deaths'))
        hurricanes_by_mortality.get(mortality_rate).append(hurricanes.get(hurricane))
    return hurricanes_by_mortality

#%%
# write your greatest damage function here:
def greatest_damage(hurricanes: dict):
    max_damage = 0
    for hurricane in hurricanes:
       if hurricanes.get(hurricane).get('Damage') != 'Damages not recorded':
           damage = int(convert_unit_to_integer(hurricanes.get(hurricane).get('Damage')))
           if damage > max_damage:
               max_damage = damage
               max_damage_hurr = hurricane
    return max_damage, max_damage_hurr
# print(greatest_damage(create_hurricane_database()))

#%%
# write your catgeorize by damage function here:

def assign_damage_rate(damage: int):
    if damage == 0:
        return 0
    elif damage > 0 and damage <= 100000000:
        return 1
    elif damage > 100000000 and damage <= 1000000000:
        return 2
    elif damage > 1000000000 and damage <= 10000000000:
        return 3
    else:
        return 4  
    
def categorized_by_damage(hurricanes: dict):
    hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[]}
    for hurricane in hurricanes:
       if hurricanes.get(hurricane).get('Damage') != 'Damages not recorded':
           damage = int(convert_unit_to_integer(hurricanes.get(hurricane).get('Damage')))
       else:
           damage = 0           
       damage_rate = assign_damage_rate(damage) 
       hurricanes_by_damage.get(damage_rate).append(hurricanes.get(hurricane))             
    return hurricanes_by_damage

print(categorized_by_damage(create_hurricane_database()))