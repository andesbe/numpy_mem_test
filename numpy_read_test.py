#create a function that reads in all the parquet files in a directory, declare a numpy array with the same shape as the data, and then fill the array with the data and returns the array

def read_parquet_files(path):
    #get the list of all the files in the directory
    files = os.listdir(path)
    #get the number of files in the directory
    num_files = len(files)
    #get the shape of the data
    data_shape
    #create a numpy array with the same shape as the data
    data = np.zeros(data_shape)
    #loop through the files and fill the numpy array with the data
    for i in range(num_files):
        data[i] = pd.read_parquet(path + files[i])
    return data