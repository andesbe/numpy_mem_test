
def read_parquet_files(path):
    """
    Read parquet files from a given path and declares a numpy array of the relevant size in order to avoid
    memory allocation during the loop.
    :param path: path to the parquet files
    :return: numpy array"""
    files = os.listdir(path)
    num_files = len(files)
    data_shape= pd.read_parquet(path + files[0]).shape
    data = np.zeros(data_shape)
    for i in range(num_files):
        data[i] = pd.read_parquet(path + files[i])
    return data