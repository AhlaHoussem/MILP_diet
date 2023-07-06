from pulp import *

def main():

    # Define the variables

    x1 = LpVariable("Broccoli", lowBound=0, cat='Integer')
    x2 = LpVariable("Meat", lowBound=0, cat='Integer')
    x3 = LpVariable("Blueberry", lowBound=0, cat='Integer')
    x4 = LpVariable("Chicken", lowBound=0, cat='Integer')
    x5 = LpVariable("Beans", lowBound=0, cat='Integer')
    x6 = LpVariable("Fish", lowBound=0, cat='Integer')

    # Define the problem
    prob = LpProblem("DietProblem", LpMinimize)

    # Define the objective function
    prob += 30*x1 + 250*x2 + 57*x3 + 335*x4 + 245*x5 + 206*x6

    # Define the constraints
    prob += 4*x1 + 0*x2 + 14.5*x3 + 0*x4 + 45*x5 + 0*x6 >= 130
    prob += 2*x1 + 26*x2 + 0.7*x3 + 25*x4 + 15*x5 + 22*x6 >= 150
    prob += 0.3*x1+17*x2+0.3*x3+21*x4+1*x5+13*x6 <= 300
    prob += 30*x1 + 250*x2 +57* x3 +335* x4 +245* x5 +206* x6 <= 4000


    # Check the status before solving
    print(f"Status: {LpStatus[prob.status]}")

    # Solve the problem
    prob.solve()

    # Check the status after solving
    print(f"Status: {LpStatus[prob.status]}")

    # Print the optimal values of the decision variables
    print(f"Optimal value of Broccoli: {x1.varValue}")
    print(f"Optimal value of Meat: {x2.varValue}")
    print(f"Optimal value of Blueberry: {x3.varValue}")
    print(f"Optimal value of Chicken: {x4.varValue}")
    print(f"Optimal value of Beans: {x5.varValue}")
    print(f"Optimal value of Fish: {x6.varValue}")



if __name__ == '__main__':
    main()
