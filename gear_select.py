from gear import Gear

# Gearクラスのインスタンスを作成し、動作をテストする
if __name__ == "__main__":
    mountain_bike_gear = Gear("mountain", 18)
    print(mountain_bike_gear)
    
    mountain_bike_gear.shift_up()
    mountain_bike_gear.shift_up()
    mountain_bike_gear.shift_down()
    print(f"現在のギア: {mountain_bike_gear.get_current_gear()}")
    print(mountain_bike_gear)

    road_bike_gear = Gear("road", 12)
    print(road_bike_gear)
    
    road_bike_gear.shift_up()
    road_bike_gear.shift_down()
    print(f"現在のギア: {road_bike_gear.get_current_gear()}")
    print(road_bike_gear)
    