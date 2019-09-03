# Addition of Vectors

heighy_weight_age = [70,170,400]

grades = [95,80,72,62]

def vector_add(v,w):
    return [v_i + w_i for v_i,w_i in zip(v,w)] 

def vector_dot(v,w):
    return [v_i * w_i for v_i,w_i in zip(v,w)] 

print(vector_add(heighy_weight_age,grades))

print(vector_dot(heighy_weight_age,grades))
