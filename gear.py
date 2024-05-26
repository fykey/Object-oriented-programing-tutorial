class Gear:
    def __init__(self, gear_type, num_gears):
        """
        Gearクラスの初期化メソッド

        Parameters:
        gear_type (str): ギアの種類（例: 'mountain', 'road'）
        num_gears (int): ギアの数
        """
        self.gear_type = gear_type
        self.num_gears = num_gears
        self.current_gear = 1

    def shift_up(self):
        """ギアを一段上げる"""
        if self.current_gear < self.num_gears:
            self.current_gear += 1
            print(f"ギアを{self.current_gear}に上げました。")
        else:
            print("これ以上ギアを上げることはできません。")

    def shift_down(self):
        """ギアを一段下げる"""
        if self.current_gear > 1:
            self.current_gear -= 1
            print(f"ギアを{self.current_gear}に下げました。")
        else:
            print("これ以上ギアを下げることはできません。")

    def get_current_gear(self):
        """現在のギアを取得する"""
        return self.current_gear

    def __str__(self):
        """オブジェクトの文字列表現を返す"""
        return f"Gear Type: {self.gear_type}, Number of Gears: {self.num_gears}, Current Gear: {self.current_gear}"