def weight_on_planets():
   # write your code here
   
    x = float(input('What do you weigh on earth?'));
    #promts input casted as a float number
    M = x*0.38;
    J = x*2.34;

    print(' \nOn Mars you would weigh',M,'pounds.\nOn Jupiter you would weigh',J,'pounds.'); 
   
if __name__ == '__main__':
    weight_on_planets();
