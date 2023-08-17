class GmError(Exception):
    def __init__(self, err_code, err_str, data=None):
        self.err_code = int(err_code)
        self.err_str = str(err_str)
        self.data = data
        

    def __str__(self):
        return self.err_str
    

if __name__ == "__main__":
    e1 = GmError(1, "dddddd6345634534hdfgh")
    print(str(e1))
    pass
