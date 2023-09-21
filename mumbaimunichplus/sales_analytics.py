import matplotlib.pyplot as plt
import datetime

class Sale:
    def __init__(self, item_name, quantity, total_price, date):
        self.item_name = item_name
        self.quantity = quantity
        self.total_price = total_price
        self.date = date

class SalesAnalytics:
    def __init__(self):
        self.sales_data = []

    def record_sale(self, item_name, quantity, total_price):
        current_date = datetime.date.today()
        sale = Sale(item_name, quantity, total_price, current_date)
        self.sales_data.append(sale)

    def generate_daily_sales_report(self, date):
        total_sales = 0
        for sale in self.sales_data:
            if sale.date == date:
                total_sales += sale.total_price
        return f"Total sales on {date}: ${total_sales:.2f}"

    def generate_weekly_sales_report(self, start_date, end_date):
        total_sales = 0
        for sale in self.sales_data:
            if start_date <= sale.date <= end_date:
                total_sales += sale.total_price
        return f"Total sales from {start_date} to {end_date}: ${total_sales:.2f}"

    def generate_monthly_sales_report(self, month, year):
        total_sales = 0
        for sale in self.sales_data:
            if sale.date.month == month and sale.date.year == year:
                total_sales += sale.total_price
        return f"Total sales for {datetime.date(year, month, 1).strftime('%B %Y')}: ${total_sales:.2f}"

    def visualize_sales_trend(self):
        dates = [sale.date for sale in self.sales_data]
        total_sales = [sale.total_price for sale in self.sales_data]

        plt.figure(figsize=(10, 6))
        plt.plot(dates, total_sales, marker='o', linestyle='-')
        plt.title("Sales Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Total Sales ($)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

# Sample usage:
sales_analytics = SalesAnalytics()

# Record sales
sales_analytics.record_sale("Chips", 5, 12.5)
sales_analytics.record_sale("Coke", 3, 4.5)
sales_analytics.record_sale("Brownie", 2, 6.0)

# Generate and print a daily sales report
daily_report = sales_analytics.generate_daily_sales_report(datetime.date.today())
print("Daily Sales Report:")
print(daily_report)

# Generate and print a weekly sales report
week_start_date = datetime.date.today() - datetime.timedelta(days=6)
weekly_report = sales_analytics.generate_weekly_sales_report(week_start_date, datetime.date.today())
print("Weekly Sales Report:")
print(weekly_report)

# Generate and print a monthly sales report
monthly_report = sales_analytics.generate_monthly_sales_report(datetime.date.today().month, datetime.date.today().year)
print("Monthly Sales Report:")
print(monthly_report)

# Visualize sales trend
sales_analytics.visualize_sales_trend()
plt.show()  # Show the Matplotlib plot
