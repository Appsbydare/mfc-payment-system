import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTabWidget, QLabel, QPushButton, 
                             QTableWidget, QTableWidgetItem, QLineEdit, 
                             QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit,
                             QGroupBox, QGridLayout, QFormLayout, QFrame,
                             QFileDialog, QProgressBar, QDateEdit, QCheckBox,
                             QScrollArea, QSplitter, QTreeWidget, QTreeWidgetItem)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont, QPixmap, QIcon


class MFCPaymentSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Malta Fight Co. - Payment Automation System")
        self.setGeometry(100, 100, 1400, 900)
        
        # Set Impact font for headers
        self.header_font = QFont("Impact", 16)
        self.subheader_font = QFont("Impact", 12)
        self.normal_font = QFont("Arial", 10)
        
        # Theme settings
        self.dark_theme = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create top bar with theme toggle
        top_bar = QHBoxLayout()
        top_bar.addStretch()
        
        theme_label = QLabel("Dark Theme:")
        theme_toggle = QCheckBox()
        theme_toggle.toggled.connect(self.toggle_theme)
        
        top_bar.addWidget(theme_label)
        top_bar.addWidget(theme_toggle)
        
        # Create tab widget
        self.tab_widget = QTabWidget()
        
        # Create tabs
        self.dashboard_tab = self.create_dashboard_tab()
        self.data_import_tab = self.create_data_import_tab()
        self.rule_manager_tab = self.create_rule_manager_tab()
        self.payment_calculator_tab = self.create_payment_calculator_tab()
        self.reports_tab = self.create_reports_tab()
        self.settings_tab = self.create_settings_tab()
        
        # Add tabs to widget
        self.tab_widget.addTab(self.dashboard_tab, "Dashboard")
        self.tab_widget.addTab(self.data_import_tab, "Data Import")
        self.tab_widget.addTab(self.rule_manager_tab, "Rule Manager")
        self.tab_widget.addTab(self.payment_calculator_tab, "Payment Calculator")
        self.tab_widget.addTab(self.reports_tab, "Reports")
        self.tab_widget.addTab(self.settings_tab, "Settings")
        
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_bar)
        main_layout.addWidget(self.tab_widget)
        central_widget.setLayout(main_layout)
        
        # Apply initial theme
        self.apply_theme()

    def toggle_theme(self, checked):
        self.dark_theme = checked
        self.apply_theme()
        # Recreate the dashboard to apply theme to stat cards
        self.recreate_dashboard()
    
    def recreate_dashboard(self):
        # Remove the existing dashboard tab
        self.tab_widget.removeTab(0)
        # Create new dashboard with current theme
        self.dashboard_tab = self.create_dashboard_tab()
        # Insert it back at position 0
        self.tab_widget.insertTab(0, self.dashboard_tab, "Dashboard")
        # Set focus back to dashboard
        self.tab_widget.setCurrentIndex(0)

    def apply_theme(self):
        if self.dark_theme:
            # Dark theme
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QTabWidget::pane {
                    border: 1px solid #555555;
                    background-color: #3c3c3c;
                }
                QTabBar::tab {
                    background-color: #555555;
                    color: #ffffff;
                    padding: 8px 16px;
                    margin-right: 2px;
                }
                QTabBar::tab:selected {
                    background-color: #2E86AB;
                }
                QGroupBox {
                    background-color: #3c3c3c;
                    border: 1px solid #555555;
                    color: #ffffff;
                    font-weight: bold;
                    padding-top: 15px;
                }
                QGroupBox::title {
                    color: #ffffff;
                }
                QWidget {
                    background-color: #3c3c3c;
                    color: #ffffff;
                }
                QTableWidget {
                    background-color: #4a4a4a;
                    gridline-color: #666666;
                }
                QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {
                    background-color: #555555;
                    border: 1px solid #777777;
                    color: #ffffff;
                    padding: 5px;
                }
                QPushButton {
                    background-color: #2E86AB;
                    color: white;
                    border: none;
                    padding: 8px;
                    font-weight: normal;
                }
                QPushButton:hover {
                    background-color: #3a9bc1;
                }
            """)
        else:
            # Light theme
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #f0f0f0;
                    color: #000000;
                }
                QPushButton {
                    background-color: #2E86AB;
                    color: white;
                    border: none;
                    padding: 8px;
                    font-weight: normal;
                }
                QPushButton:hover {
                    background-color: #3a9bc1;
                }
            """)

    def create_dashboard_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("Malta Fight Co. - Dashboard")
        header.setFont(QFont("Impact", 24))
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("color: #2E86AB; margin: 20px;")
        layout.addWidget(header)
        
        # Current month info
        month_group = QGroupBox()
        month_layout = QVBoxLayout()
        
        # Month selector
        month_info = QHBoxLayout()
        month_label = QLabel("Current Processing Month")
        month_label.setFont(QFont("Impact", 14))
        month_edit = QDateEdit()
        month_edit.setDate(QDate.currentDate())
        month_edit.setMinimumHeight(40)
        month_info.addWidget(month_label)
        month_info.addWidget(month_edit)
        month_info.addStretch()
        
        month_layout.addLayout(month_info)
        
        # Enhanced stat cards with full width
        stats_container = QWidget()
        stats_layout = QGridLayout()
        stats_layout.setSpacing(15)
        
        # Create 6 stat cards in 2 rows, 3 columns for maximum width usage
        self.create_enhanced_stat_card(stats_layout, "Total Attendances", "287", "#E74C3C", 0, 0)
        self.create_enhanced_stat_card(stats_layout, "Total Revenue", "€4,256.30", "#27AE60", 0, 1)
        self.create_enhanced_stat_card(stats_layout, "Coaches to Pay", "11", "#3498DB", 0, 2)
        self.create_enhanced_stat_card(stats_layout, "Pending Calculations", "23", "#F39C12", 1, 0)
        self.create_enhanced_stat_card(stats_layout, "BGM Payment", "€1,276.89", "#9B59B6", 1, 1)
        self.create_enhanced_stat_card(stats_layout, "Management Pay", "€361.78", "#1ABC9C", 1, 2)
        
        stats_container.setLayout(stats_layout)
        month_layout.addWidget(stats_container)
        
        month_group.setLayout(month_layout)
        layout.addWidget(month_group)
        
        # Quick actions
        actions_group = QGroupBox()
        actions_group.setTitle("Quick Actions")
        actions_layout = QHBoxLayout()
        
        import_btn = QPushButton("Import Monthly Data")
        import_btn.setMinimumHeight(60)
        import_btn.setFont(QFont("Impact", 12))
        import_btn.setStyleSheet("font-weight: normal;")
        calculate_btn = QPushButton("Calculate Payments")
        calculate_btn.setMinimumHeight(60)
        calculate_btn.setFont(QFont("Impact", 12))
        calculate_btn.setStyleSheet("font-weight: normal;")
        generate_btn = QPushButton("Generate Reports")
        generate_btn.setMinimumHeight(60)
        generate_btn.setFont(QFont("Impact", 12))
        generate_btn.setStyleSheet("font-weight: normal;")
        
        actions_layout.addWidget(import_btn)
        actions_layout.addWidget(calculate_btn)
        actions_layout.addWidget(generate_btn)
        actions_group.setLayout(actions_layout)
        layout.addWidget(actions_group)
        
        # Recent activity
        activity_group = QGroupBox()
        activity_group.setTitle("Recent Activity")
        activity_layout = QVBoxLayout()
        
        activity_list = QTextEdit()
        activity_list.setMaximumHeight(200)
        activity_list.setPlainText("""
        [2025-06-05 14:30] May attendance data imported (608 records)
        [2025-06-05 14:25] Payment rules updated for "Adult 10 Pack"
        [2025-06-05 12:15] Historical payment data refreshed (667 records)
        [2025-06-04 16:45] April payments calculated successfully
        [2025-06-04 16:40] Payslips generated for all coaches
        """)
        activity_layout.addWidget(activity_list)
        activity_group.setLayout(activity_layout)
        layout.addWidget(activity_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def create_enhanced_stat_card(self, layout, title, value, border_color, row, col):
        card = QFrame()
        card.setFrameStyle(QFrame.Box)
        card.setLineWidth(3)
        
        # Dynamic background and text colors based on theme
        if self.dark_theme:
            bg_color = "rgba(60, 60, 60, 0.95)"
            title_color = "#ffffff"
            value_color = "#ffffff"
        else:
            bg_color = "rgba(255, 255, 255, 0.95)"
            title_color = "#333333"
            value_color = border_color
            
        card.setStyleSheet(f"""
            QFrame {{
                border: 3px solid {border_color};
                border-radius: 10px;
                background-color: {bg_color};
                margin: 5px;
                padding: 10px;
            }}
        """)
        
        card_layout = QVBoxLayout()
        card_layout.setAlignment(Qt.AlignCenter)
        card_layout.setContentsMargins(5, 5, 5, 5)
        card_layout.setSpacing(5)
        
        title_label = QLabel(title)
        title_label.setFont(QFont("Impact", 18))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setWordWrap(True)
        title_label.setStyleSheet(f"""
            color: {title_color}; 
            border: none; 
            background: transparent;
            margin: 0px;
            padding: 5px;
        """)
        
        value_label = QLabel(value)
        value_label.setFont(QFont("Impact", 36))
        value_label.setAlignment(Qt.AlignCenter)
        value_label.setStyleSheet(f"""
            color: {value_color}; 
            border: none; 
            background: transparent;
            margin: 0px;
            padding: 5px;
        """)
        
        card_layout.addWidget(title_label)
        card_layout.addWidget(value_label)
        card.setLayout(card_layout)
        
        # Set minimum height for consistent appearance
        card.setMinimumHeight(140)
        
        layout.addWidget(card, row, col)

    def create_data_import_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("Data Import Manager")
        header.setFont(self.header_font)
        layout.addWidget(header)
        
        # Import sections
        splitter = QSplitter(Qt.Vertical)
        
        # Attendance data import
        attendance_group = QGroupBox()
        attendance_group.setTitle("Monthly Attendance Data (GoTeamUp Export)")
        attendance_layout = QVBoxLayout()
        
        # File selection
        file_layout = QHBoxLayout()
        attendance_file = QLineEdit()
        attendance_file.setPlaceholderText("Select May Attendances.csv file...")
        browse_btn1 = QPushButton("Browse")
        file_layout.addWidget(attendance_file)
        file_layout.addWidget(browse_btn1)
        attendance_layout.addLayout(file_layout)
        
        # Preview table
        attendance_preview = QTableWidget(5, 11)
        attendance_preview.setHorizontalHeaderLabels([
            "Customer", "Email", "Date", "Time", "Class Type", 
            "Venue", "Instructors", "Booking Method", "Membership", 
            "Booking Source", "Status"
        ])
        # Sample data
        sample_attendance = [
            ["John Smith", "john@email.com", "2025-05-01", "18:00", "Boxing", "Main Gym", "Alice", "Adult 10 Pack", "Adult 10 Pack", "App", "Attended"],
            ["Sarah Johnson", "sarah@email.com", "2025-05-01", "19:00", "Kickboxing", "Main Gym", "Bob", "Monthly Unlimited", "Monthly Unlimited", "Web", "Attended"],
            ["Mike Wilson", "mike@email.com", "2025-05-02", "17:30", "MMA", "Mat Room", "Charlie", "Drop-in", "Single Session", "Phone", "Attended"]
        ]
        for row, data in enumerate(sample_attendance):
            for col, value in enumerate(data):
                attendance_preview.setItem(row, col, QTableWidgetItem(value))
        
        attendance_layout.addWidget(attendance_preview)
        attendance_group.setLayout(attendance_layout)
        splitter.addWidget(attendance_group)
        
        # Historical payment data import
        payment_group = QGroupBox()
        payment_group.setTitle("Historical Payment Data (All Time)")
        payment_layout = QVBoxLayout()
        
        # File selection
        file_layout2 = QHBoxLayout()
        payment_file = QLineEdit()
        payment_file.setPlaceholderText("Select Historical Payment Data.csv file...")
        browse_btn2 = QPushButton("Browse")
        file_layout2.addWidget(payment_file)
        file_layout2.addWidget(browse_btn2)
        payment_layout.addLayout(file_layout2)
        
        # Preview table
        payment_preview = QTableWidget(5, 5)
        payment_preview.setHorizontalHeaderLabels([
            "Date", "Customer", "Memo", "Amount", "Invoice"
        ])
        # Sample data
        sample_payment = [
            ["2025-03-25", "John Smith", "Adult 10 Pack Pay As You Go", "112.20", "12345"],
            ["2025-04-15", "Sarah Johnson", "Monthly Unlimited Adult", "89.50", "12346"],
            ["2025-05-01", "Mike Wilson", "Single Session Adult", "15.00", "12347"]
        ]
        for row, data in enumerate(sample_payment):
            for col, value in enumerate(data):
                payment_preview.setItem(row, col, QTableWidgetItem(str(value)))
        
        payment_layout.addWidget(payment_preview)
        payment_group.setLayout(payment_layout)
        splitter.addWidget(payment_group)
        
        layout.addWidget(splitter)
        
        # Import controls
        controls_layout = QHBoxLayout()
        validate_btn = QPushButton("Validate Data")
        import_btn = QPushButton("Import Data")
        progress_bar = QProgressBar()
        
        controls_layout.addWidget(validate_btn)
        controls_layout.addWidget(import_btn)
        controls_layout.addWidget(progress_bar)
        layout.addLayout(controls_layout)
        
        # Import status
        status_text = QTextEdit()
        status_text.setMaximumHeight(100)
        status_text.setPlainText("Ready to import data. Please select files and click Validate Data.")
        layout.addWidget(status_text)
        
        widget.setLayout(layout)
        return widget

    def create_rule_manager_tab(self):
        widget = QWidget()
        layout = QHBoxLayout()
        
        # Left panel - Membership types list
        left_panel = QWidget()
        left_layout = QVBoxLayout()
        
        left_header = QLabel("Membership Types")
        left_header.setFont(self.subheader_font)
        left_layout.addWidget(left_header)
        
        # Search
        search_box = QLineEdit()
        search_box.setPlaceholderText("Search membership types...")
        left_layout.addWidget(search_box)
        
        # Membership list
        membership_tree = QTreeWidget()
        membership_tree.setHeaderLabel("Membership Categories")
        
        # Sample membership categories
        group_classes = QTreeWidgetItem(["Group Classes"])
        group_classes.addChild(QTreeWidgetItem(["Adult 10 Pack Pay As You Go"]))
        group_classes.addChild(QTreeWidgetItem(["Adult 5 Pack Pay As You Go"]))
        group_classes.addChild(QTreeWidgetItem(["Monthly Unlimited Adult"]))
        group_classes.addChild(QTreeWidgetItem(["Student 10 Pack"]))
        group_classes.addChild(QTreeWidgetItem(["Youth Boxing (13-17)"]))
        
        private_sessions = QTreeWidgetItem(["Private Sessions"])
        private_sessions.addChild(QTreeWidgetItem(["1-on-1 Training"]))
        private_sessions.addChild(QTreeWidgetItem(["Semi-Private (2 people)"]))
        private_sessions.addChild(QTreeWidgetItem(["Personal Training Package"]))
        
        membership_tree.addTopLevelItem(group_classes)
        membership_tree.addTopLevelItem(private_sessions)
        membership_tree.expandAll()
        
        left_layout.addWidget(membership_tree)
        
        # Add new membership button
        add_btn = QPushButton("Add New Membership Type")
        left_layout.addWidget(add_btn)
        
        left_panel.setLayout(left_layout)
        left_panel.setMaximumWidth(300)
        
        # Right panel - Rule details
        right_panel = QWidget()
        right_layout = QVBoxLayout()
        
        right_header = QLabel("Membership Rules Configuration")
        right_header.setFont(self.subheader_font)
        right_layout.addWidget(right_header)
        
        # Scroll area for form
        scroll = QScrollArea()
        form_widget = QWidget()
        form_layout = QFormLayout()
        
        # Basic info
        basic_group = QGroupBox("Basic Information")
        basic_layout = QFormLayout()
        
        membership_name = QLineEdit("Adult 10 Pack Pay As You Go")
        category_combo = QComboBox()
        category_combo.addItems(["Group Classes", "Private Sessions"])
        price_edit = QDoubleSpinBox()
        price_edit.setMaximum(9999.99)
        price_edit.setValue(112.20)
        price_edit.setSuffix(" €")
        
        sessions_count = QSpinBox()
        sessions_count.setMaximum(999)
        sessions_count.setValue(10)
        
        basic_layout.addRow("Membership Name:", membership_name)
        basic_layout.addRow("Category:", category_combo)
        basic_layout.addRow("Price:", price_edit)
        basic_layout.addRow("Number of Sessions:", sessions_count)
        basic_group.setLayout(basic_layout)
        
        # Payment splits
        splits_group = QGroupBox("Payment Split Percentages")
        splits_layout = QFormLayout()
        
        coach_split = QDoubleSpinBox()
        coach_split.setMaximum(100.0)
        coach_split.setValue(43.5)
        coach_split.setSuffix(" %")
        
        bgm_split = QDoubleSpinBox()
        bgm_split.setMaximum(100.0)
        bgm_split.setValue(30.0)
        bgm_split.setSuffix(" %")
        
        management_split = QDoubleSpinBox()
        management_split.setMaximum(100.0)
        management_split.setValue(8.5)
        management_split.setSuffix(" %")
        
        mfc_split = QDoubleSpinBox()
        mfc_split.setMaximum(100.0)
        mfc_split.setValue(18.0)
        mfc_split.setSuffix(" %")
        
        splits_layout.addRow("Coach %:", coach_split)
        splits_layout.addRow("BGM (Landlord) %:", bgm_split)
        splits_layout.addRow("Management %:", management_split)
        splits_layout.addRow("MFC Retained %:", mfc_split)
        splits_group.setLayout(splits_layout)
        
        # Special rules
        special_group = QGroupBox("Special Rules & Exceptions")
        special_layout = QFormLayout()
        
        is_private = QCheckBox()
        allow_discount = QCheckBox()
        allow_discount.setChecked(True)
        tax_exempt = QCheckBox()
        
        special_layout.addRow("Private Session:", is_private)
        special_layout.addRow("Allow Discounts:", allow_discount)
        special_layout.addRow("Tax Exempt:", tax_exempt)
        
        notes_edit = QTextEdit()
        notes_edit.setMaximumHeight(100)
        notes_edit.setPlainText("Standard adult group class package. 10 sessions valid for 3 months.")
        special_layout.addRow("Notes:", notes_edit)
        special_group.setLayout(special_layout)
        
        # Add all groups to form
        form_layout.addRow(basic_group)
        form_layout.addRow(splits_group)
        form_layout.addRow(special_group)
        
        form_widget.setLayout(form_layout)
        scroll.setWidget(form_widget)
        scroll.setWidgetResizable(True)
        right_layout.addWidget(scroll)
        
        # Action buttons
        buttons_layout = QHBoxLayout()
        save_btn = QPushButton("Save Rules")
        delete_btn = QPushButton("Delete Membership")
        reset_btn = QPushButton("Reset Changes")
        
        buttons_layout.addWidget(save_btn)
        buttons_layout.addWidget(delete_btn)
        buttons_layout.addStretch()
        buttons_layout.addWidget(reset_btn)
        right_layout.addLayout(buttons_layout)
        
        right_panel.setLayout(right_layout)
        
        # Add panels to main layout
        layout.addWidget(left_panel)
        layout.addWidget(right_panel)
        
        widget.setLayout(layout)
        return widget

    def create_payment_calculator_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("Monthly Payment Calculator")
        header.setFont(self.header_font)
        layout.addWidget(header)
        
        # Month selection and controls
        controls_group = QGroupBox("Calculation Controls")
        controls_layout = QHBoxLayout()
        
        month_label = QLabel("Processing Month:")
        month_label.setFont(self.subheader_font)
        month_selector = QDateEdit()
        month_selector.setDate(QDate.currentDate())
        
        calculate_btn = QPushButton("Calculate All Payments")
        calculate_btn.setMinimumHeight(40)
        export_btn = QPushButton("Export Results")
        
        controls_layout.addWidget(month_label)
        controls_layout.addWidget(month_selector)
        controls_layout.addStretch()
        controls_layout.addWidget(calculate_btn)
        controls_layout.addWidget(export_btn)
        controls_group.setLayout(controls_layout)
        layout.addWidget(controls_group)
        
        # Results tabs
        results_tabs = QTabWidget()
        
        # Coach payments tab
        coach_tab = QWidget()
        coach_layout = QVBoxLayout()
        
        coach_header = QLabel("Coach Payment Summary")
        coach_header.setFont(self.subheader_font)
        coach_layout.addWidget(coach_header)
        
        coach_table = QTableWidget(11, 6)
        coach_table.setHorizontalHeaderLabels([
            "Coach Name", "Classes Taught", "Total Students", "Gross Revenue", "Coach Payment", "Details"
        ])
        
        # Sample coach data
        coach_data = [
            ["Alice Smith", "23", "156", "€1,245.30", "€541.70", "View"],
            ["Bob Johnson", "18", "124", "€987.60", "€429.50", "View"],
            ["Charlie Wilson", "15", "98", "€756.40", "€329.03", "View"],
            ["Diana Garcia", "12", "87", "€634.20", "€275.88", "View"],
            ["Eva Martinez", "20", "145", "€1,123.80", "€488.85", "View"]
        ]
        
        for row, data in enumerate(coach_data):
            for col, value in enumerate(data):
                if col == 5:  # Details button
                    btn = QPushButton("View Details")
                    coach_table.setCellWidget(row, col, btn)
                else:
                    coach_table.setItem(row, col, QTableWidgetItem(value))
        
        coach_layout.addWidget(coach_table)
        coach_tab.setLayout(coach_layout)
        
        # BGM payments tab
        bgm_tab = QWidget()
        bgm_layout = QVBoxLayout()
        
        bgm_header = QLabel("BGM (Landlord) Payment Summary")
        bgm_header.setFont(self.subheader_font)
        bgm_layout.addWidget(bgm_header)
        
        bgm_summary = QLabel("Total BGM Payment for May 2025: €1,276.89")
        bgm_summary.setFont(QFont("Impact", 14))
        bgm_summary.setStyleSheet("color: #2E86AB; padding: 20px;")
        bgm_layout.addWidget(bgm_summary)
        
        bgm_table = QTableWidget(5, 4)
        bgm_table.setHorizontalHeaderLabels([
            "Revenue Source", "Total Revenue", "BGM Percentage", "BGM Payment"
        ])
        
        bgm_data = [
            ["Group Classes", "€3,456.78", "30%", "€1,037.03"],
            ["Private Sessions", "€1,598.40", "15%", "€239.76"],
            ["Semi-Private", "€234.50", "15%", "€35.18"],
        ]
        
        for row, data in enumerate(bgm_data):
            for col, value in enumerate(data):
                bgm_table.setItem(row, col, QTableWidgetItem(value))
        
        bgm_layout.addWidget(bgm_table)
        bgm_tab.setLayout(bgm_layout)
        
        # Management payments tab
        mgmt_tab = QWidget()
        mgmt_layout = QVBoxLayout()
        
        mgmt_header = QLabel("Management Payment Summary")
        mgmt_header.setFont(self.subheader_font)
        mgmt_layout.addWidget(mgmt_header)
        
        mgmt_summary = QLabel("Total Management Payment for May 2025: €361.78")
        mgmt_summary.setFont(QFont("Impact", 14))
        mgmt_summary.setStyleSheet("color: #2E86AB; padding: 20px;")
        mgmt_layout.addWidget(mgmt_summary)
        
        mgmt_table = QTableWidget(3, 4)
        mgmt_table.setHorizontalHeaderLabels([
            "Revenue Source", "Total Revenue", "Management %", "Management Payment"
        ])
        
        mgmt_data = [
            ["Group Classes", "€3,456.78", "8.5%", "€293.83"],
            ["Private Sessions", "€1,598.40", "5%", "€79.92"],
            ["Other Revenue", "€234.50", "0%", "€0.00"]
        ]
        
        for row, data in enumerate(mgmt_data):
            for col, value in enumerate(data):
                mgmt_table.setItem(row, col, QTableWidgetItem(value))
        
        mgmt_layout.addWidget(mgmt_table)
        mgmt_tab.setLayout(mgmt_layout)
        
        # Exception handling tab
        exceptions_tab = QWidget()
        exceptions_layout = QVBoxLayout()
        
        exceptions_header = QLabel("Exceptions & Manual Overrides")
        exceptions_header.setFont(self.subheader_font)
        exceptions_layout.addWidget(exceptions_header)
        
        exceptions_table = QTableWidget(5, 6)
        exceptions_table.setHorizontalHeaderLabels([
            "Customer", "Issue Type", "Original Amount", "Override Amount", "Reason", "Action"
        ])
        
        exceptions_data = [
            ["John Smith", "Free Session", "€15.00", "€0.00", "Promotional class", "Approved"],
            ["Sarah Wilson", "Refund Applied", "€112.20", "€0.00", "Package refunded", "Pending"],
            ["Mike Garcia", "Discount", "€89.50", "€67.13", "Student discount", "Review"]
        ]
        
        for row, data in enumerate(exceptions_data):
            for col, value in enumerate(data):
                exceptions_table.setItem(row, col, QTableWidgetItem(value))
        
        exceptions_layout.addWidget(exceptions_table)
        exceptions_tab.setLayout(exceptions_layout)
        
        # Add tabs
        results_tabs.addTab(coach_tab, "Coach Payments")
        results_tabs.addTab(bgm_tab, "BGM Payments")
        results_tabs.addTab(mgmt_tab, "Management Payments")
        results_tabs.addTab(exceptions_tab, "Exceptions")
        
        layout.addWidget(results_tabs)
        
        widget.setLayout(layout)
        return widget

    def create_reports_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("Reports & Payslip Generation")
        header.setFont(self.header_font)
        layout.addWidget(header)
        
        # Report type selection
        report_group = QGroupBox("Report Generation")
        report_layout = QGridLayout()
        
        # Monthly summary report
        monthly_summary = QGroupBox("Monthly Summary Report")
        monthly_layout = QVBoxLayout()
        monthly_desc = QLabel("Generate comprehensive monthly payment summary for all parties")
        monthly_btn = QPushButton("Generate Monthly Summary")
        monthly_layout.addWidget(monthly_desc)
        monthly_layout.addWidget(monthly_btn)
        monthly_summary.setLayout(monthly_layout)
        
        # Individual payslips
        payslips_group = QGroupBox("Individual Payslips")
        payslips_layout = QVBoxLayout()
        
        # Coach selection
        coach_selection = QHBoxLayout()
        coach_label = QLabel("Select Coach:")
        coach_combo = QComboBox()
        coach_combo.addItems([
            "All Coaches", "Alice Smith", "Bob Johnson", "Charlie Wilson", 
            "Diana Garcia", "Eva Martinez", "Frank Lopez", "Grace Kim"
        ])
        coach_selection.addWidget(coach_label)
        coach_selection.addWidget(coach_combo)
        
        payslip_btn = QPushButton("Generate Payslips")
        
        payslips_layout.addLayout(coach_selection)
        payslips_layout.addWidget(payslip_btn)
        payslips_group.setLayout(payslips_layout)
        
        # BGM report
        bgm_group = QGroupBox("BGM (Landlord) Report")
        bgm_layout = QVBoxLayout()
        bgm_desc = QLabel("Generate detailed landlord payment report with breakdown")
        bgm_btn = QPushButton("Generate BGM Report")
        bgm_layout.addWidget(bgm_desc)
        bgm_layout.addWidget(bgm_btn)
        bgm_group.setLayout(bgm_layout)
        
        # Management report
        mgmt_group = QGroupBox("Management Report")
        mgmt_layout = QVBoxLayout()
        mgmt_desc = QLabel("Generate management team payment summary")
        mgmt_btn = QPushButton("Generate Management Report")
        mgmt_layout.addWidget(mgmt_desc)
        mgmt_layout.addWidget(mgmt_btn)
        mgmt_group.setLayout(mgmt_layout)
        
        # Add report groups to grid
        report_layout.addWidget(monthly_summary, 0, 0)
        report_layout.addWidget(payslips_group, 0, 1)
        report_layout.addWidget(bgm_group, 1, 0)
        report_layout.addWidget(mgmt_group, 1, 1)
        
        report_group.setLayout(report_layout)
        layout.addWidget(report_group)
        
        # Report history
        history_group = QGroupBox("Report History")
        history_layout = QVBoxLayout()
        
        history_table = QTableWidget(10, 5)
        history_table.setHorizontalHeaderLabels([
            "Date Generated", "Report Type", "Period", "Status", "Actions"
        ])
        
        # Sample history data
        history_data = [
            ["2025-06-05 14:30", "Monthly Summary", "May 2025", "Completed", "Download"],
            ["2025-06-05 14:25", "Coach Payslips", "May 2025", "Completed", "Download"],
            ["2025-06-05 14:20", "BGM Report", "May 2025", "Completed", "Download"],
            ["2025-05-01 16:45", "Monthly Summary", "April 2025", "Completed", "Download"],
            ["2025-05-01 16:40", "All Payslips", "April 2025", "Completed", "Download"]
        ]
        
        for row, data in enumerate(history_data):
            for col, value in enumerate(data):
                if col == 4:  # Actions
                    btn = QPushButton("Download")
                    history_table.setCellWidget(row, col, btn)
                else:
                    history_table.setItem(row, col, QTableWidgetItem(value))
        
        history_layout.addWidget(history_table)
        history_group.setLayout(history_layout)
        layout.addWidget(history_group)
        
        # Export options
        export_group = QGroupBox("Export Options")
        export_layout = QHBoxLayout()
        
        format_label = QLabel("Export Format:")
        format_combo = QComboBox()
        format_combo.addItems(["PDF", "Excel", "CSV"])
        
        save_check = QCheckBox("Save to local folder")
        save_check.setChecked(True)
        
        export_layout.addWidget(format_label)
        export_layout.addWidget(format_combo)
        export_layout.addStretch()
        export_layout.addWidget(save_check)
        
        export_group.setLayout(export_layout)
        layout.addWidget(export_group)
        
        widget.setLayout(layout)
        return widget

    def create_settings_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Header
        header = QLabel("System Settings")
        header.setFont(self.header_font)
        layout.addWidget(header)
        
        # Settings tabs
        settings_tabs = QTabWidget()
        
        # Coach management
        coaches_tab = QWidget()
        coaches_layout = QVBoxLayout()
        
        coaches_header = QLabel("Coach Management")
        coaches_header.setFont(self.subheader_font)
        coaches_layout.addWidget(coaches_header)
        
        # Add new coach section
        add_coach_group = QGroupBox("Add New Coach")
        add_coach_layout = QFormLayout()
        
        coach_name = QLineEdit()
        coach_email = QLineEdit()
        coach_rate = QDoubleSpinBox()
        coach_rate.setMaximum(999.99)
        coach_rate.setSuffix(" €/hour")
        coach_active = QCheckBox()
        coach_active.setChecked(True)
        
        add_coach_layout.addRow("Full Name:", coach_name)
        add_coach_layout.addRow("Email:", coach_email)
        add_coach_layout.addRow("Hourly Rate:", coach_rate)
        add_coach_layout.addRow("Active:", coach_active)
        
        add_coach_btn = QPushButton("Add Coach")
        add_coach_layout.addRow(add_coach_btn)
        add_coach_group.setLayout(add_coach_layout)
        coaches_layout.addWidget(add_coach_group)
        
        # Existing coaches table
        coaches_table_group = QGroupBox("Existing Coaches")
        coaches_table_layout = QVBoxLayout()
        
        coaches_table = QTableWidget(11, 5)
        coaches_table.setHorizontalHeaderLabels([
            "Coach Name", "Email", "Hourly Rate", "Status", "Actions"
        ])
        
        # Sample coach data
        coaches_data = [
            ["Alice Smith", "alice@mfc.com", "€45.00", "Active", "Edit"],
            ["Bob Johnson", "bob@mfc.com", "€40.00", "Active", "Edit"],
            ["Charlie Wilson", "charlie@mfc.com", "€42.00", "Active", "Edit"],
            ["Diana Garcia", "diana@mfc.com", "€38.00", "Active", "Edit"],
            ["Eva Martinez", "eva@mfc.com", "€41.00", "Active", "Edit"]
        ]
        
        for row, data in enumerate(coaches_data):
            for col, value in enumerate(data):
                if col == 4:  # Actions
                    btn = QPushButton("Edit")
                    coaches_table.setCellWidget(row, col, btn)
                else:
                    coaches_table.setItem(row, col, QTableWidgetItem(value))
        
        coaches_table_layout.addWidget(coaches_table)
        coaches_table_group.setLayout(coaches_table_layout)
        coaches_layout.addWidget(coaches_table_group)
        
        coaches_tab.setLayout(coaches_layout)
        
        # General settings
        general_tab = QWidget()
        general_layout = QVBoxLayout()
        
        general_header = QLabel("General Settings")
        general_header.setFont(self.subheader_font)
        general_layout.addWidget(general_header)
        
        # Company information
        company_group = QGroupBox("Company Information")
        company_layout = QFormLayout()
        
        company_name = QLineEdit("Malta Fight Co.")
        company_address = QTextEdit("123 Fight Street\nValletta, Malta\nMT-1234")
        company_address.setMaximumHeight(80)
        company_email = QLineEdit("info@maltafightco.com")
        tax_rate = QDoubleSpinBox()
        tax_rate.setValue(7.0)
        tax_rate.setSuffix(" %")
        
        company_layout.addRow("Company Name:", company_name)
        company_layout.addRow("Address:", company_address)
        company_layout.addRow("Email:", company_email)
        company_layout.addRow("Tax Rate:", tax_rate)
        company_group.setLayout(company_layout)
        general_layout.addWidget(company_group)
        
        # Default percentages
        defaults_group = QGroupBox("Default Payment Percentages")
        defaults_layout = QFormLayout()
        
        default_coach = QDoubleSpinBox()
        default_coach.setValue(43.5)
        default_coach.setSuffix(" %")
        
        default_bgm = QDoubleSpinBox()
        default_bgm.setValue(30.0)
        default_bgm.setSuffix(" %")
        
        default_mgmt = QDoubleSpinBox()
        default_mgmt.setValue(8.5)
        default_mgmt.setSuffix(" %")
        
        defaults_layout.addRow("Default Coach %:", default_coach)
        defaults_layout.addRow("Default BGM %:", default_bgm)
        defaults_layout.addRow("Default Management %:", default_mgmt)
        defaults_group.setLayout(defaults_layout)
        general_layout.addWidget(defaults_group)
        
        # Save button
        save_settings_btn = QPushButton("Save Settings")
        general_layout.addWidget(save_settings_btn)
        
        general_layout.addStretch()
        general_tab.setLayout(general_layout)
        
        # Database settings
        database_tab = QWidget()
        database_layout = QVBoxLayout()
        
        database_header = QLabel("Database & Backup Settings")
        database_header.setFont(self.subheader_font)
        database_layout.addWidget(database_header)
        
        # Backup settings
        backup_group = QGroupBox("Backup Configuration")
        backup_layout = QFormLayout()
        
        backup_location = QLineEdit("C:/MFC_Backups/")
        auto_backup = QCheckBox()
        auto_backup.setChecked(True)
        backup_frequency = QComboBox()
        backup_frequency.addItems(["Daily", "Weekly", "Monthly"])
        
        backup_layout.addRow("Backup Location:", backup_location)
        backup_layout.addRow("Auto Backup:", auto_backup)
        backup_layout.addRow("Frequency:", backup_frequency)
        
        backup_now_btn = QPushButton("Backup Now")
        backup_layout.addRow(backup_now_btn)
        backup_group.setLayout(backup_layout)
        database_layout.addWidget(backup_group)
        
        # Data maintenance
        maintenance_group = QGroupBox("Data Maintenance")
        maintenance_layout = QVBoxLayout()
        
        cleanup_btn = QPushButton("Clean Old Import Files")
        rebuild_btn = QPushButton("Rebuild Database Indexes")
        export_btn = QPushButton("Export All Data")
        
        maintenance_layout.addWidget(cleanup_btn)
        maintenance_layout.addWidget(rebuild_btn)
        maintenance_layout.addWidget(export_btn)
        maintenance_group.setLayout(maintenance_layout)
        database_layout.addWidget(maintenance_group)
        
        database_layout.addStretch()
        database_tab.setLayout(database_layout)
        
        # Add settings tabs
        settings_tabs.addTab(coaches_tab, "Coaches")
        settings_tabs.addTab(general_tab, "General")
        settings_tabs.addTab(database_tab, "Database")
        
        layout.addWidget(settings_tabs)
        widget.setLayout(layout)
        return widget


def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show main window
    window = MFCPaymentSystem()
    window.show()
    
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())