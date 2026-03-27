import numpy as np
import numpy_financial as npf

# Use this if you don't have a BA II Plus

class Time_value:
    """ Financial Calculator.

            Args:
            pv (float):  Present value.
            fv (float):  Future value.
            rt (float):  Rate.
            pmt (float): Payment.
            prd (int):   Periods.
            cmp (int):   Compounding.
            ann (str):   When? 'end', 'begin'
            compt (str): Computation (pv, fv, rate, nper, pmt)
    """

    def __init__(self, pv, fv, rt, pmt, npr, cmp, ann, compt):
        self.pv = pv
        self.fv = fv
        self.rt = rt
        self.pmt = pmt
        self.npr = npr
        self.cmp = cmp # 1=Yearly, 4=Quarterly, 6=Semiannually
        self.ann = ann # str -> end, begin
        self.compt = compt

        self.npr *= self.cmp

    def __str__(self):
        return f'{self.pv}\n{self.fv}\n{self.rt}\n{self.pmt}\n{self.npr}\n{self.cmp}'

    def p_value(self):
        return npf.pv(fv=self.fv, rate=self.rt, nper=self.npr, pmt=self.pmt, when=self.ann)

    def f_value(self):
        return npf.fv(pv=self.pv, rate=self.rt, nper=self.npr, pmt=self.pmt, when=self.ann)

    def get_rate(self):
        return npf.rate(nper=self.npr, pmt=self.pmt, pv=self.pv, fv=self.fv, when=self.ann)

    def get_periods(self):
        if self.pmt == 0:
            return np.log(self.fv / -self.pv) / np.log(1 + self.rt)
        else:
            return npf.nper(rate=self.rt, pmt=self.pmt, pv=self.pv, fv=self.fv)

    def get_payment(self):
        return npf.pmt(pv=self.pv, fv=self.fv, rate=self.rt, nper=self.npr, when=self.ann)

    def compute(self):
        if self.compt == "pv":
            return self.p_value()
        elif self.compt == "fv":
            return self.f_value()
        elif self.compt == "rate":
            return self.get_rate()
        elif self.compt == "nper":
            return self.get_periods()
        elif self.compt == "pmt":
            return self.get_payment()
        return 'Something went wrong'

class Xtras:
    def __init__(self, pv, fv, rt, pmt, npr, cmp, ann, compt):
        self.pv = pv
        self.fv = fv
        self.rt = rt
        self.pmt = pmt
        self.npr = npr
        self.cmp = cmp # 1=Yearly, 4=Quarterly, 6=Semiannually
        self.ann = ann # str -> end, begin
        self.compt = compt

    def __str__(self):
            return f'{self.pv}\n{self.fv}\n{self.rt}\n{self.pmt}\n{self.npr}\n{self.cmp}'

    def perpetuity(self):
        return self.pmt / self.rt

    def growing_perpetuity(self, g_rate):
        return self.pmt / (self.rt - g_rate)

    def continuous_fv(self):
        e = 2.718
        return self.pv * (e ** (self.rt * self.npr))

    ### ... etc

if __name__ == "__main__":
    pv = -625
    fv = 1284
    rate = .06
    pmt = 0
    nper = 0
    cmp = 1
    ann = 'end'
    compt = 'nper'


    fcalc = Time_value(pv, fv, rate, pmt, nper, cmp, ann, compt)
    comp = fcalc.compute()
    print(comp)
