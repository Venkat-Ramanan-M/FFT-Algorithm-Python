print("FFT")
t=int(input("""
Enter
1 for DFT using DIT FFT
2 for IDFT using DIT FFT
3 for DFT using DIF FFT
4 for IDFT using DIF FFT
>>> 
"""))
if (t==1):
    #a1=[give input here]
    print()
    print("Enter 8 input seperated by Space ")
    a1= [complex(x) for x in input().split()]
    o=[0,4,2,6,1,5,3,7]
    a1= [a1[i] for i in o]
    print("Bit reversed input: ")
    print(a1)
    print()
    wp0=1
    wp1=(0.707-0.707j)
    wp2=(0-1j)
    wp3=(-0.707-0.707j)
    s5=[]
    s5.append(a1[0]+a1[1])
    s5.append(a1[0]-a1[1])
    s5.append(a1[2]+a1[3])
    s5.append(a1[2]-a1[3])
    s5.append(a1[4]+a1[5])
    s5.append(a1[4]-a1[5])
    s5.append(a1[6]+a1[7])
    s5.append(a1[6]-a1[7])
    print("Step1: ")
    print(s5)
    s6=[]
    s6.append(s5[0]+s5[2])
    s6.append(s5[1]+s5[3]*wp2)
    s6.append(s5[0]-s5[2])
    s6.append(s5[1]-s5[3]*wp2)
    s6.append(s5[4]+s5[6])
    s6.append(s5[5]+s5[7]*wp2)
    s6.append(s5[4]-s5[6])
    s6.append(s5[5]-s5[7]*wp2)
    print("Step2: ")
    print(s6)
    s7=[]
    s7.append(s6[0]+s6[4])
    s7.append(s6[1]+s6[5]*wp1)
    s7.append(s6[2]+s6[6]*wp2)
    s7.append(s6[3]+s6[7]*wp3)
    s7.append(s6[0]-s6[4])
    s7.append(s6[1]-s6[5]*wp1)
    s7.append(s6[2]-s6[6]*wp2)
    s7.append(s6[3]-s6[7]*wp3)
    print("Step3: ")
    print(s7)
    print()
    print("DFT using DIT FFT Algorithm: ")
    print(s7)
elif (t==2):
    print()
    print("Enter 8 input seperated by Space ")
    a1 = [complex(x) for x in input().split()]
    o = [0, 4, 2, 6, 1, 5, 3, 7]
    a1 = [a1[i] for i in o]
    print("Bit reversed input: ")
    print(a1)
    print()
    wp0 = 1
    wp1 = (0.707 + 0.707j)
    wp2 = (0 + 1j)
    wp3 = (-0.707 + 0.707j)
    s5 = []
    s5.append(a1[0] + a1[1])
    s5.append(a1[0] - a1[1])
    s5.append(a1[2] + a1[3])
    s5.append(a1[2] - a1[3])
    s5.append(a1[4] + a1[5])
    s5.append(a1[4] - a1[5])
    s5.append(a1[6] + a1[7])
    s5.append(a1[6] - a1[7])
    print("Step1: ")
    print(s5)
    s6 = []
    s6.append(s5[0] + s5[2])
    s6.append(s5[1] + s5[3] * wp2)
    s6.append(s5[0] - s5[2])
    s6.append(s5[1] - s5[3] * wp2)
    s6.append(s5[4] + s5[6])
    s6.append(s5[5] + s5[7] * wp2)
    s6.append(s5[4] - s5[6])
    s6.append(s5[5] - s5[7] * wp2)
    print("Step2: ")
    print(s6)
    s7 = []
    s7.append(s6[0] + s6[4])
    s7.append(s6[1] + s6[5] * wp1)
    s7.append(s6[2] + s6[6] * wp2)
    s7.append(s6[3] + s6[7] * wp3)
    s7.append(s6[0] - s6[4])
    s7.append(s6[1] - s6[5] * wp1)
    s7.append(s6[2] - s6[6] * wp2)
    s7.append(s6[3] - s6[7] * wp3)
    print("Step3: ")
    print(s7)
    s7 = [i / 8 for i in s7]
    print("step4 (dividing values by N):")
    print(s7)
    print()
    print("IDFT using DIT FFT Algorithm: ")
    print(s7)
