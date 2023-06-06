import math
import sys

from peewee import *

from initialization import init

sys.path.append('../initialization/')

_config = init.InitClass().MysqlConfig
_db = MySQLDatabase(
    database=_config["database"],
    host=_config["host"],
    port=_config["port"],
    user=_config["user"],
    password=_config["password"],
)


class NaNField(FloatField):
    def db_value(self, value):
        if math.isnan(value):
            return -998
        else:
            return value

    def python_value(self, value):
        if value == -998:
            return float('nan')
        else:
            return value


class WellInfo(Model):
    """
    数据库与Code的映射表
    :func 初始化字段属性、添加单条数据、查找数据
    """
    WellName = CharField(max_length=200, null=True, verbose_name='井名')
    DEPTH = NaNField(verbose_name='DEPTH', null=True)
    Density = NaNField(verbose_name='密度', null=True)
    Viscosity = NaNField(verbose_name='粘度', null=True)
    WaterLoss = NaNField(verbose_name='失水', null=True)
    MudCake = NaNField(verbose_name='泥饼', null=True)
    GelInitial = NaNField(verbose_name='初切', null=True)
    GelFinal = NaNField(verbose_name='终切', null=True)
    PH = NaNField(verbose_name='PH', null=True)
    SandContent = NaNField(verbose_name='含砂', null=True)
    R600 = NaNField(verbose_name='r600', null=True)
    R300 = NaNField(verbose_name='r300', null=True)
    PV = NaNField(verbose_name='PV', null=True)
    YP = NaNField(verbose_name='YP', null=True)
    N = NaNField(verbose_name='N', null=True)
    K = NaNField(verbose_name='K', null=True)
    Cl = NaNField(verbose_name='Cl', null=True)
    AC = NaNField(verbose_name='AC', null=True)
    GR = NaNField(verbose_name='GR', null=True)
    DEN = NaNField(verbose_name='DEN', null=True)
    VP = NaNField(verbose_name='VP', null=True)
    VS = NaNField(verbose_name='VS', null=True)
    vsh = NaNField(verbose_name='vsh', null=True)
    SH = NaNField(verbose_name='SH', null=True)
    Ed = NaNField(verbose_name='Ed', null=True)
    Ud = NaNField(verbose_name='Ud', null=True)
    Es = NaNField(verbose_name='Es', null=True)
    Us = NaNField(verbose_name='Us', null=True)
    St = NaNField(verbose_name='St', null=True)
    C = NaNField(verbose_name='C', null=True)
    fai = NaNField(verbose_name='fai', null=True)
    G0 = NaNField(verbose_name='G0', null=True)
    DEN1 = NaNField(verbose_name='DEN1', null=True)
    Pp = NaNField(verbose_name='孔隙压力', null=True)
    MW_IN_ = NaNField(verbose_name='MW_IN_', null=True)
    MW_OUT = NaNField(verbose_name='MW_OUT', null=True)
    CON_IN = NaNField(verbose_name='CON_IN', null=True)
    CON_OUT = NaNField(verbose_name='CON_OUT', null=True)
    TMP_IN = NaNField(verbose_name='TMP_IN', null=True)
    TMP_OUT = NaNField(verbose_name='TMP_OUT', null=True)
    SUM = NaNField(verbose_name='SUM', null=True)
    ROP = NaNField(verbose_name='ROP', null=True)
    HKLD = NaNField(verbose_name='HKLD', null=True)
    WOB = NaNField(verbose_name='WOB', null=True)
    RPM = NaNField(verbose_name='RPM', null=True)
    SPP = NaNField(verbose_name='SPP', null=True)
    TRQ = NaNField(verbose_name='TRQ', null=True)
    Pump_1 = NaNField(verbose_name='Pump_1', null=True)
    Pump_2 = NaNField(verbose_name='Pump_2', null=True)
    FLOWIN = NaNField(verbose_name='FLOWIN', null=True)

    class Meta:
        database = _db
        table_name = 'wellinfo'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields = [field for field in self._meta.fields]

    # 添加信息

    def InsertWellInfo(self, map) -> bool:
        if len(map) <= 0:
            return False
        # for i in self.fields:
        #     if i == "id":
        #         continue
        #     if i not in map:
        #         map[i] = ""
        for k in map.keys():
            if k not in self.fields:
                try:
                    del map[k]
                except:
                    print(k)
        try:
            self.create(**map)
            return True
        except Exception as e:
            print(e)
            return False

    # 查找井名信息
    def FindWellInfoByName(self, wellname: str = "") -> list:
        if wellname == "":
            try:
                temp = list(self.select().dicts())
                return temp
            except Exception as e:
                print(e)
                return []
        else:
            try:
                temp = list(self.select().where(WellInfo.WellName == wellname).dicts())
                return temp
            except Exception as e:
                print(e)
                return []

    def fromDataToMap(self, datas: list) -> list[dict]:
        res = []
        for i in datas:
            map = {}
            for key in self.fields:
                map[key] = i[key]
            res.append(map)
        return res


if __name__ == "__main__":
    pass
