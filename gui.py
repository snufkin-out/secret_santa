from PyQt6 import QtWidgets
import sys
import csv

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("⛇✩ Secret Santa ‧ by snufkin")
        self.resize(800, 700)

        # Set central widget and layout
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Create a container for participant fields
        self.participants_layout = QtWidgets.QVBoxLayout()

        # List to store participant input widgets (name and email)
        self.participant_widgets = []

        # Add first participant
        self.participant_count = 0
        self.add_participant()

        # Button to add more participants
        self.add_button = QtWidgets.QPushButton("Add Participant", self)
        self.add_button.clicked.connect(self.add_participant)

        # Button to generate CSV
        self.go_button = QtWidgets.QPushButton("Go", self)
        self.go_button.clicked.connect(self.generate_csv)

        # Add participant layout and buttons to main layout
        self.layout.addLayout(self.participants_layout)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.go_button)

        # Add a stretch to push items to the top
        self.layout.addStretch()

        self.show()

    def add_participant(self):
        self.participant_count += 1

        # Create a label for the participant number
        participant_label = QtWidgets.QLabel(f"Participant {self.participant_count}", self)
        self.participants_layout.addWidget(participant_label)

        # Create text fields for name and email
        name_box = QtWidgets.QLineEdit(self, placeholderText="Name")
        email_box = QtWidgets.QLineEdit(self, placeholderText="Email")
        
        # Set max size for text fields
        name_box.setMaximumSize(250, 25)
        email_box.setMaximumSize(250, 25)

        # Add name and email fields to the participant widgets list
        self.participant_widgets.append((name_box, email_box))

        # Add name and email to the participants layout
        self.participants_layout.addWidget(name_box)
        self.participants_layout.addWidget(email_box)

        # Add a thin line separator between participants
        line = QtWidgets.QFrame(self)
        line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.participants_layout.addWidget(line)

        # Add a bit of spacing below the line for cleaner separation
        self.participants_layout.addSpacing(10)

    def generate_csv(self):
        # Open or create the CSV file
        with open('participants.csv', mode='w', newline='') as file:
            writer = csv.writer(file)

            # Loop through each participant and write the name and email to the file
            for name_box, email_box in self.participant_widgets:
                name = name_box.text()
                email = email_box.text()
                writer.writerow([name, email])

        # Show a message box to indicate the CSV has been created
        QtWidgets.QMessageBox.information(self, "Success", "participants.csv file has been created.")

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec()
