from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1,
                               "Good": 2,
                               "Bad": 0})

x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary",
                   "Num_Bank_Accounts", "Num_Credit_Card",
                   "Interest_Rate", "Num_of_Loan",
                   "Delay_from_due_date", "Num_of_Delayed_Payment",
                   "Credit_Mix", "Outstanding_Debt",
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data["Credit_Score"])

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)


# scores = []
# for i in range(1, 12):
#     forest = RandomForestClassifier(max_depth=7, n_estimators=i)
#     forest.fit(x_train, y_train)
#     scores.append(forest.score(x_test, y_test))
#
# plt.plot(range(1, 12), scores, label="Testing accuracy")
# plt.xlabel("N_Estimators")
# plt.ylabel("Testing Accuracy")
# plt.legend()
# plt.show()

# Optimal Parameters
forest = RandomForestClassifier(max_depth=7, n_estimators=7)
forest.fit(x_train, y_train)

# Attain User Info
print("\nIn order to begin our classification for your credit score, we need some basic information:\n")
income = float(input("Annual Income: "))
cash_salary = float(input("Monthly Inhand Salary: "))
num_of_bank_acc = float(input("Number of Bank Accounts: "))
num_cards = float(input("Number of Credit cards: "))
rate = float(input("Interest rate: "))
num_loans = float(input("Number of Loans: "))
days_delayed = float(input("Average number of days delayed by the person: "))
num_payments = float(input("Number of delayed payments: "))
credit = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
debt = float(input("Outstanding Debt: "))
age = float(input("Credit History Age: "))
bal = float(input("Monthly Balance: "))

# Predicted Credit Score
credit = forest.predict([income, cash_salary, num_of_bank_acc, num_cards, rate, num_loans, days_delayed, num_payments, credit, debt, age, bal])


# Doesn't want to invest path
decision = int(input("Would you say that you want to invest? (Enter a 0 for no or a 1 for yes"))

if decision == 0:

    if credit[0] == "Poor":
        print(f"Ok, we suggest that you try and improve your credit score by paying bills on time, "
              f"strategically paying credit balances, and getting credit for utility and rent payments!")
        print()
        print(f"You may also want to check out resources like NerdWallet, Experian, Investopedia, and online forums!")

    if credit[0] == "Standard" or credit[0] == "Good":
        print("Ok! Your credit score is in a good spot to begin investing! We advice that "
              "you begin researching ways to invest your money, as letting it sit will only deprecate it's value")

        print("Some investment opportunities include, but aren't limited to stocks, bonds, real estate, commodities, and "
              "foreign currency")

elif decision == 1:
    cash_to_invest = int(input("Great! How much CASH would you say that you could invest?"))

    loan_decision = int(input("Would you want to take a loan out to invest with? (0 for no, 1 for yes)"))

    # If they want to invest
    if loan_decision == 1:

        # If they can't get a loan
        if credit[0] == "Poor":
            print(f"Unfortunately, you wouldn't qualify for a loan but with your cash you can invest in low-risk assets "
                  f"such as:")
            print(f"S&P 500, Treasury Bonds, Dividend Stocks, and Renting out home spaces")

        if credit[0] != "Poor":
            loan_amount = int(input(f"Fortunately, you WOULD qualify for a loan! How big of a loan would you want for "
                                    f"investing?"))

            if credit[0] == "Standard":
                loan_amount = int(loan_amount*.75)

            print(f"The loan that your bank would likely issue you is approximately {loan_amount}")
            investment_amount = loan_amount+cash_to_invest
            print(f"Including your personal cash, your investment capital is roughly {investment_amount}")

            if investment_amount < 140000:




