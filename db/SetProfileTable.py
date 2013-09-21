
from db.models import TankTempParams
from db.models import Temp
from db.models import Profile


def SetProfileTable(ForDay, ForTank)

   ParamSets = TankTempParams.objects.get(tank=ForTank)

   ParamSet = ParamSets.objets.get(start_time__gte = ForDay, end_time__lte = ForDay)
   if len(ParamSet) = 1:
      for TimePeriod in range(0,23):
         StartTime = ForDay.replace(hour=TimePeriod)
         EndTime = ForDay.replace(hour=TimePeriod,minute=59)

         TempReadings = Temp.objects.get(time__gte=StartTime time__lte=EndTime)
         SumTemp=0
         NumReadings=0
         for Reading in TempReadings:
            SumTemp=+ Reading.temp
            NumReadings=+1
         AveTemp = SumTemp/NumReadings
         
         LuxReadings = Lux.objects.get(time__gte=StartTime time__lte=EndTime)
         SumLux=0
         NumReadings=0
         for Reading in LuxReadings:
            SumLux=+ Reading.Lux
            NumReadings=+1
         AveLux = SumLux/NumReadings
         
         ProfileTargetEntry = Profile(tank=ForTank, time=ForDay.replace(hour=TimePeriod), temp=AveTemp lux=AveLux)



