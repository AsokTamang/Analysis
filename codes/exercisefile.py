def process_customer_data(filename):
    data = {}
    customers_summary = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            name, money = line.split(',')
            data[name] = int(money)
    for key, value in data.items():
        if 100 <= value <= 199:
            customers_summary[key] = (value, 'Bronze')
        elif 200 <= value <= 499:
            customers_summary[key] = (value, 'Silver')
        else:
            customers_summary[key] = (value, 'Gold')
    return customers_summary
print(process_customer_data("C:/Users/ashok/OneDrive/Desktop/customers.txt"))

