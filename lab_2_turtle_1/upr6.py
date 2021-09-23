import turtle as t

n = 12
t.shape('turtle')

for i in range(n):
    t.right(360/n)
    t.forward(200)
    t.stamp()
    t.backward(200)



