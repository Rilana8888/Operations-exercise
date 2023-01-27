# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action (weather, time_of_day, cows_milking_status, location_of_the_cows, season, slurry_tank, grass_status):
    if location_of_the_cows == 'pasture' and weather == 'rainy' or location_of_the_cows == 'pasture' and time_of_day == 'night':
        return 'take cows to cowshed'
    elif cows_milking_status and location_of_the_cows == 'cowshed':
        return 'milk cows'
    elif cows_milking_status and location_of_the_cows == 'pasture':
        return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
    elif weather == 'rainy' and location_of_the_cows == 'cowshed' and slurry_tank or weather == 'neutral' and location_of_the_cows == 'cowshed' and slurry_tank:
        return 'fertilize pasture'
    elif slurry_tank and weather == 'rainy' and location_of_the_cows == 'pasture' or slurry_tank and weather == 'neutral' and location_of_the_cows == 'pasture':
        return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'
    elif grass_status and season == 'spring' and weather == 'sunny' and location_of_the_cows == 'cowshed':
        return 'mow grass'
    elif grass_status and season == 'spring' and weather == 'sunny' and location_of_the_cows == 'pasture':
        return  'take cows to cowshed\nmow grass\ntake cows back to pasture'
    else: return'wait' 
    
    
print (farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))        



