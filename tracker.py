def calculate_finances():
    print("--- Business Financial Tracker ---")
    
    try:
        # Input financial data
        gross_sales = float(input("Enter total daily sales/revenue: "))
        expenses = float(input("Enter total daily expenses (rent, stock, utilities): "))
        
        # Calculate business logic metrics
        net_profit = gross_sales - expenses
        
        if gross_sales > 0:
            profit_margin = (net_profit / gross_sales) * 100
        else:
            profit_margin = 0.0

        # Output the professional summary
        print("\n==============================")
        print("      DAILY FINANCIAL REPORT  ")
        print("==============================")
        print(f"Gross Revenue:       {gross_sales:,.2f}")
        print(f"Total Expenses:      {expenses:,.2f}")
        print("------------------------------")
        print(f"Net Profit/Loss:     {net_profit:,.2f}")
        print(f"Net Profit Margin:   {profit_margin:.2f}%")
        print("==============================")
        
        # Simple business health advisory logic
        if profit_margin >= 20:
            print("Status: Healthy profit margin! Business is running efficiently.")
        elif 0 <= profit_margin < 20:
            print("Status: Low profit margin. Consider optimizing daily operational costs.")
        else:
            print("Status: Operating at a LOSS. Immediate budget adjustments required.")
            
    except ValueError:
        print("Error: Please enter valid numerical values for financial data.")

# Run the tracker script
if __name__ == "__main__":
    calculate_finances()
