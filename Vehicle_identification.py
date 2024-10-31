vehicles = {
        # VIN: [year, manufacturer, model, color, eng_design, eng_displace]
        "1J4GL48K4UF993861": [2002, "Jeep", "Liberty", "blue", "V6", 3.7],
        "1YVGF22C8AN381568": [2002, "Mazda", "626", "white", "I4", 2.0],
        "WP0AA0926HG410293": [1987, "Porsche", "924S", "red", "I4", 2.5],
        "5TDZA23CXTU102983": [2006, "Toyota", "Sienna", "gold", "V6", 3.3],
        "1GKKVRED5ZL382610": [2011, "GMC", "Acadia", "charcoal", "V6", 3.5],
        "2T3BF4DV9QR146782": [2012, "Toyota", "RAV 4", "green", "I4", 2.5]
        }
def vehicle_info(vin):
        print('Car info: ')
        print(f'year: {vin[0]}')
        print(f'Manufactured: {vin[1]}')
        print(f'Model: {vin[2]}')
        print(f'Color: {vin[3]}')
        print(f'Eng_design: {vin[4]}')
        print(f'Eng_displace: {vin[5]}')
def main():
        vin = input('Write the VIN of the car: ')
        vin2 = vehicles[vin]
        if vin in vehicles:
                vehicle_info(vin2)
        else:
                print('VIN not found')
        
main()