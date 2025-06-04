import pandas as pd


def main():


    # Setting the relative path to a variable to be clear
    url = "/Users/bryanmejia/Desktop/CS Personal Projects/Python/Section 2 - Getting Familiar With Python/Uploading-and-Processing-Data/cars-sample35.txt"


    # Loading in the file using pandas
    df = pd.read_csv(url, header = None) # header = None treats first row as data


    # Separate the file by columns 
    df.columns = ['Price', 'Maintenance Cost', 'Number of Doors', 'Number of Passengers', 'Luggage Capacity',
                'Safety Rating', 'Classification of Vehicle'] 


    # From created columns, store values into a list
    Prices = df['Price'].tolist()
    Maintenance_Cost = df['Maintenance Cost'].tolist()
    Number_of_Doors = df['Number of Doors'].tolist()
    Number_of_Passengers = df['Number of Passengers'].tolist()
    Luggage_Capacity = df['Luggage Capacity'].tolist()
    Safety_Rating = df['Safety Rating'].tolist()
    Classification_of_Vehicle = df['Classification of Vehicle'].tolist()


    med_Prices = []
    med_Num_of_Passengers = []
    automobiles_high_low = []


    for i in range(len(Prices)):
        if Prices[i] == 'med':
            med_Prices.append(Prices[i])
            med_Num_of_Passengers.append(Number_of_Passengers[i])
        if Prices[i] == 'high' and Maintenance_Cost[i] != 'low':
            automobiles_high_low.append(i)


    med_price_automobiles = [i for i in range(len(Prices)) if Prices[i] == 'med']
    num_of_passengers_2 = [Number_of_Passengers[i] for i in range(len(Prices)) if Prices[i] == 'med']
    automobiles_high_low2 = [i for i in range(len(Prices)) if Prices[i] == 'high' and Maintenance_Cost[i] != 'low']


    nlist = [[1,2,3], ['A','B','C'], [4,5], ['D','E']]  
    extracted_nlist = [i for n in nlist for i in n]


    print(f'Question 3 - {med_Prices}')
    print(f'Question 4 - {med_Num_of_Passengers}')
    print(f'Question 5 - {automobiles_high_low}')
    print(f'Question 6 - {med_price_automobiles}')
    print(f'Question 7 - {num_of_passengers_2}')
    print(f'Question 8 - {automobiles_high_low2}')
    print(f'Question 9 - {extracted_nlist}')

if __name__ == '__main__':
    main()

    
