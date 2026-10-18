import pandas as pd

def create_series():
    lst = [1,2,3,4,5,6]
    s1 = pd.Series(lst)
    print(s1)


def main()-> None:
    create_series()



if __name__=="__main__":
    main()

