# -*- coding: utf-8 -*-
import pandas as pd

from repository import mysqlPo


def GenerateMap(df: pd.DataFrame, index: int, wellname: str) -> dict[str, any]:
    map = {"WellName": wellname}
    for i in df.columns:
        temp = i.replace(" ", "_")
        match i:
            case "密度":
                map["Density"] = df[i][index]
            case "粘度":
                map["Viscosity"] = df[i][index]
            case "失水":
                map["WaterLoss"] = df[i][index]
            case "泥饼":
                map["MudCake"] = df[i][index]
            case "初切":
                map["GelInitial"] = df[i][index]
            case "终切":
                map["GelFinal"] = df[i][index]
            case "含砂":
                map["SandContent"] = df[i][index]
            case "600":
                map["R600"] = df[i][index]
            case "300":
                map["R300"] = df[i][index]
            case "Cl-":
                map["Cl"] = df[i][index]
            case "孔隙压力":
                map["Pp"] = df[i][index]
            case _:
                map[temp] = df[i][index]
    return map


if __name__ == '__main__':
    # 创建表
    if not mysqlPo.WellInfo.table_exists():
        mysqlPo.WellInfo.create_table()
    # 创建MySql Client
    mysqlClient = mysqlPo.WellInfo()

    """
    插入示例：
    # 需要插入的数据字典
    map = {'WellName': '朝6-2x', 'DEPTH': 202, 'Density': 1.1, 'Viscosity': 36, 
            'WaterLoss': 10.0, 'MudCake': 1.0, 'GelInitial': 1, 'GelFinal': 2, 
            'PH': 9.0, 'SandContent': 0.5, 'R600': 32, 'R300': 19, 'PV': 13,
             'YP': 3.0, 'N': 0.75, 'K': 0.09, 'Cl': nan, 'AC': nan, 
             'GR': nan, 'DEN': nan, 'VP': nan, 'VS': nan, 'vsh': nan,
              'SH': nan, 'Ed': nan, 'Ud': nan, 'Es': nan, 'Us': nan,
               'St': nan, 'C': nan, 'fai': nan, 'G0': nan, 'DEN1': nan,
                'Pp': nan, 'MW_IN_': nan, 'MW_OUT': nan, 'CON_IN': nan, 
                'CON_OUT': nan, 'TMP_IN': nan, 'TMP_OUT': nan, 'SUM': nan,
                 'ROP': 1.1, 'HKLD': 293.61, 'WOB': 20.26, 'RPM': 87, 'SPP': 3.08,
                  'TRQ': 26.54, 'Pump_1': 0, 'Pump_2': 84, 'FLOWIN': 1.553}

    # 插入单条数据：
    status = mysqlClient.InsertWellInfo(map)
    
    status:返回是否成功插入。
    
    """

    """
    # 通过名称查询
    
    listN = mysqlClient.FindWellInfoByName("朝6-3x")  #为空，默认查询全部
    
    listN:
        [{'id': 2988, 'WellName': '朝6-3x', 'DEPTH': 3188.0, 'Density': 1.35, 'Viscosity': 67.0, 'WaterLoss': 3.6, 'MudCake': 0.5, 'GelInitial': 6.0, 'GelFinal': 12.0, 'PH': 9.0, 'SandContent': 0.2, 'R600': 86.0, 'R300': 63.0, 'PV': 23.0, 'YP': 20.0, 'N': 0.45, 'K': 1.93, 'Cl': nan, 'AC': 285.23, 'GR': 142.27, 'DEN': 2.4281, 'VP': 3.50594, 'VS': 1.84972, 'vsh': 1.08207, 'SH': 1.0, 'Ed': 21.7186, 'Ud': 0.307136, 'Es': 15.0802, 'Us': 0.260297, 'St': 83.3992, 'C': 25.7059, 'fai': 28.8154, 'G0': 2.30885, 'DEN1': 2.4281, 'Pp': 1.1137, 'MW_IN_': 1.58, 'MW_OUT': 1.58, 'CON_IN': 12.4, 'CON_OUT': 13.5, 'TMP_IN': 59.6, 'TMP_OUT': 63.2, 'SUM': 103.02, 'ROP': 9.0, 'HKLD': 931.05, 'WOB': 33.27, 'RPM': 82.0, 'SPP': 14.0, 'TRQ': 10.54, 'Pump_1': 0.0, 'Pump_2': 89.0, 'FLOWIN': 1.551}]
    或：
        [
         {'id': 1, 'WellName': '朝6-2x', 'DEPTH': 203.0, 'Density': 1.1, 'Viscosity': 36.0, 'WaterLoss': 10.0, 'MudCake': 1.0, 'GelInitial': 1.0, 'GelFinal': 2.0, 'PH': 9.0, 'SandContent': 0.5, 'R600': 32.0, 'R300': 19.0, 'PV': 13.0, 'YP': 3.0, 'N': 0.75, 'K': 0.09, 'Cl': nan, 'AC': nan, 'GR': nan, 'DEN': nan, 'VP': nan, 'VS': nan, 'vsh': nan, 'SH': nan, 'Ed': nan, 'Ud': nan, 'Es': nan, 'Us': nan, 'St': nan, 'C': nan, 'fai': nan, 'G0': nan, 'DEN1': nan, 'Pp': nan, 'MW_IN_': nan, 'MW_OUT': nan, 'CON_IN': nan, 'CON_OUT': nan, 'TMP_IN': nan, 'TMP_OUT': nan, 'SUM': nan, 'ROP': 1.9, 'HKLD': 281.14, 'WOB': 30.49, 'RPM': 87.0, 'SPP': 3.88, 'TRQ': 26.78, 'Pump_1': 0.0, 'Pump_2': 84.0, 'FLOWIN': 1.514},
         {'id': 2, 'WellName': '朝6-2x', 'DEPTH': 202.0, 'Density': 1.1, 'Viscosity': 36.0, 'WaterLoss': 10.0, 'MudCake': 1.0, 'GelInitial': 1.0, 'GelFinal': 2.0, 'PH': 9.0, 'SandContent': 0.5, 'R600': 32.0, 'R300': 19.0, 'PV': 13.0, 'YP': 3.0, 'N': 0.75, 'K': 0.09, 'Cl': nan, 'AC': nan, 'GR': nan, 'DEN': nan, 'VP': nan, 'VS': nan, 'vsh': nan, 'SH': nan, 'Ed': nan, 'Ud': nan, 'Es': nan, 'Us': nan, 'St': nan, 'C': nan, 'fai': nan, 'G0': nan, 'DEN1': nan, 'Pp': nan, 'MW_IN_': nan, 'MW_OUT': nan, 'CON_IN': nan, 'CON_OUT': nan, 'TMP_IN': nan, 'TMP_OUT': nan, 'SUM': nan, 'ROP': 1.1, 'HKLD': 293.61, 'WOB': 20.26, 'RPM': 87.0, 'SPP': 3.08, 'TRQ': 26.54, 'Pump_1': 0.0, 'Pump_2': 84.0, 'FLOWIN': 1.553}
         ]

进程已结束,退出代码0

    """
    listN = mysqlClient.FindWellInfoByName()

    print(listN[:2])

    # df = pd.read_excel("朝6-2x.xlsx")
    # for i in range(len(df)):
    #     try:
    #         map = GenerateMap(df, i, "朝6-2x")
    #         status = mysqlClient.InsertWellInfo(map)
    #         if not status:
    #             print("第%d条数据插入失败" % (i + 1))
    #     except Exception as e:
    #         print(e)
