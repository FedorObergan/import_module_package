from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import numpy as np
from bashplotlib.histogram import plot_hist




if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.datetime.now())
    sample = np.random.exponential(scale=1, size=100)
    plot_hist(sample, bincount=50)
