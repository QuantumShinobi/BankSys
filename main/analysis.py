#!! No need for file, using JS to plot the graph

# import pandas as pd
# import matplotlib.pyplot as plt
# # from django.shortcuts import render
# from .models import *
# import csv


# def create_csv():
#     transactions = Transaction.objects.all()
#     with open('transactions.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['user', 'name', 'amount', 'type', 'reason',
#                         'transaction_id', 'timestamp', 'category'])
#         for transaction in transactions:
#             user = transaction.user
#             user_name = user.unique_id
#             name = user.name
#             amount = transaction.amount
#             type = transaction.type
#             reason = transaction.reason
#             transaction_id = transaction.transaction_id
#             timestamp = transaction.timestamp
#             category = transaction.category
#             writer.writerow([user_name, name, amount, type, reason,
#                             transaction_id, timestamp, category])


# # def analyse_spending():
# #     # Import the csv, pandas, and matplotlib modules

# #     # Define the name of the user to analyse
# #     user_name = "Ash"

# #     # Read the csv file into a pandas dataframe
# #     df = pd.read_csv('transactions.csv')

# #     # Filter the dataframe by the user name
# #     df_user = df[df['user'] == user_name]

# #     # Calculate the total amount spent by the user
# #     total_spent = df_user[df_user['type'] == 'Withdraw']['amount'].sum()

# #     # Calculate the average amount spent by the user per transaction
# #     avg_spent = total_spent / len(df_user[df_user['type'] == 'Withdraw'])

# #     # Calculate the percentage of spendings by category
# #     spendings_by_category = df_user[df_user['type'] ==
# #                                     'Withdraw']['category'].value_counts(normalize=True) * 100

# #     # Create a figure with two subplots
# #     fig, (ax1, ax2) = plt.subplots(
# #         1, 2, figsize=(14, 6))  # Adjust the figure size
# #     fig.subplots_adjust(wspace=0.3)

# #     # Plot the pie chart for the percentage of spendings by category
# #     ax1.pie(spendings_by_category.values,
# #             labels=spendings_by_category.index, autopct='%1.1f%%')
# #     ax1.set_title(f'Percentage of spendings by category for {user_name}')

# #     # Plot the bar chart for the amount spent by transaction
# #     categories = df_user[df_user['type'] == 'Withdraw']['category'].unique()

# #     # Adjust the width to space out the bars more
# #     width = 0.7

# #     ax2.bar(categories, df_user[df_user['type'] == 'Withdraw'].groupby(
# #         'category')['amount'].sum(), width=width)
# #     ax2.set_xticks(categories)
# #     ax2.set_xticklabels(categories)
# #     ax2.set_title(f'Amount spent by transaction for {user_name}')
# #     ax2.set_xlabel('Category')
# #     ax2.set_ylabel('Amount')
# #     fig.subplots_adjust(top=0.8)
# #     plt.tight_layout()

# #     # Save the figure as 'analysis.png' with a higher dpi for better resolution
# #     plt.savefig('analysis.png', dpi=300)  # Adjust dpi as needed


# # # Call the function to analyze spending
# # analyse_spending()


# def analyse_spending(user_uuid="1d06b5ab35094c579c467b844bb93a79"):

#     # Define the name of the user to analyse
#     # user_name = user_uuid

#     user_name = "1d06b5ab35094c579c467b844bb93a79"
#     # Read the csv file into a pandas dataframe
#     df = pd.read_csv('transactions.csv')

#     # Filter the dataframe by the user name
#     df_user = df[df['user'] == user_name]
#     name = df_user['name']
#     # Calculate the total amount spent by the user
#     total_spent = df_user[df_user['type'] == 'Withdraw']['amount'].sum()

#     # Calculate the average amount spent by the user per transaction
#     avg_spent = total_spent / len(df_user[df_user['type'] == 'Withdraw'])

#     # Calculate the percentage of spendings by category
#     spendings_by_category = df_user[df_user['type'] ==
#                                     'Withdraw']['category'].value_counts(normalize=True) * 100

#     # Create a figure with two subplots
#     fig, (ax1, ax2) = plt.subplots(
#         1, 2, figsize=(14, 6))  # Adjust the figure size
#     fig.subplots_adjust(wspace=0.3)

#     # Plot the pie chart for the percentage of spendings by category
#     ax1.pie(spendings_by_category.values,
#             labels=spendings_by_category.index, autopct='%1.1f%%')
#     ax1.set_title(f'Percentage of spendings by category for {name}')

#     # Save the pie chart as a separate image
#     # plt.savefig('pie_chart.png', dpi=300)  # Adjust dpi as needed

#     # Plot the bar chart for the amount spent by transaction
#     categories = df_user[df_user['type'] == 'Withdraw']['category'].unique()

#     # Adjust the width to space out the bars more
#     width = 0.7

#     ax2.bar(categories, df_user[df_user['type'] == 'Withdraw'].groupby(
#         'category')['amount'].sum(), width=width)
#     ax2.set_xticks(categories)
#     ax2.set_xticklabels(categories)
#     ax2.set_title(f'Amount spent by transaction for {name}')
#     ax2.set_xlabel('Category')
#     ax2.set_ylabel('Amount')
#     fig.subplots_adjust(top=0.8)
#     plt.tight_layout()

#     # Save the bar chart as a separate image
#     plt.savefig('bar_chart.png', dpi=300)  # Adjust dpi as needed


# if __name__ == "__main__":
#     analyse_spending("1d06b5ab35094c579c467b844bb93a79")
