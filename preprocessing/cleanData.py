
import pandas as pd
import pprint

def cleanData(path):
    # Define data path
    # path = "./timetables.csv"

    # Read data from local file
    df = pd.read_csv(path,sep="\t")
    
    print(df)
    # Get all locations
    traj = list(df["trajet"])
    
    # Origins array
    origin = []

    # Destination array
    destination = []

    # Feed origin and destination arrays
    for i in traj:
        splitted = i.split(" - ")
        origin.append(splitted[0].replace("Gare de ","").replace("Gare du ",""))
        destination.append(splitted[len(splitted)-1].replace("Gare de ","").replace("Gare du ",""))


    # Final dataframe
    endDF = pd.DataFrame()
    endDF["origin"] = origin
    endDF["destination"] = destination
    endDF["length"] = list(df["duree"])

    endDF.to_csv("data/clean_timetables.csv",index=False)


def csvToMatrix(path):
    from scipy.sparse import csr_matrix
    import numpy as np

    # Get data
    df = pd.read_csv(path)

    # Get all unique train station name
    unique_gares = list(set(np.concatenate((list(df["destination"]), list(df["origin"])), axis=None)))

    # Indexes for each train station
    indexes_gares = list(range(0,len(unique_gares)))

    print(unique_gares)

    print(indexes_gares)

    print(df)
    # Replace every train station name with its index in the dataframe
    df.replace(unique_gares,indexes_gares,inplace=True)

    df.dropna(inplace=True)

    df = df.astype("int64")

    # Debugg - Association station name -> index
    # for i in range(0,len(unique_gares)):
    #     print("{} -> {}".format(unique_gares[i],indexes_gares[i]))
    
    # Set up for the matrix
    data = np.array(list(df["length"]))
    row = np.array(list(df["origin"]))
    col = np.array(list(df["destination"]))

    # Debugg - see set up arrays
    print(data,row,col)

    # Matrix construction
    matrix = csr_matrix((data, (row,col)))

    # Export ids and length to csv
    df.to_csv("data/matricable_timetables.csv",index=False)

    # Export indexes
    indexes = pd.DataFrame()
    indexes["unique_gares"] = unique_gares
    indexes["indexes_gares"] = indexes_gares
    indexes.to_csv("data/matrixIndexes.csv",index=False)

    
    return matrix

# Calling cleanData()
cleanData("data/nonan_timetables.csv")

# Calling csvToMatrix()
matrix = csvToMatrix("data/clean_timetables.csv")
print(matrix.toarray())
print(matrix)
print(matrix.shape)