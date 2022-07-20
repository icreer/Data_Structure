from queue import Queue


def test(key,q):
    did_it_pass = False
    key_number1 = 0
    key_number2 = 0
    

    q_number1 = 0
    q_number2 = 0

    print(q)
    for s in range(4):
        
        if s < 2:
            
            key_number1 += key.queue[0]
            q_number1 += q.queue[0]
            key.get()
            q.get()
        else:
            key_number2 -= key.queue[0]
            key.get()
            q_number2 -= q.queue[0]
            q.get()

    try:
        key_final_number = key_number1 / key_number2
        q_final_number = q_number1 / q_number2
        if key_final_number == q_final_number and key_final_number != 0:
            did_it_pass = True
    except:
        i = 0
    
        return did_it_pass
key = Queue()
key.put(int(23))
key.put(4)
key.put(5)
key.put(23)
key.put(-10)

q1 = Queue()
q1.put(12)
q1.put(17)
q1.put(3)
q1.put(4)
q1.put(9)

q2 = Queue()
q2.put(3)
q2.put(6)
q2.put(7)
q2.put(12)
q2.put(15)

q3 = Queue()
q3.put(50)
q3.put(-8)
q3.put(-10)
q3.put(14)
q3.put(-27)


print(test(key,q1))
# True
print(test(key,q2))
# False
print(test(key,q3))
#True