# Taste Trek Restaurant Billing System

Welcome to Taste Trek! This is a simple Python-based billing system for a restaurant. The program allows customers to order items from a menu, calculates the total bill, adds tax, and provides the final amount to be paid.

## Features

- Display a menu with item prices.
- Allow customers to order multiple items.
- Calculate the total bill, including a 10% tax.
- Continuously prompt the user to order until they choose to stop.

## Menu

Here is the list of available items:

| Item           | Price (Rs.) |
|----------------|-------------|
| Pizza Regular  | 700         |
| Pizza Large    | 1300        |
| Crispy Zinger  | 500         |
| Coffee         | 600         |
| Drinks         | 150         |
| Broast         | 800         |
| Rolls          | 300         |

## How to Use

1. **Run the Program**: Start the program in your Python environment.
2. **View the Menu**: The menu will be displayed automatically.
3. **Place an Order**: Enter the name of the item you'd like to order. The item name should be typed exactly as it appears in the menu.
4. **Add More Items**: After placing an order, you can choose to add more items by typing "yes" or finish by typing "no".
5. **Calculate Total**: The program calculates the total bill, including a 10% tax, and displays it to the user.
6. **Exit**: Type "exit" at any time to stop ordering and finalize the bill.

## Example Usage

```bash
Welcome to Taste Trek :)
Enter your order (or type 'exit' to finish): pizza regular
Successfully, your pizza regular is added to your bill!
Do you want to add something more (yes/no)? yes
Enter a next food you want to addition! drinks
Successfully, drinks is added to your bill!
Do you want to add something more (yes/no)? no
Your total bill before tax is Rs.850
Your bill after tax addition is Rs.935.0
