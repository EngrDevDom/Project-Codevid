"""
    Project Codevid
    Update and data analysis of Covid cases in the Philippines
    during the period of March to July.
"""

from pylab import plot, show, title, xlabel, ylabel, legend

# Date picked 5 times a month
date = range(0, 5)

# Define the number of cases per month
March_case = []
April_case = []
May_case = []
June_case = []
July_case = []

# Define the legend
title('Average Covid cases in the Philippines')
xlabel('Month')
ylabel('No. of Cases')
legend(['March', 'April', 'May', 'June', 'July'])

# Plot and show the graph
plot()
show()
