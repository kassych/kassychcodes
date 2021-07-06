hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

tota = mins+dura
yupy = int(tota/60)
end = tota % 60


print ("The meeting will end at-", (yupy+hour),end, sep = ':')
