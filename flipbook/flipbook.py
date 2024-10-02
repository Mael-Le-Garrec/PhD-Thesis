import matplotlib.pyplot as plt
from numpy import radians
import numpy as np
import matplotlib.animation as animation
from math import radians
import os

# Create a directory to save the images
output_dir = './frames'
os.system(f'rm -f {output_dir}/*')
os.makedirs(output_dir, exist_ok=True)

# Parameters for the animation
n_frames = 260
travel_frames = int(n_frames / 2)  # number of frames where particles travel before colliding
dot_radius = 0.4


# Have like 10 frames with the last one maybe?
n_last_frames = 10


width = np.linspace(0, 150, travel_frames)
height = np.linspace(0, 70, n_frames)
solenoid_dst = 20 # position of the solenoid relative to the center

color = "#BBBBBB"
color_solenoid = "#AAAAAA"


def draw_solenoid(ax):
    center_x = (width[-1] - width[0]) / 2
    center_y = (height[-1] - height[0]) / 2
    ax.add_patch(plt.Circle((center_x, center_y), 
                            solenoid_dst, 
                            fill=False,
                            color='grey',
                            alpha=0.1)
                 )


def create_curved_trajectory(ax, max_i, angle, mass_factor, speed, degrees=True):
    if degrees:
        angle = radians(angle)

    I = 500  # solenoid current
    m = 1.88e-28 * mass_factor  # electron mass
    q = 1.6e-19   # charge of particle

    mu_0 = 4 * np.pi * 1e-7  # Permeability of free space (T*m/A)
    B = mu_0 * 1 * I
    
    # Beginning positions
    center_x = (width[-1] - width[0]) / 2
    center_y = (height[-1] - height[0]) / 2
    initial_velocity = np.array([speed * np.cos(angle), speed * np.sin(angle)])

    position = np.zeros((max_i, 2))
    velocity = np.zeros((max_i, 2))
    position[0] = np.array([center_x, center_y])
    velocity[0] = initial_velocity

    dot_radius = 0.1

    x, y = position[0]

    # Parametric equations for projectile motion
    for i in range(1, max_i):
        dst = ((x - center_x)**2 + (y - center_y)**2)**0.5
        if dst <= solenoid_dst:
            B_field = B
        else:
            B_field = -B / (1 + (dst / solenoid_dst))

        acceleration = q * np.cross(velocity[i-1], np.array([0, 0, B_field]))[:2] / m
        velocity[i] = velocity[i-1] + acceleration * i/1e9
        position[i] = position[i-1] + velocity[i] * i/1e9

        x, y = position[i]
        ax.add_patch(plt.Circle((x, y), dot_radius, color=color))


range_ = range(0, n_frames)  # everything
for i in range_:
    #if i != range_[-1]:
    #    continue
    print(i)
    fig, ax = plt.subplots()
    ax.plot([0, width[-1]], [0, 0], 'w.')  # Dummy plot for scaling
    ax.plot([0], [height[-1]], 'w.')  # Dummy plot for scaling

    # Draw the magnet
    draw_solenoid(ax)

    # Make the particles move towards each other
    if i < travel_frames+1:  # +1 so we actually collide
        # First particle
        x = (width[-1] / (travel_frames)* i) / 2
        y = (height[-1] - height[0]) / 2
        ax.add_patch(plt.Circle((x, y), dot_radius, color=color))

        # Second particle
        x = width[-1] - (width[-1] / (travel_frames) * i) / 2
        y = (height[-1] - height[0]) / 2
        ax.add_patch(plt.Circle((x, y), dot_radius, color=color))


    # Collide!
    if i > travel_frames:
        # Have the last n_last_frames the same
        if i >= (n_frames - n_last_frames):
            index = (n_frames - n_last_frames) - travel_frames
        else:
            index = i - travel_frames
        speed = 8e6

        #for angle in [45, 90+45, -45, 69, -69, 69+90, -69-90]:
        for angle in [21, -12, -180-5, -180-10]:#, -69, 69+90, -69-90]:
            create_curved_trajectory(ax, index, angle=angle, mass_factor=1e10, speed=speed, degrees=True)
        
        create_curved_trajectory(ax, index, angle=34, mass_factor=1, degrees=True, speed=speed)
        create_curved_trajectory(ax, index, angle=90, mass_factor=0.6, degrees=True, speed=speed)
        create_curved_trajectory(ax, index, angle=180+40, mass_factor=1.5, degrees=True, speed=speed)
        create_curved_trajectory(ax, index, angle=78, mass_factor=-0.7, degrees=True, speed=speed)

    ax.set_aspect('equal')
    ax.axis('off')
    plt.savefig(f"{output_dir}/frame_{i}.pgf", bbox_inches='tight', pad_inches=0)
    plt.savefig(f"{output_dir}/frame_{i}.png", bbox_inches='tight', pad_inches=0)
    plt.close(fig)



#os.system('convert -delay 10 -loop 0 frames/*.png frames/animation.gif')
