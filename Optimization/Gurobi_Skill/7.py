import os
import gurobipy
import pandas as pd

class DEA(object):
	def __init__(self, DMUs_Name, X, Y, AP=False):
		self.m1, self.m1_name, self.m2, self.m2_name, self.AP = X.shape[1], X.columns.tolist(), Y.shape[1], Y.columns.tolist(), AP
		self.DMUs, self.X, self.Y = gurobipy.multidict({DMU: [X.loc[DMU].tolist(), Y.loc[DMU].tolist()] for DMU in DMUs_Name})
		print(f'DEA(AP={AP}) MODEL RUNING...')

	def __CCR(self):
		for k in self.DMUs:
			MODEL = gurobipy.Model()
			OE, lambdas, s_negitive, s_positive = MODEL.addVar(), MODEL.addVars(self.DMUs),  MODEL.addVars(self.m1), MODEL.addVars(self.m2)
			MODEL.update()
			MODEL.setObjectiveN(OE, index=0, priority=1)
			MODEL.setObjectiveN(-(sum(s_negitive) + sum(s_positive)), index=1, priority=0)
			MODEL.addConstrs(gurobipy.quicksum(lambdas[i] * self.X[i][j] for i in self.DMUs if i != k or not self.AP) + s_negitive[j] == OE * self.X[k][j] for j in range(self.m1))
			MODEL.addConstrs(gurobipy.quicksum(lambdas[i] * self.Y[i][j] for i in self.DMUs if i != k or not self.AP) - s_positive[j] == self.Y[k][j] for j in range(self.m2))
			MODEL.setParam('OutputFlag', 0)
			MODEL.optimize()
			self.Result.at[k, ('效益分析', '综合技术效益(CCR)')] = MODEL.objVal
		return self.Result

	def dea(self):
		columns_Page = ['效益分析'] * 3 + ['规模报酬分析'] * 2 + ['差额变数分析'] * (self.m1 + self.m2) + ['投入冗余率'] * self.m1 + ['产出不足率'] * self.m2
		columns_Group = ['技术效益(BCC)', '规模效益(CCR/BCC)', '综合技术效益(CCR)','有效性', '类型'] + (self.m1_name + self.m2_name) * 2
		self.Result = pd.DataFrame(index=self.DMUs, columns=[columns_Page, columns_Group])
		self.__CCR()
		return self.Result

	def analysis(self, path=None, name=None):
		Result = self.dea()
		file_path = os.path.join(os.path.expanduser("~"), 'Desktop') if path == None else r'../table'
		file_name = '\\DEA 数据包络分析报告.xlsx' if name == None else f'\\{name}.xlsx'
		Result.to_excel(file_path + file_name, 'DEA 数据包络分析报告')


if __name__ == '__main__':
	data = pd.DataFrame({1990: [14.40, 0.65, 31.30, 3621.00, 0.00], 1991: [16.90, 0.72, 32.20, 3943.00, 0.09],
		                 1992: [15.53, 0.72, 31.87, 4086.67, 0.07], 1993: [15.40, 0.76, 32.23, 4904.67, 0.13],
		                 1994: [14.17, 0.76, 32.40, 6311.67, 0.37], 1995: [13.33, 0.69, 30.77, 8173.33, 0.59],
		                 1996: [12.83, 0.61, 29.23, 10236.00, 0.51], 1997: [13.00, 0.63, 28.20, 12094.33, 0.44],
		                 1998: [13.40, 0.75, 28.80, 13603.33, 0.58], 1999: [14.00, 0.84, 29.10, 14841.00, 1.00]},
	                    index=['政府财政收入占 GDP 的比例/%', '环保投资占 GDP 的比例/%', '每千人科技人员数/人', '人均 GDP/元', '城市环境质量指数']).T

	X = data[['政府财政收入占 GDP 的比例/%', '环保投资占 GDP 的比例/%', '每千人科技人员数/人']]
	Y = data[['人均 GDP/元', '城市环境质量指数']]

	dea = DEA(DMUs_Name=data.index, X=X, Y=Y)
	dea.analysis()
	print(dea.dea())
