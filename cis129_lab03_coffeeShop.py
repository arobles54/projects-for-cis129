def main():
    # Display shop name and separator
    print("*" * 35)
    print("My Coffee and Muffin Shop")

    # Get user input for the number of coffees and muffins
    print("Number of coffees bought?")
    number_of_coffees = int(input())
    print("Number of muffins bought?")
    number_of_muffins = int(input())

    # Print separator
    print("*" * 35)
    
    # Calculate total costs
    total_cost_of_coffees = number_of_coffees * 5
    total_cost_of_muffins = number_of_muffins * 4
    
    # Calculate subtotal, tax, and total
    subtotal = total_cost_of_coffees + total_cost_of_muffins
    tax = subtotal * 0.06 
    total = subtotal + tax
    
    # Print receipt
    print("\n\n\n")
    print("*" * 35)
    print("My Coffee and Muffin Shop Receipt")
    print(f"{number_of_coffees} Coffee at $5 each: ${total_cost_of_coffees:.2f}")
    print(f"{number_of_muffins} Muffins at $4 each: ${total_cost_of_muffins:.2f}")
    print(f"6% tax: ${tax:.2f}")
    print("-" * 7)
    print(f"Total: ${total:.2f}")
    print("*" * 35)

if __name__ == "__main__":
    main()