# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action (weather, time_of_day, cows_milking_status, location_of_the_cows, season, slurry_tank, grass_status):
    if location_of_the_cows == 'pasture' and weather == 'rainy':
        print ('take cows to cowshed') 
    elif location_of_the_cows == 'pasture' and time_of_day == 'night':
        print ('take cows to cowshed')
    elif cows_milking_status and location_of_the_cows == 'pasture':
        print ('take cows to cowshed')
    elif slurry_tank and weather == 'rainy' and location_of_the_cows == 'pasture':
        print ('take cows to cowshed')
    elif slurry_tank and weather == 'neutral' and location_of_the_cows == 'pasture':
        print ('take cows to cowshed')
    elif grass_status and season == 'spring' and weather == 'sunny' and location_of_the_cows == 'pasture':
        print ('take cows to cowshed')
    if cows_milking_status and location_of_the_cows == 'cowshed':
        print ('milk cows')
    elif cows_milking_status and location_of_the_cows == 'pasture':
        print ('milk cows')
    if slurry_tank and location_of_the_cows == 'cowshed' and weather == 'rainy':
        print ('fertilize pasture')
    elif slurry_tank and location_of_the_cows == 'cowshed' and weather == 'neutral':
        print ('fertilize pasture')
    elif slurry_tank and location_of_the_cows == 'pasture' and weather == 'rainy':
        print ('fertilize pasture')
    elif slurry_tank and location_of_the_cows == 'pasture' and weather == 'neutral':
        print ('fertilize pasture')
    if grass_status and season == 'spring' and weather == 'sunny' and cows_milking_status == False and location_of_the_cows == 'cowshed':
        print ('mow grass')
    elif grass_status and season == 'spring' and weather == 'sunny' and cows_milking_status == False and location_of_the_cows == 'pasture':
        print ('mow grass')
    if cows_milking_status and location_of_the_cows == 'pasture':
        print ('take cows back to pasture')
    elif slurry_tank and weather == 'rainy' and location_of_the_cows == 'pasture':
        print ('take cows back to pasture')
    elif slurry_tank and weather == 'neutral' and location_of_the_cows == 'pasture':
        print ('take cows back to pasture')
    elif grass_status and season == 'spring' and weather == 'sunny' and location_of_the_cows == 'pasture':
        print ('take cows back to pasture')
    else: print ('wait') 
    
farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)        



