from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def Lorenz(w,t,a,b,c):
    x,y,z = w
    return np.array([a * (y-x), x*(b-z) - y, x*y - c*z])

'''
Lorenz 混沌系统吸引子以及序列
# t = np.arange(0,30,0.01)
# track1 = odeint(Lorenz, (0.0,1.00,0.0), t, args=(10.0,28.0,3.0))
# track2 = odeint(Lorenz, (0.0,1.01,0.0), t, args=(10.0,28.0,3.0))
# print(track1)
#
# fig_3d = plt.figure()
# ax3D = Axes3D(fig_3d)
# ax3D.plot(track1[:,0],track1[:,1],track1[:,2],c='b')
# ax3D.plot(track2[:,0],track2[:,1],track2[:,2],c='g')
# # ax3D.view_init(45,60)
# ax3D.set_xlabel('X'), ax3D.set_ylabel('Y'), ax3D.set_zlabel('Z')
# # ax3D.set_xticks([-20,0,20]), ax3D.set_yticks([-50,0,50]), ax3D.set_zticks([0,6,12])
# plt.show()
'''


def D4_Hyper_Chaotic(u,t,a,b,c,d,e):
    x,y,z,w = u
    return np.array([a * (y-x), x*(b-z) - y + e*w, x*y - c*z + x**2, -1*d*y])

# t = np.arange(0,50,0.001)
# track1 = odeint(D4_Hyper_Chaotic, (100,100,100,100), t, args=(10,28,8/3,1,16))
# # track2 = odeint(D4_Hyper_Chaotic, (0.0,1.01,0.0,0.0), t, args=(10.0,28.0,8.0/3.0,1,16.0))
# print(track1)
#
# fig_3d = plt.figure()
# # plt.axes().set(facecolor = 'orange')
# ax3D = Axes3D(fig_3d)
# ax3D.plot(track1[:,0],track1[:,1],track1[:,2],c='b')
# # ax3D.plot(track2[:,0],track2[:,1],track2[:,2],c='g')
# # ax3D.view_init(0,60)
# ax3D.set_xlabel('x', fontdict={'family': 'Arial', 'size': '20'}), ax3D.set_ylabel('y', fontdict={'family': 'Arial', 'size': '20'}), ax3D.set_zlabel('z', fontdict={'family': 'Arial', 'size': '20'})
# plt.xticks(fontproperties = 'Arial', size = '18'), plt.yticks(fontproperties = 'Arial', size = '18'), plt.tick_params(labelsize=16)
# ax3D.patch.set_facecolor('none')
# # ax3D.set_alpha(0)
# # ax3D.w_xaxis.set_pane_color((0.0,0.0,0.0,0.0)), ax3D.w_yaxis.set_pane_color((0.0,0.0,0.0,0.0)), ax3D.w_zaxis.set_pane_color((0.0,0.0,0.0,0.0))
#
# plt.show()
# # plt.savefig(r'D:\2021\07. 外出会议\00. 第二届中国空间数据智能学术会议Spatial DI2021\Test.png', format='png',bbox_inches = 'tight', dpi = 600)
#
# plt.plot(track1[:,0],track1[:,1],c='b')
# plt.xlabel('x', fontdict={'family': 'Arial', 'size': '16'}), plt.ylabel('y', fontdict={'family': 'Arial', 'size': '16'})
# plt.xticks(fontproperties = 'Arial', size = '16'), plt.yticks(fontproperties = 'Arial', size = '16')
# plt.show()
#
#
# plt.plot(track1[:,0],track1[:,2],c='b')
# plt.xlabel('x', fontdict={'family': 'Arial', 'size': '16'}), plt.ylabel('z', fontdict={'family': 'Arial', 'size': '16'})
# plt.xticks(fontproperties = 'Arial', size = '16'), plt.yticks(fontproperties = 'Arial', size = '16')
# plt.show()
#
# plt.plot(track1[:,1],track1[:,2],c='b')
# plt.xlabel('x', fontdict={'family': 'Arial', 'size': '16'}), plt.ylabel('w', fontdict={'family': 'Arial', 'size': '16'})
# plt.xticks(fontproperties = 'Arial', size = '16'), plt.yticks(fontproperties = 'Arial', size = '16')
# plt.show()


# if __name__=='__main__':
#     a = hyperchaotic_system((0,1,1,0),10.0,28.0,8.0/3.0,1,16.0)
#     print(a)

