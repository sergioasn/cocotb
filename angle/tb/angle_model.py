def angle_model(theta_in,freq, sequence_in):
  if freq == 0:#60Hz
    counter = 1023
  elif freq == 1:
    counter = 1023
  if angle_model.last_theta != theta_in:
    angle_model.last_theta = theta_in
    angle_model.counter = theta_in
    return angle_model.last_theta
  else:
      if sequence_in ==1:
          if angle_model.counter < counter:
              angle_model.counter += 1
          else:
              angle_model.counter = 0
      else:
           if angle_model.counter > 0:
               angle_model.counter -= 1
           else:
               angle_model.counter = counter
  return angle_model.counter
#static variable
angle_model.counter = 0
angle_model.last_theta = 0
