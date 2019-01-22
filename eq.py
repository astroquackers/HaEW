import numpy as np



def haew(ri,rHa,Av): 
	ri_mod = np.array([ -1.81734621e-01,   4.45990046e-06,   1.61342222e-01, 3.67158725e-01,   5.44852095e-01,   7.69352735e-01, 9.83821596e-01])
	rha_mod = np.array([  4.92785935e-02,   4.92407406e-06,   9.45875470e-02, 2.33535417e-01,   3.36037239e-01,   4.29700362e-01, 5.32009702e-01])
	ri0 = ri-(Av*0.2)
	rHa0 = rHa-(Av*0.07)
	rHa_predict = np.interp(ri0, ri_mod, rha_mod, left=None, right=None)
	rHa_excess = rHa0-rHa_predict
	Ha_excess = -(rHa_excess)-(0.03436211*rHa_excess*ri0)  - (0.02539148*rHa_excess**1.14049095)*(ri0**-0.027672421) -(0.03058978*(rHa_excess**3.01971529)*(ri0**0.43299475))
	a = -0.4*Ha_excess
	b = 10**a
	Eq = 107*(1-b)
	return Eq
