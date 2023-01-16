import matplotlib.pyplot as plt
import numpy as np

# x=np.linspace(0,2,20)
# y=np.linspace(5,9,20)
# plt.plot(x,y,'.-')
# plt.show()


# x=[1,8,13,45]
# y=[5,3,9,23]
# plt.plot(x,y,'o-')
# plt.show()


# x=np.linspace(0,2,20)
# y=x**2
# plt.plot(x,y,'.-')
# plt.show()


# x=np.linspace(-2,2,100)
# y=x**2
# plt.plot(x,y)
# plt.show()


# x=np.linspace(-2,2,100)
# y=x**3
# plt.plot(x,y)
# plt.show()


# x=np.linspace(-2,2,100)
# y=x**4
# plt.plot(x,y)
# plt.show()


# x=np.linspace(-2,2,100)
# y=x**2
# plt.subplot(1,3,1)
# plt.plot(x,y)

# x=np.linspace(-2,2,100)
# y=x**3
# plt.subplot(1,3,2)
# plt.plot(x,y)

# x=np.linspace(-2,2,100)
# y=x**4
# plt.subplot(1,3,3)
# plt.plot(x,y)

# plt.show()




# x=np.linspace(-2,2,100)
# y=x**2
# plt.subplot(2,3,1)
# plt.plot(x,y)

# x=np.linspace(-2,2,100)
# y=x**3
# plt.subplot(2,3,2)
# plt.plot(x,y)

# x=np.linspace(-2,2,100)
# y=x**4
# plt.subplot(2,3,3)
# plt.plot(x,y)

# plt.show()


# x=np.linspace(0,2*np.pi,100)
# y=np.sin(x)
# plt.subplot(1,4,1)
# plt.plot(x,y)


# x=np.linspace(0,2*np.pi,100)
# y=np.cos(x)
# plt.subplot(1,4,2)
# plt.plot(x,y)

# x=np.linspace(0,2*np.pi,100)
# y=np.tan(x)
# plt.subplot(1,4,3)
# plt.plot(x,y)

# # x=np.linspace(0,2*np.pi,100)
# # y=np.cot(x)
# # plt.subplot(1,4,4)
# # plt.plot(x,y)

# plt.show()

x=np.linspace(0,2*np.pi,100)
y=np.sin(x)
plt.subplot(1,4,1)
plt.plot(x,y)


x=np.linspace(0,2*np.pi,100)
y=np.cos(x)
plt.subplot(1,4,2)
plt.plot(x,y)

x=np.linspace(0,2*np.pi,100)
y=np.tan(x)
plt.subplot(1,4,3)
plt.plot(x,y)

# x=np.linspace(0,2*np.pi,100)
# y=np.cot(x)
# plt.subplot(1,4,4)
# plt.plot(x,y)

plt.show()