# Level 1 Wheat Field output (change if you have any bonuses)
BASE_WHEAT = 2;

# Level 1 Farm worker bonus (change if you have any bonuses)
BASE_FARM = 2;


def main():
    tiles_total = int(input("Enter number of available tiles: "));
    wheat_field_levels = int(input("Enter the average level of your wheat fields: "));
    farm_levels = int(input("Enter the average level of your farms: "));

    # Optimal split lies between +1/-1 of half the number of tiles
    mid_range = tiles_total // 2 if tiles_total % 2 == 0 else (tiles_total + 1) // 2

    upper_range = mid_range + 1;
    lower_range = mid_range - 1;

    # Wheat output on a farm with upper_range number of farms
    upper_range_wheat_val = (((BASE_FARM * farm_levels) * upper_range) + 1) * (BASE_WHEAT * wheat_field_levels);

    # Wheat output on a farm with mid_range number of farms
    mid_range_wheat_val = (((BASE_FARM * farm_levels) * mid_range) + 1) * (BASE_WHEAT * wheat_field_levels);

    # Wheat output on a farm with lower_range number of farms
    lower_range_wheat_val = (((BASE_FARM * farm_levels) * lower_range) + 1) * (BASE_WHEAT * wheat_field_levels);

    # Total wheat output for each number of farms
    upper_total = upper_range_wheat_val * (tiles_total - upper_range);
    mid_total = mid_range_wheat_val * (tiles_total - mid_range);
    lower_total = lower_range_wheat_val * (tiles_total - lower_range);

    print();
    print(f"{upper_range} farms: +{upper_total} per sec");
    print(f"{mid_range} farms: +{mid_total} per sec");                  
    print(f"{lower_range} farms: +{lower_total} per sec");
    print();

    options = [lower_range, mid_range, upper_range];
    optimal = getOptimal(upper_total, mid_total, lower_total);

    print();
    print(f"Optimal number of farms: {options[optimal]}");
    print();

def getOptimal(upper, mid, lower):
    '''
    Returns 2 for upper, 1 for mid, 0 for lower
    '''
    highest = max(upper, mid, lower);
    optimal = 2 if highest == upper else 1 if highest == mid else 0;
    
    return optimal;

    

if __name__ == "__main__":
    main();
    while True:
        if (input("Again? Y/N\n").lower() == 'y'):
            main();
        else:
            break;
