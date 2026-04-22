import pandas as pd
import matplotlib.pyplot as plt

result = None   


while(True):
    print("\nMain Menu")
    print("1. Fetch data")
    print("2. Dataframe Statistics")
    print("3. Display Records")
    print("4. Working on Records")
    print("5. Working on Columns")
    print("6. Search specific row/column")
    print("7. Data Visualization")
    print("8. Data analytics")
    print("9. Exit")

    ch=int(input("Enter your choice: "))

    
    if ch==1:
        try:
            result=pd.read_csv("results.csv",index_col=0)
            print("✅ Data loaded successfully!")
        except:
            print("❌ File not found! Keep results.csv in same folder.")

   
    elif result is None:
        print("⚠ Please fetch data first (Press 1)")
        continue

    
    elif ch==2:
        while(True):
            print("\nDataframe Statistics Menu")
            print("1. Display the Transpose")
            print("2. Display all column names")
            print("3. Display the indexes")
            print("4. Display the shape")
            print("5. Display the dimension")
            print("6. Display the data types of all columns")
            print("7. Display the size")
            print("8. Exit")

            ch2=int(input("Enter choice: "))

            if ch2==1:
                print(result.T)
            elif ch2==2:
                print(result.columns)
            elif ch2==3:
                print(result.index)
            elif ch2==4:
                print(result.shape)
            elif ch2==5:
                print(result.ndim)
            elif ch2==6:
                print(result.dtypes)
            elif ch2==7:
                print(result.size)
            elif ch2==8:
                break

    elif ch==3:
        while(True):
            print("\nDisplay Records Menu")
            print("1. Top 5 Records")
            print("2. Bottom 5 Records")
            print("3. Specific number of records from the top")
            print("4. Specific number of records from the bottom")
            print("5. Details of a specific Subject")
            print("6. Display details of all subjects")
            print("7. Exit")

            ch3=int(input("Enter choice: "))

            if ch3==1:
                print(result.head())
            elif ch3==2:
                print(result.tail())
            elif ch3==3:
                n=int(input("Enter number of records: "))
                print(result.head(n))
            elif ch3==4:
                n=int(input("Enter number of records: "))
                print(result.tail(n))
            elif ch3==5:
                st=input("Enter subject name: ")
                print(result.loc[st])
            elif ch3==6:
                print(result)
            elif ch3==7:
                break

    
    elif ch==7:
        plt.plot(result.index,result['highest'],marker='o')
        plt.title("SUBJECTWISE HIGHEST MARKS")
        plt.xlabel("SUBJECTS")
        plt.ylabel("HIGHEST MARKS")
        plt.xticks(rotation=30)
        plt.grid(True)
        plt.show()

   
    elif ch==8:
        m=result['average'].max()
        s=result.loc[result.average==m]
        print("Subject with maximum average marks:",s.index[0])

    elif ch==9:
        print("Program Closed.")
        break
