def angle_model(theta_in,freq, sequence_in):
  if freq == 0:#60Hz
    angle_model.counter = 408
  elif freq == 1:
    angle_model.counter = 489
  if angle_model.theta_input != theta_in:
    angle_model.theta_input= theta_in
    angle_model.last_theta= theta_in
    angle_model.cnt_aux=0
  else:
      if angle_model.cnt_aux < angle_model.counter:
        angle_model.cnt_aux +=1
      else:
        angle_model.cnt_aux=0
        if sequence_in ==1:
          angle_model.last_theta += 1
          # print('maaaaaaaaaassss')
        else:
          angle_model.last_theta -= 1
          # print('menosssss')

  return angle_model.last_theta
#static variable
angle_model.cnt_aux=0
angle_model.theta_input=0
angle_model.counter = 0
angle_model.last_theta = 0
