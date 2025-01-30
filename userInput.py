import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 
import database 


class InfoForm:
  def __init__(self, root):
    self.root = root 
    self.content_frame = tk.Frame(self.root)
    self.content_frame.grid(row=0, column=0, sticky="nsew")
 
    self.content_frame.grid_columnconfigure(0, weight=1, minsize=200)  
    self.content_frame.grid_columnconfigure(1, weight=1, minsize=200)   
    self.create_left_column() 
    self.create_right_column() 
    self.root.grid_rowconfigure(0, weight=1)
    self.root.grid_columnconfigure(0, weight=1)

  def create_left_column(self): 
        self.income = tk.Label(self.content_frame, text="Income Sources", font=('Arial', 25, "bold"))
        self.income.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.salaryLabel = tk.Label(self.content_frame, text="Main Salary", font=('Arial', 16))
        self.salaryLabel.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.salaryEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.salaryEntry.insert(0,"$")
        self.salaryEntry.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.salaryTwoLabel = tk.Label(self.content_frame, text="Secondary Salary", font=('Arial', 16))
        self.salaryTwoLabel.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        self.salaryTwoEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.salaryTwoEntry.insert(0,"$")
        self.salaryTwoEntry.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.sideIncomeLabel = tk.Label(self.content_frame, text="Additional Income", font=('Arial', 16))
        self.sideIncomeLabel.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.sideIncomeEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.sideIncomeEntry.insert(0,"$")
        self.sideIncomeEntry.grid(row=6, column=0, padx=10, pady=5, sticky="w")
 



  def create_right_column(self): 
        self.expenses = tk.Label(self.content_frame, text="Expenses", font=('Arial', 25, "bold"))
        self.expenses.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.housingLabel = tk.Label(self.content_frame, text="Rent/Mortgage + Utilities", font=('Arial', 16))
        self.housingLabel.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        self.housingEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.housingEntry.insert(0,"$")
        self.housingEntry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.groceryLabel = tk.Label(self.content_frame, text="Groceries", font=('Arial', 16))
        self.groceryLabel.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        
        self.groceryEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.groceryEntry.insert(0,"$")
        self.groceryEntry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.taxesLabel = tk.Label(self.content_frame, text="Taxes", font=('Arial', 16))
        self.taxesLabel.grid(row=5, column=1, padx=10, pady=10, sticky="w")
        
        self.taxesEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.taxesEntry.insert(0,"$")
        self.taxesEntry.grid(row=6, column=1, padx=10, pady=5, sticky="w") 

        self.healthcareLabel = tk.Label(self.content_frame, text="Health Care/Fitness", font=('Arial', 16))
        self.healthcareLabel.grid(row=9, column=1, padx=10, pady=10, sticky="w")
        
        self.healthcareEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.healthcareEntry.insert(0,"$")
        self.healthcareEntry.grid(row=10, column=1, padx=10, pady=5, sticky="w")

        self.entLabel = tk.Label(self.content_frame, text="Entertainment/Leisure", font=('Arial', 16))
        self.entLabel.grid(row=11, column=1, padx=10, pady=10, sticky="w")
        
        self.entEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.entEntry.insert(0,"$")
        self.entEntry.grid(row=12, column=1, padx=10, pady=5, sticky="w")

        self.childLabel = tk.Label(self.content_frame, text="Childcare", font=('Arial', 16))
        self.childLabel.grid(row=13, column=1, padx=10, pady=10, sticky="w")
        
        self.childEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.childEntry.insert(0,"$")
        self.childEntry.grid(row=14, column=1, padx=10, pady=5, sticky="w")

        self.debtLabel = tk.Label(self.content_frame, text="Debt Payments", font=('Arial', 16))
        self.debtLabel.grid(row=15, column=1, padx=10, pady=10, sticky="w")
        
        self.debtEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.debtEntry.insert(0,"$")
        self.debtEntry.grid(row=16, column=1, padx=10, pady=5, sticky="w")

        self.otherLabel = tk.Label(self.content_frame, text="Other", font=('Arial', 16))
        self.otherLabel.grid(row=17, column=1, padx=10, pady=10, sticky="w")
        
        self.otherEntry = tk.Entry(self.content_frame, font=('Arial', 16))
        self.otherEntry.insert(0,"$")
        self.otherEntry.grid(row=18, column=1, padx=10, pady=5, sticky="w")

        self.totalIncomeLabel = tk.Label(self.content_frame, text="Total Net Income", font=('Arial', 25))
        self.totalIncomeLabel.grid(row=19, column=1, padx=10, pady=10, sticky="w")
        
        self.totalIncomeEntry = tk.Entry(self.content_frame, state="readonly", font=('Arial', 16))
        self.totalIncomeEntry.insert(0,"$")
        self.totalIncomeEntry.grid(row=20, column=1, padx=10, pady=5, sticky="w")
        
        self.update_button = tk.Button(self.content_frame, text="Calculate", command=self.update_readonly_field)
        self.update_button.grid(row=21, column=1, pady=10)

        self.submit_button = tk.Button(self.content_frame, text="Submit", command=lambda:self.submit_data("submit"))
        self.submit_button.grid(row=9, column=1, pady=10)
 

  def update_readonly_field(self, event=None): 
        incomeEntries = [self.salaryEntry,self.salaryTwoEntry,self.sideIncomeEntry]
        expensesEntries = [self.otherEntry,self.debtEntry,self.childEntry,self.entEntry, self.healthcareEntry,  self.taxesEntry, self.groceryEntry, self.housingEntry]

        result = 0
        for x in incomeEntries:
          x.delete(0,1)
          result += int(x.get().replace(",",""))

        for x in expensesEntries:
          x.delete(0,1)
          result -= int(x.get().replace(",",""))
 
        self.totalIncomeEntry.config(state="normal") 
        self.totalIncomeEntry.delete(0, tk.END)  
        self.totalIncomeEntry.insert(0, '$')
        self.totalIncomeEntry.insert(1, result)  
        self.totalIncomeEntry.config(state="readonly")   


  def submit_data(self, type):
    print (type)
    try: 
        main_income = int(self.salaryEntry.get().replace("$", ""))
        secondary_income = int(self.salaryTwoEntry.get().replace("$", ""))
        side_income = int(self.sideIncomeEntry.get().replace("$", ""))
        housing = int(self.housingEntry.get().replace("$", ""))
        groceries = int(self.groceryEntry.get().replace("$", ""))
        taxes = int(self.taxesEntry.get().replace("$", ""))
        healthcare = int(self.healthcareEntry.get().replace("$", ""))
        entertainment = int(self.entEntry.get().replace("$", ""))
        child = int(self.childEntry.get().replace("$", ""))
        debt = int(self.debtEntry.get().replace("$", ""))
        other = int(self.otherEntry.get().replace("$", ""))

        # Calculate total income and expenses
        expenses = housing + groceries + taxes + healthcare + entertainment + child + debt + other
        total_income = main_income + secondary_income + side_income - expenses
 
        database.update_user(
            main_income, secondary_income, side_income, expenses, housing, groceries,
            taxes, healthcare, entertainment, child, debt, other, total_income
        )  
        database.print_all_data()
        messagebox.showinfo("Success", "Data submitted successfully!")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for all fields!")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
  




root=tk.Tk()
app =InfoForm(root) 
database.create_table()
root.mainloop()  

 