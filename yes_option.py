from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import requests
import tkinter as tk

app = tk.Tk()
app.title("Intellivest")
app.iconbitmap("Intellivest.ico")

def make_text(text):
    output_text = tk.Text(app, wrap="word", foreground="white", background="purple", font="Courier")
    output_text.grid(row=0, column=0, padx=10, pady=10)

    # Insert the text into the Text widget
    output_text.insert(tk.END, text)


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
credit = forest.predict([[income, cash_salary, num_of_bank_acc, num_cards, rate, num_loans, days_delayed, num_payments, credit, debt, age, bal]])

print(f"Your predicted credit score is: {credit[0]}")

# Doesn't want to invest path
decision = int(input("Would you say that you want to invest? (Enter a 0 for no or a 1 for yes)" ))

if decision == 0:

    if credit[0] == "Poor":
        make_text("Ok,we suggest that you try and improve your credit score by paying bills on time, strategically paying credit balances, and getting credit for utility and rent payments. You may also want to check out resources like NerdWallet, Experian, Investopedia, and online forums to find ways to improve your credit score!")
    if credit[0] == "Standard" or credit[0] == "Good":
        make_text("Ok! Your credit score is in a good spot to begin investing! We advice that you begin researching ways to invest your money, as letting it sit will only deprecate it's value. Some investment opportunities include, but aren't limited to stocks, bonds, real estate, commodities, and foreign currency. You may also want to check out resources like Fidelity Investments, Stock Exchange, Investopedia, and online forums to begin your journey in investment!")

elif decision == 1:
    cash_to_invest = int(input("Great! How much CASH would you say that you could invest? "))

    loan_decision = int(input("Would you want to take a loan out to invest with? (0 for no, 1 for yes) "))

    if loan_decision == 0:
        if cash_to_invest == 10000:
            make_text("From sources across the web we advise you to invest in REIT's, "
                      "your emergency fund(s), and maxing out your IRA to optimize how money you'll have in the future")
        elif cash_to_invest < 10000:
            make_text("From sources across the web we advise you to invest in index funds, real estate, stocks, and e-commerce")
        else:
            make_text("From sources across the web we advise you to invest in high-yield savings, bonds, stocks, and mutual funds")

    # If they want to invest
    if loan_decision == 1:

        # If they can't get a loan
        if credit[0] == "Poor":

            make_text("Unfortunately, you wouldn't qualify for a loan but with your cash you can invest in low-risk assets such as:\n"
                      "S&P 500, Treasury Bonds, Dividend Stocks, and Renting out home spaces")
        if credit[0] != "Poor":
            loan_amount = int(input(f"Fortunately, you WOULD qualify for a loan! How big of a loan would you want for "
                                    f"investing? "))

            if credit[0] == "Standard":
                loan_amount = int(loan_amount*.75)

            print(f"The loan that your bank would likely issue you is approximately {loan_amount}")
            investment_amount = loan_amount+cash_to_invest
            print(f"Including your personal cash, your investment capital is roughly {investment_amount}")

            response_json = requests.get(
                "https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=660b686a5741c3a14db31b0f2dc9ce41").json()
            top_7_winners = response_json[:7]

            response_json = requests.get(
                "https://financialmodelingprep.com/api/v3/stock_market/losers?apikey=660b686a5741c3a14db31b0f2dc9ce41").json()
            top_7_losers = response_json[len(response_json) - 7:]

            # Risky companies is a list of companies that are risky, regardless of price
            risky_companies = []

            winner_expensive = sorted(top_7_winners[:int((len(top_7_winners)/2))], key=lambda x: x['price'], reverse=True)
            winner_not_expensive = sorted(top_7_winners[int((len(top_7_winners)) / 2):], key=lambda x: x['price'])

            loser_expensive = sorted(top_7_losers[:int((len(top_7_losers) / 2))], key=lambda x: x['price'], reverse=True)
            loser_not_expensive = sorted(top_7_losers[int((len(top_7_losers)) / 2):], key=lambda x: x['price'])

            if investment_amount > 140000:

                print_list = []
                for company in winner_expensive:
                    print_list.append(company["name"])
                for company in loser_expensive:
                    print_list.append(company["name"])

                make_text(text=f"Great news! We have a list of high-risk higher-price stocks just for you!         "
                               f"          "
                               f"{print_list}")

            if investment_amount < 140000:
                # Suggest pricey stocks

                print_list = []
                for company in winner_not_expensive:
                    print_list.append(company["name"])
                for company in loser_not_expensive:
                    print_list.append(company["name"])


                make_text(text= f"Great news! We have a list of high-risk lower-price stocks just for you!         "
                                f"          "
                                f"{print_list}")

app.mainloop()