elif (t==3):
    print("Enter 8 input seperated by Space")
    a= [complex(x) for x in input().split()]
    w0=1
    w1=(0.707-0.707j)
    w2=(0-1j)
    w3=(-0.707-.707j)
    #a=[]#<---Enter the values
    l=[]
    l1=[]
    l=a[0:4]
    l1=a[4:8]
    s1=[]
    s2=[]
    for i in range(0,4):
        s1.append(round((l[i]+l1[i]).real,3)+round((l[i]+l1[i]).imag,3)*1j)
    for i in range(0,4):
        s1.append(round((l[i]-l1[i]).real,3)+round((l[i]-l1[i]).imag,3)*1j)
    print("Step1: ")
    print(s1)
    a1=s1[0:2]
    a2=s1[2:4]
    x1=s1[4]*w0
    x2=s1[5]*w1
    x3=s1[6]*w2
    x4=s1[7]*w3
    for i in range(0,2):
        s2.append(a1[i]+a2[i])
    for i in range(0,2):
        s2.append(a1[i]-a2[i])
    s2.append(x1+x3)
    s2.append(x2+x4)
    s2.append(x1-x3)
    s2.append(x2-x4)
    print("Step2: ")
    print(s2)
    s3=[]
    x5=s2[2]*w0
    x6=s2[3]*w2
    x7=s2[6]*w0
    x8=s2[7]*w2
    s3.append(s2[0]+s2[1])
    s3.append(s2[0]-s2[1])
    s3.append(x5+x6)
    s3.append(x5-x6)
    s3.append(s2[4]+s2[5])
    s3.append(s2[4]-s2[5])
    s3.append(x7+x8)
    s3.append(x7-x8)
    print("Step3: ")
    print(s3)
    o = [0, 4, 2, 6, 1, 5, 3, 7]
    s5 = [s3[i] for i in o]
    print("Bit reversed final output:")
    print(s5)
    print()
    print("DFT using DIF FFT Algorithm: ")
    print(s5)
elif(t==4):
    print("Enter 8 input seperated by Space")
    a = [complex(x) for x in input().split()]
    w0 = 1
    w1 = (0.707 + 0.707j)
    w2 = (0 + 1j)
    w3 = (-0.707 + 0.707j)
    # a=[]#<---Enter the values
    l = []
    l1 = []
    l = a[0:4]
    l1 = a[4:8]
    s1 = []
    s2 = []
    for i in range(0, 4):
        s1.append(round((l[i] + l1[i]).real, 3) + round((l[i] + l1[i]).imag, 3) * 1j)
    for i in range(0, 4):
        s1.append(round((l[i] - l1[i]).real, 3) + round((l[i] - l1[i]).imag, 3) * 1j)
    print("Step1: ")
    print(s1)
    a1 = s1[0:2]
    a2 = s1[2:4]
    x1 = s1[4] * w0
    x2 = s1[5] * w1
    x3 = s1[6] * w2
    x4 = s1[7] * w3
    for i in range(0, 2):
        s2.append(a1[i] + a2[i])
    for i in range(0, 2):
        s2.append(a1[i] - a2[i])
    s2.append(x1 + x3)
    s2.append(x2 + x4)
    s2.append(x1 - x3)
    s2.append(x2 - x4)
    print("Step2: ")
    print(s2)
    s3 = []
    x5 = s2[2] * w0
    x6 = s2[3] * w2
    x7 = s2[6] * w0
    x8 = s2[7] * w2
    s3.append(s2[0] + s2[1])
    s3.append(s2[0] - s2[1])
    s3.append(x5 + x6)
    s3.append(x5 - x6)
    s3.append(s2[4] + s2[5])
    s3.append(s2[4] - s2[5])
    s3.append(x7 + x8)
    s3.append(x7 - x8)
    print("Step3: ")
    print(s3)
    s4 = [i / 8 for i in s3]
    print("step4 (dividing values by N):")
    print(s4)
    o = [0, 4, 2, 6, 1, 5, 3, 7]
    s5 = [s4[i] for i in o]
    print("Bit reversed final output:")
    print(s5)
    print()
    print("IDFT using DIF FFT Algorithm: ")
    print(s5)

