def main()-> None:
    empl_list= [450000,80000,60000,35000]

    increament = lambda salary : salary + ((salary*10)/100)

    revised_salary = list(map(increament, empl_list));
    print(revised_salary)




if __name__ == "__main__":
    main()