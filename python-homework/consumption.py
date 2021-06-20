# 016.md/2 hw's solution aka Consumption

print("Please reply below.")
print("Highway consumption / km (litre): ")
highway_c = int(input())      # országúti fogyasztás / km
print("Urban consumption / km (litre): ")
urban_c = int(input())        # városi fogyasztás / km
print("Highway distance (km): ")
highway_d = int(input())      # országúton megtett út (km)
print("Urban distance (km): ")
urban_d = int(input())        # városban megtett út (km)
print("The price of gasoline (HUF): ")
gasoline_pr = int(input())    # benzin ára (HUF)

# Mennyit fogyaszt az autód csak oda?
one_way = (highway_c * highway_d) + (urban_c * urban_d)
print("One-way consumption: %s" % one_way)

# És oda-vissza?
return_way = one_way * 2
print("Return way consumption: %s" % return_way)

# Mennyibe kerül a teljes út, ha ??? Ft a benzin?
cost = return_way * gasoline_pr
print("Total (return way) cost %s" % cost)
