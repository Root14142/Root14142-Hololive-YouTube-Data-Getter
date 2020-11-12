import datetime
import matplotlib.pyplot as plt
import YouTubeData

hololive_channels_list = []
hololive_channel_IDs = [
    # 0期生+α
    ["UCJFZiqLMntJufDCHc6bQixg",  # Hololive
     "UCp6993wxpyDPHUpavwDFqgg",  # ときのそら
     "UCDqI2jOz0weumE8s7paEk6g",  # ロボ子さん
     "UC-hM6YJuNYVAmUWxeIr9FeA",  # さくらみこ
     "UC5CwaMl1eIgY8h02uZw7u8A",  # 星街すいせい
     "UC0TXe_LYZ4scaW2XMyi5_kw"],  # AZKi
    # 1期生
    ["UCD8HOxPs4Xvsm8H0ZxXGiBw",  # 夜空メル
     "UCFTLzh12_nrtzqBPsTCqenA",  # アキ・ローゼンタール
     "UC1CfXB_kRs3C-zaeTG3oGyg",  # 赤井はあと
     "UCdn5BQ06XqgXoAxIhbqw5Rg",  # 白上フブキ
     "UCQ0UDLQCjY0rmuxCDE38FGg"],  # 夏色まつり
    # 2期生
    ["UC1opHUrw8rvnsadT-iGp7Cg",  # 湊あくあ
     "UCXTpFs_3PqI41qX2d9tL2Rw",  # 紫咲シオン
     "UC7fk0CB07ly8oSl0aqKkqFg",  # 百鬼あやめ
     "UC1suqwovbL1kzsoaZgFZLKg",  # 癒月ちょこ
     "UCvzGlP9oQwU--Y0r9id_jnA"],  # 大空スバル
    # ゲーマーズ
    ["UCp-5t9SrOQwXMU7iIjQfARg",  # 大神ミオ
     "UCvaTdHTWBGv3MKj3KVqJVCw",  # 猫又おかゆ
     "UChAnqc_AY5_I3Px5dig3X1Q"],  # 戌神ころね
    # 3期生
    ["UC1DCedRgGHBdm81E1llLhOQ",  # 兎田ぺこら
     "UCl_gCybOJRIgOXw6Qb4qJzQ",  # 潤羽るしあ
     "UCvInZx9h3jC2JzsIzoOebWg",  # 不知火フレア
     "UCdyqAaZDKHXg4Ahi7VENThQ",  # 白銀ノエル
     "UCCzUftO8KOVkV4wQG1vkUvg"],  # 宝鐘マリン
    # 4期生
    ["UCZlDXzGoo7d44bwdNObFacg",  # 天音かなた
     "UCS9uQI-jC3DE0L4IpXyvr6w",  # 桐生ココ
     "UCqm3BQLlJfvkTsX_hvm0UmA",  # 角巻わため
     "UC1uv2Oq6kNxgATlCiez59hw",  # 常闇トワ
     "UCa9Y57gfeY0Zro_noHRVrnw"],  # 姫森ルーナ
    # 5期生
    ["UCFKOVgVbGmX65RxO3EtH3iw",  # 雪花ラミィ
     "UCAWSyEs_Io8MtpY3m-zqILA",  # 桃鈴ねね
     "UCUKD-uaobj9jiqB-VXt71mA",  # 獅白ぼたん
     "UCK9V2B22uJYu3N7eR_BT9QA"],  # 尾丸ポルカ
    # Hololive-ID
    ["UCOyYb1c43VlX9rc_lT6NKQw",  # Ayunda Risu
     "UCP0BspO_AMEe3aQqqpo89Dg",  # Moona Hoshinova
     "UCAoy6rzhSf4ydcYjJw3WoVg"],  # Airani Iofifteen
    # Hololive-EN
    ["UCL_qhgtOy0dy1Agp8vkySQg",  # Mori Calliope
     "UCHsx4Hqa-1ORjQTh9TYDhww",  # Takanashi Kiara
     "UCMwGHR0BTZuLsmjY_NT5Pwg",  # Ninomae Ina'nis
     "UCoSrY_IQQVpmIRZ9Xf-y93g",  # Gawr Gura
     "UCyl1z3jo3XHR1riLFKG5UAg"]  # Watson Amelia
]
hololive_channel_names = [
    "hololive", "Tokino Sora", "Roboco", "Sakura Miko", "Hoshimachi Suisei", "AZKi",
    "Yozora Mel", "Aki Rosenthal", "Akai Haato", "Sirakami Fubuki", "Natsuiro Matsuri",
    "Minato Aqua", "Murasaki Shion", "Nakiri Ayame", "Yuzuki Choco", "Ozora Subaru",
    "Okami Mio", "Nekomata Okayu", "Inugami Korone",
    "Usada Pekora", "Uruha Rushia", "Shiranui Flare", "Hakugin Noel", "Houshou Marine",
    "Amane Kanata", "Kiryu Coco", "Tsunomaki Watame", "Tokoyami Towa", "Himemori Luna",
    "Yukihana Lamy", "Momosuzu Nene", "Shishiro Botan", "Omaru Polka",
    "Ayunda Risu", "Moona Hoshinova", "Airani Iofifteen",
    "Mori Calliope", "Takanashi Kiara", "Ninomae Ina'nis", "Gawr Gura", "Watson Amelia"
]


def create_img(sd_data_dict):
    fig = plt.figure(figsize=(16, 9), dpi=100)
    height = []
    label = []
    for o in range(len(sd_data_dict)):
        height.append(int(sd_data_dict[o][1]))
        label.append(sd_data_dict[o][0])
    left = range(len(height))
    plt.xlim(0, max(height) + 100000)
    plt.title("Hololive Subscribe Ranking In " + str(datetime.date.today()))
    plt.barh(left, height, tick_label=label, align="center", linewidth=7)
    for x in range(len(height)):
        plt.text(height[x], x, height[x], ha='left', va='center')
    return fig


def main():
    ID_dict = {}
    cut = 0
    for k in range(len(hololive_channel_IDs)):
        for l in range(len(hololive_channel_IDs[k])):
            ID_dict[hololive_channel_IDs[k][l]] = hololive_channel_names[cut]
            cut += 1

    for i in range(len(hololive_channel_IDs)):
        hololive_channels_list.append(",".join(hololive_channel_IDs[i]))

    data_dict = YouTubeData.main(ID_dict, hololive_channels_list)
    sd_data_dict = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

    img = create_img(sd_data_dict)
    return img
