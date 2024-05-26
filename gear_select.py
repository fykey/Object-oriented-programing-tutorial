from gear import Gear

# インスタンス""mountain_bike_gear"を作成
mountain_bike_gear = Gear("mountain", 18) 
print(mountain_bike_gear.gear_type)
print(mountain_bike_gear.num_gears)

mountain_bike_gear.shift_up()
mountain_bike_gear.shift_up()
mountain_bike_gear.shift_down()
print(f"現在のギア: {mountain_bike_gear.get_current_gear()}")


road_bike_gear = Gear("road", 12)


road_bike_gear.shift_up()
road_bike_gear.shift_down()
print(f"現在のギア: {road_bike_gear.get_current_gear()}")

    