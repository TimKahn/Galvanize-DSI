import pandas as pd

if __name__ == '__main__':
    data = []
    columns = ['victim_race', 'yes', 'no']
    data.append(['white', 45, 85])
    data.append(['black', 14, 218])
    df = pd.DataFrame(data = data, columns = columns)
    df.set_index(df['victim_race'], inplace=True)
    del df['victim_race']
    print(df)

    rows, cols = df.shape[0], df.shape[1]
    grand_tot = df.sum().sum()
    row_tot = df.sum
