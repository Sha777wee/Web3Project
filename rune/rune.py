import sched
import time

from pydub.generators import Sine
from pydub.playback import play

from common.engine.btc_engine import BtcEngine
from common.engine.rune_engine import RuneEngine


def main():
    while True:
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(60, 1, get_real_date)
        scheduler.run()


def get_real_date():
    try:
        btc_data_engine = BtcEngine(symbol="btc", url="https://api2.runealpha.xyz/stats/btc-price")
        btc_tick_data = btc_data_engine.get_tick_data()
        cook_data_engine = RuneEngine(symbol="cook", url="https://api.runealpha.xyz/market/runes/c82970852")
        cook_tick_data = cook_data_engine.get_tick_data()
        psbts_data_engine = RuneEngine(symbol="psbts", url="https://api.runealpha.xyz/market/runes/c86d905a3")
        psbts_tick_data = psbts_data_engine.get_tick_data()
        x_data_engine = RuneEngine(symbol="x", url="https://api.runealpha.xyz/market/runes/c82a70d93")
        x_tick_data = x_data_engine.get_tick_data()
        goonfi_data_engine = RuneEngine(symbol="goonfi", url="https://api.runealpha.xyz/market/runes/c8ef40e7c")
        goonfi_tick_data = goonfi_data_engine.get_tick_data()

        print("====================================================================================")
        print(f"时间：{btc_tick_data.datetime.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"btc价格：${btc_tick_data.price}")
        print(f"cook价格:${round(cook_tick_data.price * btc_tick_data.price / 100000, 2)},{cook_tick_data.price}sats")
        print(f"psbts价格:${round(psbts_tick_data.price * btc_tick_data.price / 100000, 2)}")
        print(f"goonfi价格:${round(goonfi_tick_data.price * btc_tick_data.price / 100000, 2)}")
        print(f"x价格:${round((x_tick_data.price * btc_tick_data.price / 100000000) * 21, 2)}")

        # 生成一个持续时间为1秒的440 Hz的正弦波提示音
        if round(cook_tick_data.price * btc_tick_data.price / 100000, 2) < 150 or cook_tick_data.price < 270:
            tone = Sine(440).to_audio_segment(duration=100000)
            play(tone)
    except Exception as e:
        pass


if __name__ == "__main__":
    main()
