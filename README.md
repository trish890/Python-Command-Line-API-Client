# Python-Command-Line-API-Client

### What is this?
This is a file called `client.py`. It is a tool that you use in your terminal. It helps you manage a printing shop. You use it to send and see information about orders.


### What can it do?
The client has four main actions:
* **view**: Shows a list of all orders.
* **order**: Creates a new print order for a customer.
* **search**: Finds one specific order using its ID number.
* **stats**: Shows the total money and the number of orders.

### How to use it
You use this tool by typing `python client.py` followed by a command.

**1. See all orders**
Type this to see everything:
`python client.py view`

**2. Make a new order**
Type the name, email, pages, and paper type:
`python client.py order "Name" "Email" Pages PaperType`

*Example:* `python client.py order "John Doe" "john@mail.com" 10 colored`

**3. Find an order by ID**
Type the ID number of the order:
`python client.py search 1`

**4. See shop totals**
Type this to see the statistics:
`python client.py stats`

### Important Information
* **Paper Types:** You must use `black_white`, `colored`, or `photo`.
* **Names:** If a name has a space, put it in quotes like this: `"Trisha Mae"`.