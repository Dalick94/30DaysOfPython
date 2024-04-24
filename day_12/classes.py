### CLASSES ###

# EXERCISES LEVEL 1 #

#1.
import statistics

class Statistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        return statistics.mode(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        return statistics.variance(self.data)

    def standard_deviation(self):
        return statistics.stdev(self.data)

    def min_value(self):
        return min(self.data)

    def max_value(self):
        return max(self.data)

    def count(self):
        return len(self.data)

    def percentile(self, p):
        return statistics.quantile(self.data, p/100)

    def frequency_distribution(self):
        freq_dist = {}
        for num in self.data:
            if num in freq_dist:
                freq_dist[num] += 1
            else:
                freq_dist[num] = 1
        return freq_dist

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

stat = Statistics(ages)

print("Mean:", stat.mean())
print("Median:", stat.median())
print("Mode:", stat.mode())
print("Range:", stat.range())
print("Variance:", stat.variance())
print("Standard Deviation:", stat.standard_deviation())
print("Min Value:", stat.min_value())
print("Max Value:", stat.max_value())
print("Count:", stat.count())
print("25th Percentile:", stat.percentile(25))
print("Frequency Distribution:", stat.frequency_distribution())

# EXERCISES LEVEL 2 
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()
    
    def add_income(self, amount, description):
        self.incomes.add((amount, description))
    
    def add_expense(self, amount, description):
        self.expenses.add((amount, description))
    
    def total_income(self):
        return sum(income[0] for income in self.incomes)
    
    def total_expense(self):
        return sum(expense[0] for expense in self.expenses)
    
    def account_info(self):
        return f"{self.firstname} {self.lastname}'s account information:\nIncomes: {self.incomes}\nExpenses: {self.expenses}"
    
    def account_balance(self):
        return self.total_income() - self.total_expense()