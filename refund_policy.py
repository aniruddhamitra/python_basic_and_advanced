
'''''
answer_a=int(input('How many days ago have you purchased the item?: '))
if answer_a < 10 :
    answer_b=input('Has the item broken down on its own [y/n]? :')
    answer_c=input('Have you used the item at all [y/n]?:  ')
    if answer_b =='y' and answer_c == 'n':
              print('You can get a refund')
    else:
        print('You cannot get a refund')
else:
    print ('You cannot get a refund')
    
    '''
answer_a=int(input('How many days ago have you purchased the item?: '))
answer_b=input('Has the item broken down on its own [y/n]? :')
answer_c=input('Have you used the item at all [y/n]?:  ')
if answer_a<=10 and  answer_b =='y' and answer_c == 'n':
              print('You can get a refund')
elif answer_a>=10 and  answer_b =='y' :
                 print('You can get a refund')
else:
    print ('You cannot get a refund')