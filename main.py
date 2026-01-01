import flet as ft

class CalculatorApp:
    def __init__(self):
        self.expression = ""
        self.operators = {'+', '-', '*', '/'}
        
        # ألوان الأزرار
        self.button_colors = {
            'C': ft.colors.RED_300,      # أحفر فاتح
            '⌫': ft.colors.ORANGE_300,   # برتقالي
            '=': ft.colors.BLUE_300,     # أزرق
            '/': ft.colors.GREEN_300,    # أخضر
            '×': ft.colors.GREEN_300,    # أخضر
            '-': ft.colors.GREEN_300,    # أخضر
            '+': ft.colors.GREEN_300,    # أخضر
            '%': ft.colors.GREY_400,     # رمادي
            'default': ft.colors.GREY_900  # رمادي غامق
        }
        
        # حجم الخط
        self.display_font_size = 50
        self.button_font_size = 30
        
    def main(self, page: ft.Page):
        page.title = "آلة حاسبة"
        page.bgcolor = ft.colors.GREY_900
        page.horizontal_alignment = "center"
        page.vertical_alignment = "center"
        page.padding = 20
        
        # شاشة العرض
        self.display = ft.Text(
            value="0",
            size=self.display_font_size,
            color=ft.colors.WHITE,
            text_align="right",
            weight="bold",
            width=400,
            height=100
        )
        
        def on_button_click(e):
            current_text = e.control.content.value
            
            if current_text == 'C':
                self.expression = ""
                self.display.value = "0"
            
            elif current_text == '⌫':
                if self.expression:
                    self.expression = self.expression[:-1]
                    self.display.value = self.expression if self.expression else "0"
            
            elif current_text == '=':
                try:
                    expr = self.expression.replace('×', '*')
                    result = str(eval(expr))
                    self.display.value = result
                    self.expression = result
                except:
                    self.display.value = "خطأ!"
                    self.expression = ""
            
            elif current_text == '%':
                try:
                    result = str(eval(self.expression) / 100)
                    self.display.value = result
                    self.expression = result
                except:
                    self.display.value = "خطأ!"
                    self.expression = ""
            
            else:
                if self.display.value == "0" or self.display.value == "خطأ!":
                    self.expression = ""
                
                if current_text == '×':
                    self.expression += '*'
                elif current_text == '00':
                    self.expression += '00'
                else:
                    self.expression += current_text
                
                self.display.value = self.expression.replace('*', '×')
            
            page.update()
        
        def create_button(text):
            bgcolor = self.button_colors.get(text, self.button_colors['default'])
            
            return ft.Container(
                content=ft.Text(
                    text,
                    size=self.button_font_size,
                    color=ft.colors.WHITE,
                    weight="bold"
                ),
                width=85,
                height=85,
                border_radius=10,
                bgcolor=bgcolor,
                alignment=ft.alignment.center,
                on_click=on_button_click,
                animate=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN_OUT),
                padding=0,
                margin=0
            )
        
        # توزيع الأزرار
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['00', '0', '.', '=']
        ]
        
        # إنشاء الشبكة
        buttons_grid = ft.Column(spacing=5)
        
        for row in buttons:
            row_container = ft.Row(spacing=5, alignment="center")
            for btn_text in row:
                row_container.controls.append(create_button(btn_text))
            buttons_grid.controls.append(row_container)
        
        # الواجهة الرئيسية
        main_container = ft.Container(
            width=400,
            bgcolor=ft.colors.GREY_900,
            padding=20,
            border_radius=15,
            shadow=ft.BoxShadow(
                spread_radius=2,
                blur_radius=15,
                color=ft.colors.BLACK
            )
        )
        
        main_container.content = ft.Column(
            [
                ft.Container(
                    content=self.display,
                    bgcolor=ft.colors.GREY_800,
                    border_radius=10,
                    padding=10,
                    margin=ft.margin.only(bottom=20)
                ),
                buttons_grid
            ],
            spacing=0,
            horizontal_alignment="center"
        )
        
        page.add(main_container)

# تشغيل التطبيق
calculator = CalculatorApp()
ft.app(target=calculator.main)
