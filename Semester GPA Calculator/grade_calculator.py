import pandas as pd

def gpa_calculator():
    
    letter_to_gpa = {'A+': 4.33, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D': 1.0, 'F': 0.0, 'P': 0.0} 
    df = pd.read_csv('grades.txt', sep= " ", header=None, names = ["Course Name", "Credits", "Grade"])
    df["Grade Value"] = [letter_to_gpa[c] for c in df['Grade']]
   # df["Credits"] = pd.to_numeric(df["Credits"])
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    df["Weighted"] = df["Grade Value"] * df["Credits"]
    gpa = round(sum(df["Weighted"])/(sum(df["Credits"])),2)
   
    print()
    print(df)
    print()
    print('GPA: ', gpa)

    with open('output.txt','w') as outfile:
        df.to_string(outfile, columns=df.columns)
        outfile.write('\n\n' + str(gpa))
        
if __name__ == "__main__":
    gpa_calculator()