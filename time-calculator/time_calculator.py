def add_time(start, duration,Dname=""):
  day_name = ['sunday',"monday","tuesday","wednesday",'thursday','friday','saturday']
  start = start.split(" ") 
  h,m = start[0].split(":")
 
  isAm = True if start[1] == 'AM' else False
  duration = duration.split(":")
  aH,aM = duration[0],duration[1]
  rH,rM = int(h) + int(aH), int(m) + int(aM)
  rD = 0
  while (rM > 60):
    rM -= 60
    rH += 1
  while rH > 12:
    rH -= 12
    if isAm:
      isAm = False
    else:
      isAm = True
      rD += 1
  if rH == 12:
    if isAm:
      isAm = False
    else:
      isAm = True
      rD += 1
  time_txt = '{}:{} {}'.format(rH,str(rM).zfill(2),"AM" if isAm else "PM")
  if Dname != "":
    index = day_name.index(Dname.lower())
    time_txt += ', {}'.format(day_name[(index + rD)% 7].capitalize())
  if rD == 1:
    time_txt += " (next day)"
  elif rD != 1 and rD != 0:
    time_txt += " ({} days later)".format(rD)
  return time_txt
  
