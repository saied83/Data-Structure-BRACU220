class Patient:
  def __init__(self, id, name, age, blood_group, nxt, prev):
    self.id = id
    self.name = name
    self.age = age
    self.blood_group = blood_group
    self.prev = prev
    self.nxt = nxt

class WRM():
  def __init__(self):
    self.dummy_head = Patient(None, None, None, None, None, None)
    self.dummy_head.nxt = self.dummy_head
    self.dummy_head.prev = self.dummy_head
    self.tail = self.dummy_head

  def RegisterPatient(self, id, name, age, blood_group):
    self.n = Patient(id, name, age, bg, self.dummy_head, self.tail)
    self.tail.nxt = self.n
    self.tail = self.tail.nxt
    self.dummy_head.prev = self.tail
    print(f"\n\n{name} registered successfully as a patient")
    print("\n#########################################\n")

  def ServePatient(self):
    temp = self.dummy_head.nxt
    self.dummy_head.nxt = temp.nxt
    self.dummy_head.nxt.prev = self.dummy_head
    print(f"\n\n{temp.name} served successfully")
    print("\n#########################################\n")

  def CancelAll(self):
    self.dummy_head.nxt = self.dummy_head
    self.dummy_head.prev = self.dummy_head
    self.tail = self.dummy_head
    print("\n\nAll appointments cancelled successfully.")
    print("\n#########################################\n")


  def CanDoctorGoHome(self):
    if self.dummy_head == self.dummy_head.nxt == self.dummy_head.prev:
        print("\n\nYes, Doctor can go home.")
        print("\n#########################################\n")
    else:
        print("\n\nNo, Doctor can't go home.")
        print("\n#########################################\n")

  def ShowAllPatient(self):
    print("\n\nPatient/s in the waiting room:")
    print("\n#########################################\n")
    temp = self.dummy_head.nxt
    while temp != self.dummy_head:
        print(temp.name)
        temp = temp.nxt

  def ReverseTheLine(self):
      cur = self.dummy_head
      temp = None
      while temp != self.dummy_head:
          prev_of_cur = cur.prev
          nxt_of_cur = cur.nxt
          cur.nxt = prev_of_cur
          cur.prev = nxt_of_cur
          cur = cur.prev
          temp = cur
      print("\n\nSuccessfully reversed the line.")
      print("\n#########################################\n")


# Driver Code
cabin = WRM()
inpt = True
while inpt:
    print("Choice any one of the following options to execute:\n1. Add Patient\n2. Serve Patient\n3. Show All patients\n4. Can Doctor go Home?\n5. Cancel all Appointment\n6. ReverseTheLine\n7. Quit")
    inpt = int(input())
    if inpt == 1:
        id = int(input("Enter patient's id: "))
        name = input("Enter patient's name: ")
        age = int(input("Enter patient's age: "))
        bg = input("Enter patient's blood group: ")
        cabin.RegisterPatient(id, name, age, bg)
    elif inpt == 2:
        cabin.ServePatient()
    elif inpt == 3:
        cabin.ShowAllPatient()
    elif inpt == 4:
        cabin.CanDoctorGoHome()
    elif inpt == 5:
        cabin.CancelAll()
    elif inpt == 6:
        cabin.ReverseTheLine()
    elif inpt == 7:
        inpt = False

