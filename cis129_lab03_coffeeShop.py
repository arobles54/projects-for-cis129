def main():
    # Display shop name and separator
    print("*" * 35)
    print("My Coffee and Muffin Shop")

    # Get user input for the number of coffees, muffins, cookies, and brownies
    print("Number of coffees bought?")
    number_of_coffees = int(input())
    print("Number of muffins bought?")
    number_of_muffins = int(input())
    print("Number of cookies bought?")
    number_of_cookies = int(input())
    print("Number of brownies bought?")
    number_of_brownies = int(input())

    
    # Print separator
    print("*" * 35)
    
    # Calculate total costs
    total_cost_of_coffees = number_of_coffees * 5
    total_cost_of_muffins = number_of_muffins * 4
    total_cost_of_cookies = number_of_cookies * 3
    total_cost_of_brownies = number_of_brownies * 3
    
    # Calculate subtotal, tax, and total
    subtotal = total_cost_of_coffees + total_cost_of_muffins + total_cost_of_cookies + total_cost_of_brownies
    tax = subtotal * 0.06 
    total = subtotal + tax
    
    # Print receipt
    print("\n\n\n")
    print("*" * 35)
    print("My Coffee and Muffin Shop Receipt")
    print(f"{number_of_coffees} Coffee at $5 each: ${total_cost_of_coffees:.2f}")
    print(f"{number_of_muffins} Muffins at $4 each: ${total_cost_of_muffins:.2f}")
    print(f"{number_of_cookies} Cookies at $3 each: ${total_cost_of_cookies:.2f}")
    print(f"{number_of_brownies} Brownies at $3 each: ${total_cost_of_brownies:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("-" * 7)
    print(f"Total: ${total:.2f}")
    print("*" * 35)

    # Print thank you message
    print("Thank you for your purchase! We hope to see your wonderful smile here again soon! 😊")

if __name__ == "__main__":
    main()
