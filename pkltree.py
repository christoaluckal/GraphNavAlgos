import numpy as np
from scipy.spatial import KDTree
import pickle as pk
# from random import randint as rd
import matplotlib.pyplot as plt
import time
final_coords_list = []

#Reads the pkl file with the coordinate list as a list of tuples eg: list = [(X0,Y0),(X1,Y1),....]
#Run the image_to_list python script to generate the list from a png of the "map"
coords_list = pk.load(open("shapes.pkl",'rb'))

# print("Number of datapoints is {}".format(len(coords_list)))

#Convert the python list to a numpy array
final_coords_list = np.array(coords_list)
x_coords,y_coords = zip(*final_coords_list)

#Show the full "map"
# plt.scatter(x_coords,y_coords,s=0.1)
# plt.show()


start_s = time.time()
#Scipy KDTree implementation
kdtree = KDTree(final_coords_list)

end_s = time.time()

print(str(end_s-start_s)+" s")

#Input the position of the observer
print("Enter the current position X")
current_posx = int(input())
print("Enter the current position Y")
current_posy = int(input()) 
print("Enter zoom amount [Higher number is less zoom :)]")
zoom = int(input())
print("Enter step size:")
step_size = int(input())
print("Press WASD to move, X for step-size or press E to exit\n")
while True:
    start_s = time.time()
    #Query point is the current location with a radius set to 10 unit distance. Change 10 to whatever is desired
    coords = kdtree.query_ball_point([current_posx,current_posy],r=zoom)
    end_s = time.time()
    #final_coords_list[coords] is a list of coordinate pairs that fall inside the specified distance
    point_list = final_coords_list[coords]
    #Incase there are no points in the vicinity we skip the current iteration and ask for next directional input
    if len(point_list) is not 0:
        # Split the coords terms to X and Y coordinates
        plot_x,plot_y = zip(*final_coords_list[coords])
        plt.scatter(plot_x,plot_y,s=0.01)
        plt.show()
    else:
        print("Skipped at:",str(current_posx)," ",str(current_posy))
        pass
    #Current position
    next_dir = input()
    if next_dir == 'w':
        current_posy = current_posy + step_size
    elif next_dir == 'a':
        current_posx = current_posx - step_size
    elif next_dir == 's':
        current_posy = current_posy - step_size
    elif next_dir == 'd':
        current_posx = current_posx + step_size
    elif next_dir == 'z':
        zoom = int(input("Change zoom: "))
    elif next_dir == 'e':
        break
    elif next_dir == 'x':
        step_size = int(input())
    else:
        pass