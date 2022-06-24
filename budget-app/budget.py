class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = []
    self.balance = 0
  
  def __repr__(self):
    h = self.name.center(30,"*") + '\n'
    b = f = ''
    for i in self.ledger:    
      b += '{:<23}{:>7}'.format(i['description'][:23],"{:.2f}".format(i['amount'])[:7]) +"\n"    
    f += 'Total: {:.2f}'.format(self.balance)  
    return h+b+f
    
  def deposit(self,amount,description=""):
    self.ledger.append({'amount':amount,'description':description})
    self.balance += amount
    
  def withdraw(self,amount,description=""):
    if (self.balance - amount >= 0):
      self.ledger.append({'amount':-1*amount,'description':description})
      self.balance -= amount
      return True
    else:
      return False
    
  def get_balance(self):
    return self.balance

  def check_funds(self,amount):
    if self.balance >= amount:
      return True
    else:
      return False
  
  def transfer(self,amount,category):
    if(self.withdraw(amount,"Transfer to {}".format(category.name))):
      category.deposit(amount,'Transfer from {}'.format(self.name))
      return True
    else:
      return False
  
def create_spend_chart(categories):
  
  print_text = b = ''
  print_text+= 'Percentage spent by category' 
  
  spent_amount = []
  for category in categories:
    spent = 0
    for i in category.ledger:
      if i['amount'] < 0:
        spent += abs(i['amount'])
    spent_amount.append(round(spent,2))
  
  
  total_amount = round(sum(spent_amount),2)
  spent_percent = [int(i/total_amount *10 // 1 *10) for i in spent_amount]
  for i in range(100,-1,-10):
    l = "{:>3}| ".format(i)
    r = ''
    for j in range(len(spent_percent)):
      if spent_percent[j] == i:
        spent_percent[j] -= 10
        r += 'o  '
      else:
        r+='  '
      r+= ''
    print_text += '\n{}{}'.format(l,r)
  print_text += "\n{}{}".format(" "*4,"-"*(len(spent_percent)*3+1))
  f = ''
  max_char = max([len(i.name) for i in categories])
  name_category = ["{}{}".format(i.name," "*(max_char-len(i.name))) for i in categories]
  for i in range(max_char):
    f += "\n{}".format(" "*5)
    for j in range(len(spent_percent)):
        f += "{}  ".format(name_category[j][i])
  print_text += f
  return print_text