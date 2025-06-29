import numpy as np
import pygame
import math
import sys
import time
import matplotlib.pyplot as plt


def pendulum():
  def get_theta_double_dot(theta,theta_dot):
    return -μ * theta_dot -(g/L)*np.sin(theta)
  def Radians(theta):
    return np.pi*(theta/180)  
  

  pygame.init()
  
  width = 820#640
  height = 460#360
  window = pygame.display.set_mode((width, height))
  
  
  pygame.display.set_caption('Pendulum: Numerical solution vs Small angle approximation')

  font = pygame.font.SysFont('Arial', 20)
  
  #Constants 
  BLACK = (0,0,0)
  WHITE = (255,255,255)
  BLUE = (65,105,225)
  ORANGE = (255, 165, 0) 

  FPS = 100

  

  #Variables
  length = 150
  origin = [width//2, 150]
  Bob = [width//2, length]
  Alex =[width//2, length]
 
  #Physical constant
  g=9.80665
  L=2
  t_stop=float(input("Enter the time you want to stop the program: "))
  μ=float(input("Enter the friction coefficient (0 - 1): "))
  
  Theta_0 =Radians(float(input("Enter the starting angle(0-180): ")))
  Theta_dot_0=0
  theta=Theta_0
  theta_approximation=Theta_0
  
  theta_dot=Theta_dot_0
  delta_t=0.01
  t_passed=0
  t_r=[]
  th_r=[]
  shm=[]
  Period=0  
  Period=0
  stoptimer=False
  clock=pygame.time.Clock()
  




  while True:
      clock.tick(FPS)
      window.fill(WHITE)
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
      Bob[0] = int(origin[0] + length*math.sin(-1*theta)) 
      Bob[1] = int(origin[1] + length*math.cos(-1*theta))
      Alex[0] = int(origin[0] + length*math.sin(-1*theta_approximation)) 
      Alex[1] = int(origin[1] + length*math.cos(-1*theta_approximation))
      
      pygame.draw.line(window, BLUE, (origin[0], origin[1]), (Bob[0], Bob[1]), 1)
      pygame.draw.circle(window, BLUE, (Bob[0], Bob[1]), 15)
      pygame.draw.line(window, ORANGE, (origin[0], origin[1]), (Alex[0], Alex[1]), 2)
      pygame.draw.circle(window, ORANGE, (Alex[0], Alex[1]), 10)

      pygame.draw.line(window, BLACK, (origin[0], origin[1]), (width//2 ,150+length), 1)
      
      # The blue pendulum is the numerical solution
      # The orange pendulum is the small angle approximation
    
  
    
      
  
      
      theta_double_dot=get_theta_double_dot(theta,theta_dot)

      theta_dot += theta_double_dot*delta_t
     

    
      theta+=theta_dot*delta_t
      

      if t_passed==0 or t_passed > 0 and not stoptimer:
            if μ == 0:
              Period+=delta_t
              if np.floor(theta_dot)==0 and theta>0:
                    stoptimer=True
            else:
              Period = "Can't be determined."

  
    
      t_passed += delta_t
      print(t_passed)
      theta_approximation=(Theta_0)*np.cos(math.sqrt(g/L)*t_passed)
      
      t_r.append(t_passed)
      th_r.append(theta)
      shm.append(theta_approximation)

      if t_passed > t_stop:
        break
      
 

      time_display = f" Time Passed: {t_passed:.2f} s"
      theta_display = f" Angle (numerical solution): {theta:.2f} radians"
      theta_approximation_display = f" Angle (small angle approximation): {theta_approximation:.2f} radians"
      
      
      
      DisplayData = [
          time_display,
          theta_display,
          theta_approximation_display
      ]

      for i, line in enumerate(DisplayData):
          text_surface = font.render(line, True, BLACK)
          window.blit(text_surface, (10,10 + i*30))
      
  
      pygame.display.update()

  print(Period)
  plt.plot(t_r, th_r, label='Numerical solution')
  plt.plot(t_r,shm, label='Small angle approximation',linestyle='--')
  plt.title("Pendulum Motion: Numerical solution vs Small angle approximation")
  plt.xlabel('Time(s)')
  plt.ylabel('Angle(radians)')

  plt.grid(True, which='both')
  plt.axhline(y=0, color='k')
  plt.legend()
  plt.show()

pendulum()